"""Demo learners, so Admin's numbers aren't all zero on day one. The lessons themselves are code (tr_*.py), not demo
data: they are always there. Loaded automatically the first time anyone opens the Learn page or the landing page
(ensure_loaded), removed or reloaded from Admin -> Demo data. Removing it is remembered: it doesn't come back.

Demo users have is_demo=True and @example.com emails; they can't sign in (no password). Every demo row is flagged
is_demo=True, so remove() deletes exactly what load() added.
"""
import datetime as dt

from anvil.tables import app_tables

from . import common as C

DEMO_USERS = [
    # name, email, how many lessons (in teaching order) they finished, how many cards they have reviewed
    ("Maya Chen", "maya.demo@example.com", 9, 30),
    ("Theo Martin", "theo.demo@example.com", 4, 12),
    ("Ines Ozola", "ines.demo@example.com", 17, 60),
]
# Tables that hold demo rows (each has an is_demo column). Children before parents.
DEMO_TABLES = ["card_reviews", "lesson_progress", "study_days"]


def state():
    return C.get_setting("demo", "never")  # "never" | "loaded" | "removed"


def ensure_loaded():
    if state() == "never":
        load()


def load():
    from . import Curriculum
    ix = Curriculum.index()
    remove(remember=False)
    now = C.now()
    for u_i, (name, email, n_lessons, n_cards) in enumerate(DEMO_USERS):
        u = app_tables.users.get(email=email) or app_tables.users.add_row(email=email, enabled=False)
        u.update(display_name=name, is_demo=True, signed_up=now - dt.timedelta(days=40 - 9 * u_i))
        lessons = ix["order"][:n_lessons]
        for k, lid in enumerate(lessons):
            when = now - dt.timedelta(days=n_lessons - k)
            app_tables.lesson_progress.add_row(user=u, lesson=lid, done=True, saved=k % 5 == 0, is_demo=True,
                                               done_at=when, opened_at=when)
        cards = [c for c in ix["cards"] if c.split("~")[0] in lessons][:n_cards]
        for k, cid in enumerate(cards):
            box = 1 + (k % 5)
            app_tables.card_reviews.add_row(user=u, card=cid, box=box, reviews=box + 1, knew=box, is_demo=True,
                                            last=now - dt.timedelta(days=k % 6), due=now + dt.timedelta(days=box * 2 - 3))
        for d in range(6):
            app_tables.study_days.add_row(user=u, day=(now - dt.timedelta(days=d)).date(), cards=4 + 3 * ((d + u_i) % 4),
                                          knew=3 + 2 * ((d + u_i) % 3), lessons=d % 2, is_demo=True)
    C.set_setting("demo", "loaded")
    return counts()


def remove(remember=True):
    for name in DEMO_TABLES:
        for r in getattr(app_tables, name).search(is_demo=True):
            r.delete()
    for u in app_tables.users.search(is_demo=True):
        u.delete()
    if remember:
        C.set_setting("demo", "removed")
    return counts()


def counts():
    out = {"users": len(app_tables.users.search(is_demo=True))}
    for name in DEMO_TABLES:
        out[name] = len(getattr(app_tables, name).search(is_demo=True))
    return out
