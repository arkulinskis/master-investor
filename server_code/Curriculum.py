"""The curriculum: tracks -> lessons -> cards, the glossary and the library. Read-only and public (guests learn too).

Content lives in plain Python data files, one per track (server_code/tr_<id>.py, schema in tools/content_check.py),
and the library in lib_data.py. This module indexes them once per server process and serves plain dicts.
A card's id is "<lesson id>~<n>" (n from 1), so it stays the same as long as cards are only added at the end.
"""
from typing import Any

import anvil.server

from . import common as C
from . import Study
from . import DemoData
from . import lib_data
from . import tr_foundations, tr_statements, tr_valuation, tr_instruments, tr_macro, tr_portfolio, tr_trading, tr_quant, tr_data

# The ladder, in teaching order. icon = a name from UI.ICONS (theme/assets/app-kit.js).
TRACK_MODULES = [(tr_foundations, "coins"), (tr_statements, "file"), (tr_valuation, "scale"), (tr_instruments, "layers"),
                 (tr_macro, "bank"), (tr_portfolio, "target"), (tr_trading, "pulse"), (tr_quant, "flask"), (tr_data, "code")]
LEVELS = ["Beginner", "Intermediate", "Advanced", "Pro"]

_idx: dict = {}


def index():
    """Build (once) the lookups every callable uses."""
    if _idx:
        return _idx
    tracks, lessons, cards, order = [], {}, {}, []
    for n, (mod, icon) in enumerate(TRACK_MODULES):
        tr: Any = mod.TRACK
        tr_lessons: list[Any] = tr["lessons"]
        t = {"id": tr["id"], "title": tr["title"], "level": tr["level"], "blurb": tr["blurb"], "icon": icon, "n": n + 1,
             "lessons": [L["id"] for L in tr_lessons],
             "minutes": sum(int(L["minutes"]) for L in tr_lessons), "cards": sum(len(L["cards"]) for L in tr_lessons)}
        tracks.append(t)
        for i, L in enumerate(tr_lessons):
            lessons[L["id"]] = dict(L, track=tr["id"], track_title=tr["title"], pos=i + 1)
            order.append(L["id"])
            for k, (q, a) in enumerate(L["cards"]):
                cid = "%s~%d" % (L["id"], k + 1)
                cards[cid] = {"id": cid, "q": q, "a": a, "lesson": L["id"], "lesson_title": L["title"],
                              "track": tr["id"], "track_title": tr["title"], "level": L["level"]}
    _idx.update(tracks=tracks, by_track={t["id"]: t for t in tracks}, lessons=lessons, cards=cards, order=order)
    return _idx


def lesson_row(L, done=None):
    """A lesson as a list row (no body)."""
    return {"id": L["id"], "title": L["title"], "level": L["level"], "minutes": L["minutes"], "summary": L["summary"],
            "track": L["track"], "track_title": L["track_title"], "pos": L["pos"], "cards": len(L["cards"]),
            "done": bool(done and L["id"] in done)}


def card_dict(c, box=None):
    return dict(c, box=box)


def _track_dict(t, done):
    n_done = len([i for i in t["lessons"] if i in done]) if done else 0
    return {"id": t["id"], "title": t["title"], "level": t["level"], "blurb": t["blurb"], "icon": t["icon"], "n": t["n"],
            "lessons": len(t["lessons"]), "minutes": t["minutes"], "cards": t["cards"], "done": n_done,
            "pct": int(round(100.0 * n_done / len(t["lessons"]))) if t["lessons"] else 0}


@anvil.server.callable
def get_learn():
    """The Learn page (and the landing ledger): every track with the caller's progress, plus a few sample cards."""
    ix = index()
    DemoData.ensure_loaded()
    me = C.me()
    done = Study.done_set(me) if me else set()
    tracks = [_track_dict(t, done) for t in ix["tracks"]]
    samples = [ix["cards"][cid] for cid in ("compounding~1", "dcf~1", "backtesting~1") if cid in ix["cards"]]
    if len(samples) < 3:  # content still growing: take the first card of three spread-out lessons
        order = ix["order"]
        picks = [order[0], order[len(order) // 2], order[-1]] if order else []
        samples = [ix["cards"]["%s~1" % p] for p in picks if "%s~1" % p in ix["cards"]]
    return {"tracks": tracks, "levels": LEVELS, "samples": samples,
            "totals": {"tracks": len(tracks), "lessons": len(ix["lessons"]), "cards": len(ix["cards"]),
                       "done": len(done), "terms": sum(len(L["terms"]) for L in ix["lessons"].values())},
            "next": Study.next_lesson(me, done) if me else None}


@anvil.server.callable
def get_track(track_id):
    ix = index()
    t = ix["by_track"].get(C.text(track_id, 40))
    if t is None:
        return C.fail("That track doesn't exist.")
    me = C.me()
    done = Study.done_set(me) if me else set()
    lessons = [lesson_row(ix["lessons"][i], done) for i in t["lessons"]]
    nxt = next((L for L in lessons if not L["done"]), None)
    pos = [x["id"] for x in ix["tracks"]].index(t["id"])
    prev_t = ix["tracks"][pos - 1] if pos > 0 else None
    next_t = ix["tracks"][pos + 1] if pos + 1 < len(ix["tracks"]) else None
    return C.ok(track=_track_dict(t, done), lessons=lessons, next_id=nxt["id"] if nxt else None,
                prev_track={"id": prev_t["id"], "title": prev_t["title"]} if prev_t else None,
                next_track={"id": next_t["id"], "title": next_t["title"]} if next_t else None)


def unwrap(md):
    """Join hard-wrapped lines inside a paragraph or list item (Anvil's markdown turns every newline into a line
    break). Blank lines, headings, list items, quotes and lines that are a formula on their own stay separate."""
    out: list = []
    for raw in (md or "").strip().splitlines():
        line = raw.rstrip()
        s = line.strip()
        starts_block = (not s or s.startswith(("#", "- ", "* ", "> ")) or (s[:1].isdigit() and ". " in s[:4])
                        or (s.startswith("`") and s.endswith("`")))
        prev = out[-1] if out else ""
        ps = prev.strip()
        prev_closed = (not ps or ps.startswith("#") or (ps.startswith("`") and ps.endswith("`") and not ps.startswith(("- ", "* "))))
        if out and not starts_block and not prev_closed:
            out[-1] = prev + " " + s
        else:
            out.append(line if not s.startswith(("- ", "* ")) else s)
    return "\n".join(out)


@anvil.server.callable
def get_lesson(lesson_id):
    ix = index()
    L = ix["lessons"].get(C.text(lesson_id, 80))
    if L is None:
        return C.fail("That lesson doesn't exist (it may have moved).")
    me = C.me()
    order = ix["order"]
    i = order.index(L["id"])
    prev_L = ix["lessons"][order[i - 1]] if i > 0 else None
    next_L = ix["lessons"][order[i + 1]] if i + 1 < len(order) else None
    mine = Study.lesson_state(me, L["id"]) if me else {"done": False, "saved": False}
    boxes = Study.boxes(me) if me else {}
    cards = [card_dict(ix["cards"]["%s~%d" % (L["id"], k + 1)], boxes.get("%s~%d" % (L["id"], k + 1)))
             for k in range(len(L["cards"]))]
    t = ix["by_track"][L["track"]]
    ex = L["example"]
    return C.ok(lesson={
        "id": L["id"], "title": L["title"], "level": L["level"], "minutes": L["minutes"], "summary": L["summary"],
        "body": unwrap(L["body"]), "example": {"title": ex["title"], "body": unwrap(ex["body"])} if ex else None,
        "calc": L["calc"],
        "terms": [{"term": a, "definition": b} for a, b in L["terms"]],
        "links": [{"label": a, "url": b} for a, b in L["links"]],
        "track": L["track"], "track_title": L["track_title"], "pos": L["pos"], "of": len(t["lessons"]),
        "done": mine["done"], "saved": mine["saved"]},
        cards=cards,
        prev={"id": prev_L["id"], "title": prev_L["title"]} if prev_L else None,
        next={"id": next_L["id"], "title": next_L["title"]} if next_L else None)


def _hit_score(L, words):
    hay_title = L["title"].lower()
    hay = " ".join([L["summary"], L["body"], " ".join(a + " " + b for a, b in L["terms"])]).lower()
    score = 0
    for w in words:
        if w in hay_title:
            score += 5
        elif w in hay:
            score += 1
        else:
            return 0
    return score


@anvil.server.callable
def search_lessons(query):
    """Lessons whose title, summary, text or terms contain every word of the query (title hits first)."""
    words = [w for w in C.text(query, 80).lower().split() if len(w) > 1]
    if not words:
        return {"results": [], "query": ""}
    ix = index()
    me = C.me()
    done = Study.done_set(me) if me else set()
    scored = [(_hit_score(L, words), n, L) for n, L in enumerate(ix["lessons"][i] for i in ix["order"])]
    hits = [lesson_row(L, done) for s, n, L in sorted([x for x in scored if x[0]], key=lambda x: (-x[0], x[1]))[:30]]
    return {"results": hits, "query": " ".join(words)}


@anvil.server.callable
def get_glossary():
    """Every key term from every lesson, A to Z, with the lesson it comes from."""
    ix = index()
    seen, terms = set(), []
    for lid in ix["order"]:
        L = ix["lessons"][lid]
        for term, definition in L["terms"]:
            key = term.lower()
            if key in seen:
                continue
            seen.add(key)
            terms.append({"term": term, "definition": definition, "lesson": L["id"], "lesson_title": L["title"],
                          "letter": term[:1].upper() if term[:1].isalpha() else "#"})
    terms.sort(key=lambda x: x["term"].lower())
    return {"terms": terms}


@anvil.server.callable
def get_library():
    """Data sources, GitHub repositories and books (server_code/lib_data.py)."""
    def clean(items):
        return [{k: v for k, v in it.items() if isinstance(v, (str, int, float, bool))} for it in items]
    return {"sources": clean(lib_data.SOURCES), "repos": clean(lib_data.REPOS), "books": clean(lib_data.BOOKS)}
