"""Learning progress: lessons done and saved, hide-and-reveal card reviews (spaced repetition), study days, decks,
and the member's dashboard.

Spaced repetition (Leitner boxes): a card starts in box 1. "Got it" moves it up a box and schedules it further out
(INTERVAL_DAYS); "Not yet" sends it back to box 1, due again in 10 minutes. Box 5 = mastered.
Guests can study every deck; nothing is saved for them (the page keeps the session score).
"""
import datetime as dt
import random

import anvil.server
from anvil.tables import app_tables
import anvil.tables as tables

from . import common as C

INTERVAL_DAYS = {1: 1, 2: 3, 3: 7, 4: 16, 5: 35}
MASTERED = 5
DECK_SIZE = 20
PLACEMENT = [("Beginner", 3), ("Intermediate", 3), ("Advanced", 3), ("Pro", 3)]


def _cur():
    from . import Curriculum
    return Curriculum


def today():
    return C.now().date()


# ------------------------------------------------------------------ reads used by Curriculum
def done_set(user):
    if user is None:
        return set()
    return {r["lesson"] for r in app_tables.lesson_progress.search(user=user, done=True)}


def lesson_state(user, lesson_id):
    r = app_tables.lesson_progress.get(user=user, lesson=lesson_id) if user else None
    if user is not None:
        if r is None:
            r = app_tables.lesson_progress.add_row(user=user, lesson=lesson_id, done=False, saved=False, is_demo=False)
        r["opened_at"] = C.now()
    return {"done": bool(r and r["done"]), "saved": bool(r and r["saved"])}


def boxes(user):
    if user is None:
        return {}
    return {r["card"]: int(r["box"] or 1) for r in app_tables.card_reviews.search(user=user)}


def next_lesson(user, done=None):
    """The lesson to continue with: after the last one opened, else the first one not done."""
    ix = _cur().index()
    done = done_set(user) if done is None else done
    order = ix["order"]
    opened = [r for r in app_tables.lesson_progress.search(tables.order_by("opened_at", ascending=False), user=user)
              if r["opened_at"] is not None and r["lesson"] in ix["lessons"]]
    if opened and opened[0]["lesson"] not in done:
        pick = opened[0]["lesson"]
    else:
        start = order.index(opened[0]["lesson"]) if opened else 0
        rest = [i for i in order[start:] + order[:start] if i not in done]
        pick = rest[0] if rest else None
    if pick is None:
        return None
    return _cur().lesson_row(ix["lessons"][pick], done)


def _day(user):
    d = today()
    r = app_tables.study_days.get(user=user, day=d)
    if r is None:
        r = app_tables.study_days.add_row(user=user, day=d, cards=0, knew=0, lessons=0, is_demo=False)
    return r


def streak(user):
    """Consecutive study days up to today (or up to yesterday, if today has nothing yet)."""
    days = {r["day"] for r in app_tables.study_days.search(user=user) if (r["cards"] or 0) + (r["lessons"] or 0) > 0}
    d = today()
    if d not in days:
        d = d - dt.timedelta(days=1)
    n = 0
    while d in days:
        n += 1
        d = d - dt.timedelta(days=1)
    return n


# ------------------------------------------------------------------ lessons
@anvil.server.callable(require_user=True)
def mark_lesson(lesson_id, done=True):
    me = C.require_user()
    ix = _cur().index()
    lesson_id = C.text(lesson_id, 80)
    if lesson_id not in ix["lessons"]:
        return C.fail("That lesson doesn't exist.")
    r = app_tables.lesson_progress.get(user=me, lesson=lesson_id) or app_tables.lesson_progress.add_row(
        user=me, lesson=lesson_id, done=False, saved=False, is_demo=False)
    was = bool(r["done"])
    r.update(done=bool(done), done_at=C.now() if done else None)
    if done and not was:
        day = _day(me)
        day["lessons"] = (day["lessons"] or 0) + 1
    track = ix["lessons"][lesson_id]["track"]
    t = ix["by_track"][track]
    mine = done_set(me)
    return C.ok(done=bool(done), track_done=all(i in mine for i in t["lessons"]), streak=streak(me))


@anvil.server.callable(require_user=True)
def save_lesson(lesson_id, saved=True):
    me = C.require_user()
    lesson_id = C.text(lesson_id, 80)
    if lesson_id not in _cur().index()["lessons"]:
        return C.fail("That lesson doesn't exist.")
    r = app_tables.lesson_progress.get(user=me, lesson=lesson_id) or app_tables.lesson_progress.add_row(
        user=me, lesson=lesson_id, done=False, saved=False, is_demo=False)
    r["saved"] = bool(saved)
    return C.ok(saved=bool(saved))


# ------------------------------------------------------------------ cards
@anvil.server.callable(require_user=True)
def review_card(card_id, knew):
    """Record one reveal: knew=True ("Got it") moves the card up a box; False ("Not yet") back to box 1."""
    me = C.require_user()
    card_id = C.text(card_id, 100)
    if card_id not in _cur().index()["cards"]:
        return C.fail("That card doesn't exist any more.")
    if C.rate_limited("review", 600, 3600):
        return C.fail("That's a lot of cards in one hour. Take a break and come back fresh.")
    r = app_tables.card_reviews.get(user=me, card=card_id)
    if r is None:
        r = app_tables.card_reviews.add_row(user=me, card=card_id, box=0, reviews=0, knew=0, is_demo=False)
    box = int(r["box"] or 0)
    box = min(max(box, 1) + 1, MASTERED) if knew and box > 0 else (2 if knew else 1)
    due = C.now() + (dt.timedelta(days=INTERVAL_DAYS[box]) if knew else dt.timedelta(minutes=10))
    r.update(box=box, due=due, reviews=(r["reviews"] or 0) + 1, knew=(r["knew"] or 0) + (1 if knew else 0), last=C.now())
    day = _day(me)
    day.update(cards=(day["cards"] or 0) + 1, knew=(day["knew"] or 0) + (1 if knew else 0))
    return C.ok(box=box, due=C.iso(due), mastered=box >= MASTERED)


def _due_cards(user):
    ix = _cur().index()
    now = C.now()
    rows = [r for r in app_tables.card_reviews.search(user=user) if r["card"] in ix["cards"]]
    due = sorted([r for r in rows if r["due"] is None or r["due"] <= now], key=lambda r: (r["box"] or 0, r["due"] or now))
    seen = {r["card"] for r in rows}
    fresh = []
    done = done_set(user)
    for lid in ix["order"]:  # new cards from lessons the person has finished, in teaching order
        if lid in done:
            fresh += [c for c in ix["cards"] if c.startswith(lid + "~") and c not in seen]
    return [(r["card"], int(r["box"] or 1)) for r in due], fresh


@anvil.server.callable
def get_deck(mode, arg=None):
    """A practice deck. mode: due (members) | mixed | level <Beginner..Pro> | track <id> | lesson <id> | placement | saved."""
    ix = _cur().index()
    me = C.me()
    mode = C.text(mode, 20)
    arg = C.text(arg, 80) if arg else ""
    bx = boxes(me)
    cards = ix["cards"]
    title, ids = "", []
    rng = random.Random()
    if mode == "due":
        if me is None:
            return C.fail("Sign in to keep a review schedule. Until then, try a mixed deck.")
        due, fresh = _due_cards(me)
        ids = [c for c, b in due][:DECK_SIZE]
        ids += fresh[:max(0, DECK_SIZE - len(ids))]
        title = "Due for review"
    elif mode == "mixed":
        ids = rng.sample(list(cards), min(DECK_SIZE, len(cards)))
        title = "Mixed deck"
    elif mode == "level":
        if arg not in _cur().LEVELS:
            return C.fail("Pick a level: Beginner, Intermediate, Advanced or Pro.")
        pool = [c for c, v in cards.items() if v["level"] == arg]
        ids = rng.sample(pool, min(DECK_SIZE, len(pool)))
        title = arg + " cards"
    elif mode == "track":
        t = ix["by_track"].get(arg)
        if t is None:
            return C.fail("That track doesn't exist.")
        pool = [c for c, v in cards.items() if v["track"] == arg]
        ids = rng.sample(pool, min(DECK_SIZE, len(pool)))
        title = t["title"]
    elif mode == "lesson":
        L = ix["lessons"].get(arg)
        if L is None:
            return C.fail("That lesson doesn't exist.")
        ids = ["%s~%d" % (arg, k + 1) for k in range(len(L["cards"]))]
        title = L["title"]
    elif mode == "saved":
        if me is None:
            return C.fail("Sign in to save lessons.")
        saved = [r["lesson"] for r in app_tables.lesson_progress.search(user=me, saved=True) if r["lesson"] in ix["lessons"]]
        pool = [c for c, v in cards.items() if v["lesson"] in saved]
        ids = rng.sample(pool, min(DECK_SIZE, len(pool)))
        title = "Saved lessons"
    elif mode == "placement":
        for level, n in PLACEMENT:
            pool = [c for c, v in cards.items() if v["level"] == level]
            ids += rng.sample(pool, min(n, len(pool)))
        title = "Placement check"
    else:
        return C.fail("Unknown deck.")
    return C.ok(title=title, mode=mode, arg=arg, cards=[dict(cards[c], box=bx.get(c)) for c in ids],
                saving=me is not None)


@anvil.server.callable
def get_practice():
    """The Practice page's menu: counts per deck, and the member's due count."""
    ix = _cur().index()
    me = C.me()
    out = {"total": len(ix["cards"]),
           "levels": [{"level": lv, "count": len([c for c in ix["cards"].values() if c["level"] == lv])} for lv in _cur().LEVELS],
           "tracks": [{"id": t["id"], "title": t["title"], "cards": t["cards"]} for t in ix["tracks"]],
           "signed_in": me is not None, "due": 0, "fresh": 0, "saved": 0, "mastered": 0}
    if me is not None:
        due, fresh = _due_cards(me)
        out.update(due=len(due), fresh=len(fresh),
                   saved=len(app_tables.lesson_progress.search(user=me, saved=True)),
                   mastered=len([r for r in app_tables.card_reviews.search(user=me) if (r["box"] or 0) >= MASTERED]))
    return out


def placement_result(right_by_level):
    """Where to start, from a placement check: the first level with fewer than 2 of 3 right."""
    for level, n in PLACEMENT:
        if int(right_by_level.get(level, 0)) < 2:
            return level
    return "Pro"


@anvil.server.callable
def placement_advice(right_by_level):
    """Turn {level: number right} into a starting point (a track and its first lesson)."""
    if not isinstance(right_by_level, dict):
        return C.fail("No answers to score.")
    level = placement_result(right_by_level)
    start = {"Beginner": "foundations", "Intermediate": "statements", "Advanced": "portfolio", "Pro": "quant"}[level]
    ix = _cur().index()
    t = ix["by_track"].get(start) or ix["tracks"][0]
    words = {"Beginner": "Start at the beginning: the Foundations track builds everything else.",
             "Intermediate": "You know the basics. Start with reading companies and valuing them.",
             "Advanced": "You're past the fundamentals. Portfolio construction, risk and trading are your next steps.",
             "Pro": "You know this well. Go straight to the quant's world, and use the rest as a refresher."}[level]
    return C.ok(level=level, text=words, track={"id": t["id"], "title": t["title"]}, first_lesson=t["lessons"][0])


# ------------------------------------------------------------------ the member's dashboard
@anvil.server.callable(require_user=True)
def get_home():
    me = C.require_user()
    ix = _cur().index()
    done = done_set(me)
    due, fresh = _due_cards(me)
    reviews = list(app_tables.card_reviews.search(user=me))
    by_day = {r["day"]: r for r in app_tables.study_days.search(user=me)}
    week = []
    for k in range(6, -1, -1):
        d = today() - dt.timedelta(days=k)
        r = by_day.get(d)
        week.append({"day": d.isoformat(), "cards": int(r["cards"] or 0) if r else 0, "knew": int(r["knew"] or 0) if r else 0,
                     "lessons": int(r["lessons"] or 0) if r else 0, "today": k == 0})
    tracks = []
    for t in ix["tracks"]:
        n = len([i for i in t["lessons"] if i in done])
        tracks.append({"id": t["id"], "title": t["title"], "icon": t["icon"], "level": t["level"], "done": n,
                       "lessons": len(t["lessons"]), "pct": int(round(100.0 * n / len(t["lessons"]))) if t["lessons"] else 0})
    saved = [_cur().lesson_row(ix["lessons"][r["lesson"]], done)
             for r in app_tables.lesson_progress.search(tables.order_by("opened_at", ascending=False), user=me, saved=True)
             if r["lesson"] in ix["lessons"]]
    return {"streak": streak(me), "due": len(due), "fresh": len(fresh), "week": week, "tracks": tracks, "saved": saved[:12],
            "next": next_lesson(me, done),
            "stats": {"lessons_done": len(done), "lessons": len(ix["lessons"]), "cards_seen": len(reviews),
                      "cards": len(ix["cards"]), "mastered": len([r for r in reviews if (r["box"] or 0) >= MASTERED]),
                      "reviews": sum(int(r["reviews"] or 0) for r in reviews)}}


@anvil.server.callable(require_user=True)
def reset_progress():
    """Delete all of this person's study data (lessons, cards, days). Their account stays."""
    me = C.require_user()
    for name in ("card_reviews", "lesson_progress", "study_days"):
        for r in getattr(app_tables, name).search(user=me):
            r.delete()
    return C.ok()
