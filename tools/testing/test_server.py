"""Server tests against the strict mock of Anvil (tools/testing/mock).

    python tools/testing/test_server.py          -> prints ALL OK, or the first failure

call(name, ...) runs a server function the way the browser does: by name, with require_user enforced,
and the reply must be JSON (a datetime or a row in a reply fails here, like it would break the page).
Add tests for every new server function: the happy path, bad input, and someone who isn't allowed.
"""
import datetime as dt
import importlib
import json
import os
import pathlib
import shutil
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
PROJECT = HERE.parents[1]
_tmp = pathlib.Path(tempfile.mkdtemp())
shutil.copytree(PROJECT / "server_code", _tmp / "app")
(_tmp / "app" / "__init__.py").write_text("")
os.environ["ANVIL_APP_YAML"] = str(PROJECT / "anvil.yaml")  # the mock's tables follow the app's own schema
sys.path[:0] = [str(HERE / "mock"), str(_tmp)]
import anvil.server  # noqa: E402
import anvil.users  # noqa: E402
import anvil.secrets  # noqa: E402
anvil.secrets.SECRETS["admin_emails"] = "admin@example.com"  # the App Secret, faked
from anvil.tables import app_tables as T  # noqa: E402

M = {p.stem: importlib.import_module("app." + p.stem) for p in sorted((PROJECT / "server_code").glob("*.py"))}
now = dt.datetime.now(dt.timezone.utc)


def call(name, *args):
    r = anvil.server.call(name, *args)
    json.dumps(r)  # strict: must be JSON-able
    return r


def as_user(row):
    anvil.users.CURRENT[0] = row
    anvil.server.session.use(row.get_id() if row is not None else None)


def denied(name, *args):
    try:
        call(name, *args)
    except anvil.server.PermissionDenied:
        return True
    return False


def ok(r, msg=""):
    assert isinstance(r, dict) and r.get("ok"), (msg, r)
    return r


def bad(r, msg=""):
    assert isinstance(r, dict) and r.get("ok") is False and r.get("error"), (msg, r)
    return r


def person(email, name=None, **kw):
    return T.users.add_row(email=email, enabled=True, signed_up=now, display_name=name, **kw)


# ---------------------------------------------------------------------------------- accounts
admin = person("admin@example.com", "The Admin")
ana = person("ana@example.com", "Ana")
bob = person("bob@example.com")

as_user(None)
assert call("get_me") is None
assert denied("update_profile", "X")
as_user(admin)
assert call("get_me")["is_admin"] is True, "ADMIN_EMAILS become admins on first sign-in"
as_user(ana)
me = call("get_me")
assert me["name"] == "Ana" and me["is_admin"] is False
assert ana["last_seen"] is not None
as_user(bob)
assert call("get_me")["name"] == "Bob", "a name comes from the email when none is set"
bad(call("update_profile", " x "))
assert ok(call("update_profile", "  Bob   Stone "))["me"]["name"] == "Bob Stone"

# ---------------------------------------------------------------------------------- feedback
as_user(None)
bad(call("submit_feedback", "bug", "hi"))
ok(call("submit_feedback", "bug", "The button is broken", "guest@example.com", {"page": "#home", "evil": "x" * 9999}))
fb = T.feedback.search()[0]
assert fb["name"] == "Guest" and fb["email"] == "guest@example.com" and "evil" not in fb["context"] and fb["status"] == "new"
for i in range(4):
    ok(call("submit_feedback", "idea", "Idea number %d" % i))
bad(call("submit_feedback", "idea", "One too many this hour"), "rate limit")
as_user(ana)
ok(call("submit_feedback", "nonsense-kind", "Signed-in feedback"))
assert T.feedback.get(message="Signed-in feedback")["kind"] == "other"
assert denied("list_feedback")
as_user(admin)
lst = call("list_feedback")
assert lst["counts"]["new"] == 6 and len(lst["items"]) == 6
fid = lst["items"][0]["id"]
ok(call("set_feedback_status", fid, "done", "Fixed it"))
assert call("list_feedback", "done")["items"][0]["note"] == "Fixed it"
bad(call("set_feedback_status", fid, "weird"))
bad(call("set_feedback_status", "nope", "done"))
ok(call("delete_feedback", fid))
assert len(call("list_feedback")["items"]) == 5

# ---------------------------------------------------------------------------------- admin
as_user(ana)
for fn, args in [("admin_overview", ()), ("list_users", ()), ("set_admin", (bob.get_id(), True)), ("demo_load", ()), ("demo_remove", ())]:
    assert denied(fn, *args), fn
as_user(admin)
ov = call("admin_overview")
assert ov["users"] == 3 and ov["admins"] == 1 and ov["feedback_new"] == 5 and ov["lessons_done"] == 0
assert len(call("list_users")["users"]) == 3 and len(call("list_users", "bob")["users"]) == 1
ok(call("set_admin", bob.get_id(), True))
assert bob["is_admin"] is True
bad(call("set_admin", admin.get_id(), False), "can't remove your own admin")
ok(call("set_enabled", bob.get_id(), False))
assert bob["enabled"] is False
bad(call("set_enabled", admin.get_id(), False))
ok(call("set_enabled", bob.get_id(), True))
ok(call("set_admin", bob.get_id(), False))
assert bob["is_admin"] is False

# ---------------------------------------------------------------------------------- curriculum (public)
as_user(None)
learn = call("get_learn")
assert M["DemoData"].state() == "loaded", "demo learners load on the first visit"
assert learn["totals"]["tracks"] == 9 and learn["totals"]["lessons"] >= 50 and learn["totals"]["cards"] >= 300, learn["totals"]
assert len(learn["samples"]) == 3 and all(c["q"] and c["a"] for c in learn["samples"])
assert learn["next"] is None and all(t["done"] == 0 for t in learn["tracks"])
ix = M["Curriculum"].index()
assert len(set(ix["order"])) == len(ix["order"]), "lesson ids are unique"
tr = ok(call("get_track", "valuation"))
assert tr["lessons"][0]["id"] == "price-vs-value" and tr["prev_track"]["id"] == "statements" and tr["next_track"]["id"] == "instruments"
bad(call("get_track", "nope"))
les = ok(call("get_lesson", "dcf"))
assert les["lesson"]["calc"] == "dcf" and les["cards"] and les["cards"][0]["id"] == "dcf~1" and les["lesson"]["done"] is False
assert les["prev"]["id"] == "multiples" and les["next"]["id"] == "discount-rates"
assert ok(call("get_lesson", ix["order"][0]))["prev"] is None and ok(call("get_lesson", ix["order"][-1]))["next"] is None
bad(call("get_lesson", "../etc"))
hits = call("search_lessons", "discounted cash flow")["results"]
assert hits and hits[0]["id"] in ("dcf", "reverse-dcf", "discount-rates"), [h["id"] for h in hits[:3]]
assert call("search_lessons", "zzqqxx")["results"] == [] and call("search_lessons", " ")["results"] == []
gl = call("get_glossary")["terms"]
assert len(gl) > 150 and len({t["term"].lower() for t in gl}) == len(gl), "glossary has no duplicates"
assert [t["term"].lower() for t in gl] == sorted(t["term"].lower() for t in gl)
lib = call("get_library")
assert len(lib["sources"]) >= 20 and len(lib["repos"]) >= 20 and len(lib["books"]) >= 10

# ---------------------------------------------------------------------------------- practice decks
pr = call("get_practice")
assert pr["signed_in"] is False and pr["total"] == learn["totals"]["cards"] and len(pr["levels"]) == 4
bad(call("get_deck", "due"), "guests have no schedule")
bad(call("get_deck", "saved"))
assert len(ok(call("get_deck", "mixed"))["cards"]) == 20
assert all(c["level"] == "Pro" for c in ok(call("get_deck", "level", "Pro"))["cards"])
bad(call("get_deck", "level", "Wizard"))
assert all(c["track"] == "quant" for c in ok(call("get_deck", "track", "quant"))["cards"])
bad(call("get_deck", "track", "nope"))
assert [c["id"] for c in ok(call("get_deck", "lesson", "dcf"))["cards"]] == [c["id"] for c in les["cards"]]
pl = ok(call("get_deck", "placement"))["cards"]
assert len(pl) == 12 and [c["level"] for c in pl] == ["Beginner"] * 3 + ["Intermediate"] * 3 + ["Advanced"] * 3 + ["Pro"] * 3
bad(call("get_deck", "weird"))
assert ok(call("placement_advice", {"Beginner": 3, "Intermediate": 1}))["level"] == "Intermediate"
assert ok(call("placement_advice", {}))["track"]["id"] == "foundations"
assert ok(call("placement_advice", {"Beginner": 3, "Intermediate": 3, "Advanced": 2, "Pro": 2}))["level"] == "Pro"
bad(call("placement_advice", "nope"))

# ---------------------------------------------------------------------------------- study progress (members)
for fn, args in [("mark_lesson", ("dcf",)), ("save_lesson", ("dcf",)), ("review_card", ("dcf~1", True)), ("get_home", ()), ("reset_progress", ())]:
    assert denied(fn, *args), fn
as_user(ana)
assert call("get_learn")["next"]["id"] == ix["order"][0], "a new member starts at the first lesson"
call("get_lesson", "compounding")  # opening a lesson remembers it
assert call("get_learn")["next"]["id"] == "compounding"
r = ok(call("mark_lesson", "compounding", True))
assert r["done"] and r["track_done"] is False and r["streak"] == 1
assert call("get_learn")["next"]["id"] == "risk-and-return", "after a finished lesson comes the next one"
bad(call("mark_lesson", "nope"))
ok(call("save_lesson", "dcf", True))
assert ok(call("get_lesson", "compounding"))["lesson"]["done"] is True
assert call("get_track", "foundations")["track"]["done"] == 1
home = call("get_home")
assert home["stats"]["lessons_done"] == 1 and home["fresh"] == len(ix["lessons"]["compounding"]["cards"]) and home["due"] == 0
assert home["saved"][0]["id"] == "dcf" and home["streak"] == 1 and home["week"][-1]["today"] and home["week"][-1]["lessons"] == 1
due = ok(call("get_deck", "due"))["cards"]
assert due and all(c["lesson"] == "compounding" for c in due), "new cards come from finished lessons"
assert ok(call("get_deck", "saved"))["cards"] and all(c["lesson"] == "dcf" for c in ok(call("get_deck", "saved"))["cards"])
r1 = ok(call("review_card", "compounding~1", True))
assert r1["box"] == 2 and not r1["mastered"]
r2 = ok(call("review_card", "compounding~2", False))
assert r2["box"] == 1
bad(call("review_card", "nope~1", True))
row = T.card_reviews.get(user=ana, card="compounding~2")
row["due"] = now - dt.timedelta(minutes=1)
due = ok(call("get_deck", "due"))["cards"]
assert due[0]["id"] == "compounding~2", "cards due come first"
assert "compounding~1" not in [c["id"] for c in due], "a known card waits for its interval"
for _ in range(4):
    last = ok(call("review_card", "compounding~1", True))
assert last["box"] == 5 and last["mastered"], "box 5 = mastered"
assert call("get_home")["stats"]["mastered"] == 1 and call("get_practice")["mastered"] == 1
assert ok(call("get_lesson", "compounding"))["cards"][0]["box"] == 5
as_user(bob)
assert call("get_home")["stats"]["lessons_done"] == 0, "progress is private to each member"
assert T.card_reviews.get(user=bob, card="compounding~1") is None
as_user(ana)
ok(call("mark_lesson", "compounding", False))
assert call("get_home")["stats"]["lessons_done"] == 0
ok(call("reset_progress"))
assert not T.card_reviews.search(user=ana) and not T.lesson_progress.search(user=ana) and not T.study_days.search(user=ana)

# ---------------------------------------------------------------------------------- demo data
as_user(admin)
ov = call("admin_overview")
assert ov["lessons_done"] > 0 and ov["reviews"] > 0 and ov["top"] and ov["top"][0]["count"] == len(M["DemoData"].DEMO_USERS)
ok(call("demo_remove"))
assert M["DemoData"].state() == "removed" and not T.users.search(is_demo=True) and not T.card_reviews.search(is_demo=True)
as_user(None)
call("get_learn")
assert M["DemoData"].state() == "removed", "removed demo data doesn't come back by itself"
as_user(admin)
ok(call("demo_load"))
n_rows = len(T.lesson_progress.search(is_demo=True))
ok(call("demo_load"))
assert len(T.lesson_progress.search(is_demo=True)) == n_rows > 0, "reloading replaces the demo instead of doubling it"

# ---------------------------------------------------------------------------------- Privacy & Terms
if "legal_server" in M:
    as_user(ana)
    st = call("legal_state")
    assert st["signedIn"] and st["accepted_version"] is None
    ok(call("legal_accept", st["version"], "signup"))
    assert ana["legal_source"] == "signup" and call("legal_state")["accepted_version"] == st["version"]

# ---------------------------------------------------------------------------------- schema check (App Board): names only, never data
r = anvil.server.ENDPOINTS["/schema-check"](tables="users, lesson_progress,no_such_table")
json.dumps(r)
assert "email" in r["tables"]["users"] and "lesson" in r["tables"]["lesson_progress"] and r["tables"]["no_such_table"] is None, r

# ---------------------------------------------------------------------------------- every callable is covered by a permission check
# A callable that changes data without require_user / a C.require_* check is a security hole. List the public ones here.
PUBLIC = {"log_client_error", "get_me", "session_ping", "submit_feedback", "legal_state", "legal_accept",
          "get_learn", "get_track", "get_lesson", "search_lessons", "get_glossary", "get_library",
          "get_deck", "get_practice", "placement_advice"}
for name, (f, need) in sorted(anvil.server.CALLABLES.items()):
    if name in PUBLIC:
        continue
    assert need, "%s is callable by anyone: add require_user=True (or list it in PUBLIC in test_server.py)" % name

print("ALL OK (%d server functions)" % len(anvil.server.CALLABLES))
