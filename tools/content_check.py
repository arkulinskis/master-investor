"""Check the curriculum files (server_code/tr_*.py) and the library (server_code/lib_data.py).

    python -I tools/content_check.py            -> prints a summary, or every problem found

A track file defines TRACK = {"id", "title", "level", "blurb", "lessons": [lesson, ...]}.
A lesson is a dict:
    id        lowercase-hyphen slug, unique across ALL tracks
    title     short title (<= 60 characters)
    level     "Beginner" | "Intermediate" | "Advanced" | "Pro"
    minutes   reading time, 3..15
    summary   one sentence (<= 160 characters)
    body      markdown (### subheadings, paragraphs, - lists, 1. lists, **bold**, *italic*, `formula`, > rule of thumb)
              no tables, no HTML tags, no links, no level-1/level-2 headings; 180..650 words
    example   {"title": str, "body": markdown} a worked example with real-looking numbers (or None)
    terms     list of (term, definition) tuples, 3..7
    cards     list of (question, answer) tuples, 6..9: the hide-and-reveal self-test cards
    calc      None or one of CALCS (a calculator on the Tools page that fits the lesson)
    links     list of (label, url) tuples, 0..4, only stable, well-known https URLs
House style: no em dashes or en dashes anywhere (use commas, colons, "to"), plain clear English.
"""
import importlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "server_code"))

LEVELS = {"Beginner", "Intermediate", "Advanced", "Pro"}
CALCS = {"compound", "dcf", "position", "kelly", "bond", "options", "sharpe"}
problems = []


def bad(where, msg):
    problems.append("%s: %s" % (where, msg))


def words(s):
    return len(re.findall(r"[A-Za-z0-9%$]+", s or ""))


def text_ok(where, s):
    if not isinstance(s, str):
        bad(where, "not a string")
        return
    if "—" in s or "–" in s:
        bad(where, "em/en dash found (house style: none)")
    if re.search(r"</?[a-zA-Z][^>]*>", s):
        bad(where, "HTML tag found")


def md_ok(where, s):
    text_ok(where, s)
    if not isinstance(s, str):
        return
    for line in s.splitlines():
        t = line.strip()
        if t.startswith("|") and t.endswith("|"):
            bad(where, "markdown table (not allowed): " + t[:40])
        if re.match(r"^#{1,2} ", t):
            bad(where, "use ### for subheadings, not # or ##: " + t[:40])
    if re.search(r"\]\(https?://", s):
        bad(where, "links go in 'links', not in the markdown")


def check_track(mod_name):
    mod = importlib.import_module(mod_name)
    tr = getattr(mod, "TRACK", None)
    if not isinstance(tr, dict):
        bad(mod_name, "no TRACK dict")
        return []
    for k in ("id", "title", "level", "blurb", "lessons"):
        if k not in tr:
            bad(mod_name, "TRACK missing " + k)
    text_ok(mod_name + ".blurb", tr.get("blurb", ""))
    out = []
    for i, L in enumerate(tr.get("lessons", [])):
        w = "%s lesson %d (%s)" % (mod_name, i + 1, L.get("id"))
        need = ("id", "title", "level", "minutes", "summary", "body", "example", "terms", "cards", "calc", "links")
        for k in need:
            if k not in L:
                bad(w, "missing " + k)
        if not re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", str(L.get("id", ""))):
            bad(w, "id must be a lowercase-hyphen slug")
        if len(L.get("title", "")) > 60:
            bad(w, "title over 60 characters")
        if L.get("level") not in LEVELS:
            bad(w, "level must be one of %s" % sorted(LEVELS))
        if not isinstance(L.get("minutes"), int) or not 3 <= L.get("minutes", 0) <= 15:
            bad(w, "minutes must be an int 3..15")
        if len(L.get("summary", "")) > 160:
            bad(w, "summary over 160 characters")
        text_ok(w + " title", L.get("title", ""))
        text_ok(w + " summary", L.get("summary", ""))
        md_ok(w + " body", L.get("body", ""))
        n = words(L.get("body", ""))
        if not 180 <= n <= 650:
            bad(w, "body has %d words (180..650)" % n)
        ex = L.get("example")
        if ex is not None:
            if not isinstance(ex, dict) or set(ex) != {"title", "body"}:
                bad(w, "example must be None or {'title', 'body'}")
            else:
                text_ok(w + " example title", ex["title"])
                md_ok(w + " example", ex["body"])
        terms = L.get("terms", [])
        if not 3 <= len(terms) <= 7:
            bad(w, "%d terms (3..7)" % len(terms))
        for t in terms:
            if not (isinstance(t, tuple) and len(t) == 2):
                bad(w, "term must be a (term, definition) tuple: %r" % (t,))
                continue
            text_ok(w + " term", t[0])
            text_ok(w + " term", t[1])
        cards = L.get("cards", [])
        if not 6 <= len(cards) <= 9:
            bad(w, "%d cards (6..9)" % len(cards))
        for c in cards:
            if not (isinstance(c, tuple) and len(c) == 2 and c[0] and c[1]):
                bad(w, "card must be a (question, answer) tuple: %r" % (c,))
                continue
            text_ok(w + " card", c[0])
            text_ok(w + " card", c[1])
            if len(c[1]) > 520:
                bad(w, "card answer over 520 characters: " + c[0][:40])
        if L.get("calc") is not None and L.get("calc") not in CALCS:
            bad(w, "calc must be None or one of %s" % sorted(CALCS))
        for ln in L.get("links", []):
            if not (isinstance(ln, tuple) and len(ln) == 2 and str(ln[1]).startswith("https://")):
                bad(w, "link must be (label, https url): %r" % (ln,))
        out.append(L)
    return out


def main():
    mods = sorted(p.stem for p in (ROOT / "server_code").glob("tr_*.py"))
    ids, total_cards, total = {}, 0, 0
    for m in mods:
        lessons = check_track(m)
        for L in lessons:
            if L.get("id") in ids:
                bad(m, "lesson id %s also in %s" % (L["id"], ids[L["id"]]))
            ids[L.get("id")] = m
            total_cards += len(L.get("cards", []))
        total += len(lessons)
        print("  %-22s %2d lessons" % (m, len(lessons)))
    lib = ROOT / "server_code" / "lib_data.py"
    if lib.exists():
        ld = importlib.import_module("lib_data")
        for kind in ("SOURCES", "REPOS", "BOOKS"):
            items = getattr(ld, kind, None)
            if not isinstance(items, list):
                bad("lib_data", kind + " missing")
                continue
            for it in items:
                if not isinstance(it, dict) or not str(it.get("url", "")).startswith("https://"):
                    bad("lib_data." + kind, "item needs an https url: %r" % (it,))
                    continue
                for k, v in it.items():
                    if isinstance(v, str):
                        text_ok("lib_data.%s %s" % (kind, it.get("name")), v)
            print("  lib_data.%-12s %2d items" % (kind, len(items)))
    print("%d lessons, %d cards in %d tracks" % (total, total_cards, len(mods)))
    if problems:
        print("\n".join(["PROBLEMS:"] + problems))
        sys.exit(1)
    print("CONTENT OK")


if __name__ == "__main__":
    main()
