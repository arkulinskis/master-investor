"""Public lesson pages for search engines, AI assistants and shared links: /lessons (every track) and /lessons/<id>.

Plain HTML rendered on the server from the same curriculum the app uses (Curriculum.index + unwrap), so crawlers that
don't run JavaScript can read every lesson. Cards are <details> reveals (they work without JavaScript); each page links
back to the app (/#lesson/<id>) to practise the cards on the spaced-repetition schedule. Unknown lesson -> 404.
@anvil.server.route serves at the root of the domain (see seo_routes.py); the sitemap lists these paths
(sitemap_extra in APP_MAKER/seo/apps/masterinvestor.json).
"""
import html
import json
import re

import anvil
import anvil.server

from . import Curriculum
from . import seo_routes

NOT_ADVICE = "Education only, not financial advice. Examples use made-up companies and numbers."
FONTS = ("https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500"
         "&family=Newsreader:opsz,wght@6..72,500;6..72,600&display=swap")

CSS = """
:root{--bg:#fff;--surface:#fff;--surface2:#f2f6f3;--ink:#0f1f17;--muted:#4a5c52;--line:#d6dfd9;--grid:#e6ece8;--brand:#0b7a3e;
--brand-ink:#fff;--brand-soft:#e2f2e7;--accent:#ffe27a;--accent-ink:#5c4300;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--bg:#0c1510;--surface:#111d16;--surface2:#18271f;--ink:#e7f1eb;--muted:#a9bcb0;
--line:#263a2e;--grid:#1c2c23;--brand:#45c27e;--brand-ink:#03140a;--brand-soft:#143222;--accent:#e8c547;--accent-ink:#261c00;color-scheme:dark}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.65 "Hanken Grotesk",system-ui,-apple-system,"Segoe UI",sans-serif;
-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}
a{color:var(--brand);text-underline-offset:3px}a:focus-visible,summary:focus-visible{outline:2px solid var(--brand);outline-offset:3px;border-radius:4px}
.top{border-bottom:1px solid var(--line);background:var(--surface)}
.top .in{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:58px}
.brand{display:flex;align-items:center;gap:10px;font:600 1.15rem/1 "Newsreader",Georgia,serif;color:var(--ink);text-decoration:none}
.brand img{width:30px;height:30px;border-radius:7px}
.in{max-width:820px;margin:0 auto;padding:0 16px}
main .in{padding-top:28px;padding-bottom:48px}
.crumbs{font-size:.9rem;color:var(--muted);margin:0 0 14px}.crumbs a{color:var(--muted)}
h1,h2,h3{font-family:"Newsreader",Georgia,serif;font-weight:600;line-height:1.15;text-wrap:balance}
h1{font-size:clamp(2rem,6vw,2.75rem);letter-spacing:-.015em;margin:0 0 10px}
h2{font-size:1.55rem;margin:40px 0 12px}h3{font-size:1.25rem;margin:28px 0 8px}
.lead{font-size:1.2rem;color:var(--muted);margin:0 0 12px;text-wrap:pretty}
.meta{font:500 .85rem/1.4 "IBM Plex Mono",ui-monospace,monospace;color:var(--muted);margin:0 0 26px}
.body p,.body li{text-wrap:pretty}.body ul,.body ol{padding-left:24px}.body li{margin:6px 0}
code{font:500 .92em "IBM Plex Mono",ui-monospace,monospace;background:var(--surface2);border:1px solid var(--grid);border-radius:4px;padding:1px 5px}
blockquote{margin:18px 0;padding:10px 16px;border-left:4px solid var(--accent);background:var(--surface2);border-radius:0 6px 6px 0}
blockquote p{margin:0}
.ex{border:1px solid var(--line);border-radius:8px;padding:4px 20px 12px;margin:32px 0;background:var(--surface)}
.ex h2{margin-top:18px}
dl{display:grid;gap:12px;margin:0}dt{font-weight:700}dd{margin:2px 0 0;color:var(--muted)}
details{border:1px solid var(--line);border-radius:8px;margin:10px 0;background:var(--surface)}
summary{cursor:pointer;padding:14px 16px;font-weight:600;list-style:none;display:flex;gap:12px;align-items:baseline}
summary::-webkit-details-marker{display:none}
summary .n{font:500 .8rem/1 "IBM Plex Mono",ui-monospace,monospace;color:var(--muted);min-width:2.2em}
summary .r{margin-left:auto;font:600 .8rem/1 "Hanken Grotesk",sans-serif;color:var(--brand);white-space:nowrap}
details[open] summary .r{color:var(--muted)}
details .a{padding:0 16px 14px 50px;margin:0;border-top:1px solid var(--grid);padding-top:12px}
.cta{display:inline-block;background:var(--brand);color:var(--brand-ink);padding:12px 20px;border-radius:8px;font-weight:700;text-decoration:none;margin:18px 0 6px}
.cta:hover{filter:brightness(1.06)}
.pager{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;border-top:1px solid var(--line);margin-top:40px;padding-top:18px}
.links li{margin:6px 0}
.note{font-size:.9rem;color:var(--muted)}
.track{border-top:1px solid var(--line);padding-top:6px;margin-top:30px}
.track ol{padding-left:0;list-style:none;margin:0}
.track li{display:grid;grid-template-columns:2.6em minmax(0,1fr);gap:4px 10px;padding:12px 0;border-bottom:1px solid var(--grid)}
.track li .n{font:500 .85rem/1.6 "IBM Plex Mono",ui-monospace,monospace;color:var(--muted)}
.track li a{font-weight:700}.track li p{margin:2px 0 0;color:var(--muted);font-size:.95rem}
footer{border-top:1px solid var(--line);color:var(--muted);font-size:.9rem}footer .in{padding-top:18px;padding-bottom:28px}
@media (max-width:520px){details .a{padding-left:16px}summary .r{display:none}}
"""


def _esc(s):
    return html.escape(s or "", quote=True)


def _inline(s):
    """Escape, then the inline markdown the curriculum uses: `code`, **bold**, *italic*."""
    codes: list = []

    def keep(m):
        codes.append("<code>%s</code>" % m.group(1))
        return "\x00%d\x00" % (len(codes) - 1)

    t = re.sub(r"`([^`]+)`", keep, _esc(s))
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], t)


def md(text):
    """The markdown subset tools/content_check.py allows (### headings, paragraphs, - and 1. lists, > quotes,
    **bold**, *italic*, `code`) as escaped HTML. Hard-wrapped lines are joined first (Curriculum.unwrap)."""
    out: list = []
    para: list = []
    lst = None  # "ul" | "ol" while inside a list

    def flush_para():
        if para:
            out.append("<p>%s</p>" % _inline(" ".join(para)))
            del para[:]

    def close_list():
        nonlocal lst
        if lst:
            out.append("</%s>" % lst)
            lst = None

    for raw in Curriculum.unwrap(text).splitlines():
        s = raw.strip()
        if not s:
            flush_para()
            close_list()
            continue
        m_ol = re.match(r"^(\d+)\.\s+(.*)$", s)
        if s.startswith("#"):
            flush_para()
            close_list()
            out.append("<h3>%s</h3>" % _inline(s.lstrip("#").strip()))
        elif s.startswith(("- ", "* ")) or m_ol:
            flush_para()
            kind = "ol" if m_ol else "ul"
            if lst != kind:
                close_list()
                out.append("<%s>" % kind)
                lst = kind
            out.append("<li>%s</li>" % _inline(m_ol.group(2) if m_ol else s[2:]))
        elif s.startswith(">"):
            flush_para()
            close_list()
            out.append("<blockquote><p>%s</p></blockquote>" % _inline(s.lstrip(">").strip()))
        else:
            close_list()
            para.append(s)
    flush_para()
    close_list()
    return "\n".join(out)


def _ld(data):
    return json.dumps(data, ensure_ascii=False).replace("</", "<\\/")


def _page(o, title, desc, path, ld, body):
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<link rel="canonical" href="%(url)s">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta property="og:type" content="article"><meta property="og:site_name" content="Master Investor">
<meta property="og:title" content="%(title)s"><meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(url)s"><meta property="og:image" content="%(o)s/_/theme/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b7a3e">
<link rel="icon" href="%(o)s/_/theme/icon-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="%(fonts)s" rel="stylesheet">
<script type="application/ld+json">%(ld)s</script>
<style>%(css)s</style></head>
<body>
<header class="top"><div class="in"><a class="brand" href="%(o)s/"><img src="%(o)s/_/theme/icon-180.png" alt="" width="30" height="30">Master Investor</a>
<a href="%(o)s/lessons">All lessons</a></div></header>
<main><div class="in">
%(body)s
</div></main>
<footer><div class="in"><p>%(not_advice)s Past returns don't predict future ones.</p>
<p>Master Investor is a free investing course made by <a href="https://arkvital.com">Arkvital</a> in Montreal, Canada.
<a href="%(o)s/">Open the app</a> &middot; <a href="%(o)s/about">About</a> &middot; Contact developer: <a href="https://arkvital.com">arkvital.com</a> &middot; Parent company: <a href="https://addanapp.com">addanapp.com</a></p></div></footer>
</body></html>
""" % {"title": _esc(title), "desc": _esc(desc), "url": _esc(o + path), "o": _esc(o), "fonts": _esc(FONTS), "ld": ld,
       "css": CSS, "body": body, "not_advice": _esc(NOT_ADVICE)}


def _org(o):
    return {"@type": "Organization", "@id": "https://arkvital.com/#org", "name": "Arkvital", "url": "https://arkvital.com"}


def lesson_html(o, lesson_id):
    """The page for one lesson, or None if there is no such lesson."""
    ix = Curriculum.index()
    L = ix["lessons"].get(lesson_id)
    if L is None:
        return None
    order = ix["order"]
    i = order.index(L["id"])
    prev_L = ix["lessons"][order[i - 1]] if i > 0 else None
    next_L = ix["lessons"][order[i + 1]] if i + 1 < len(order) else None
    path = "/lessons/" + L["id"]
    title = "%s: a free lesson | Master Investor" % L["title"]
    app_link = "%s/#lesson/%s" % (o, L["id"])
    cards = "\n".join(
        '<details><summary><span class="n">Q%d</span><span>%s</span><span class="r">Reveal</span></summary>'
        '<p class="a">%s</p></details>' % (k + 1, _esc(q), _esc(a)) for k, (q, a) in enumerate(L["cards"]))
    terms = "".join("<div><dt>%s</dt><dd>%s</dd></div>" % (_esc(a), _esc(b)) for a, b in L["terms"])
    ex = L["example"]
    ex_html = ('<section class="ex" aria-labelledby="ex-h"><h2 id="ex-h">%s</h2><div class="body">%s</div></section>'
               % (_esc(ex["title"]), md(ex["body"]))) if ex else ""
    links = ("<h2>Go further</h2><ul class=\"links\">%s</ul>" % "".join(
        '<li><a href="%s" rel="noopener">%s</a></li>' % (_esc(u), _esc(lab)) for lab, u in L["links"])) if L["links"] else ""
    pager = '<nav class="pager" aria-label="Lessons">%s%s</nav>' % (
        ('<a href="%s/lessons/%s">&larr; %s</a>' % (_esc(o), _esc(prev_L["id"]), _esc(prev_L["title"]))) if prev_L else "<span></span>",
        ('<a href="%s/lessons/%s">%s &rarr;</a>' % (_esc(o), _esc(next_L["id"]), _esc(next_L["title"]))) if next_L else "")
    t = ix["by_track"][L["track"]]
    body = """<nav class="crumbs" aria-label="Breadcrumb"><a href="%(o)s/lessons">Lessons</a> / <a href="%(o)s/lessons#%(track)s">%(track_title)s</a></nav>
<article>
<h1>%(title)s</h1>
<p class="lead">%(summary)s</p>
<p class="meta">%(level)s &middot; lesson %(pos)d of %(of)d in %(track_title)s &middot; %(minutes)d min read &middot; %(n)d cards</p>
<div class="body">%(body)s</div>
%(example)s
<h2>Key terms</h2>
<dl>%(terms)s</dl>
<h2>Check yourself</h2>
<p class="note">Answer each question in your head, then open it to see the answer.</p>
%(cards)s
<a class="cta" href="%(app)s">Practise these cards in the app</a>
<p class="note">Free, no account needed. With an account the app brings each card back on a spaced-repetition schedule.</p>
%(links)s
</article>
%(pager)s""" % {"o": _esc(o), "track": _esc(L["track"]), "track_title": _esc(L["track_title"]), "title": _esc(L["title"]),
                "summary": _esc(L["summary"]), "level": _esc(L["level"]), "pos": L["pos"], "of": len(t["lessons"]),
                "minutes": int(L["minutes"]), "n": len(L["cards"]), "body": md(L["body"]), "example": ex_html,
                "terms": terms, "cards": cards, "app": _esc(app_link), "links": links, "pager": pager}
    ld = _ld({"@context": "https://schema.org", "@graph": [
        {"@type": "LearningResource", "@id": o + path + "#lesson", "name": L["title"], "description": L["summary"],
         "url": o + path, "learningResourceType": "Lesson", "educationalLevel": L["level"], "inLanguage": "en",
         "timeRequired": "PT%dM" % int(L["minutes"]), "isAccessibleForFree": True,
         "teaches": [a for a, b in L["terms"]], "keywords": ", ".join(a for a, b in L["terms"]),
         "isPartOf": {"@type": "Course", "name": "Master Investor: " + L["track_title"], "url": o + "/lessons#" + L["track"],
                      "provider": {"@id": "https://arkvital.com/#org"}},
         "publisher": {"@id": "https://arkvital.com/#org"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Lessons", "item": o + "/lessons"},
            {"@type": "ListItem", "position": 2, "name": L["track_title"], "item": o + "/lessons#" + L["track"]},
            {"@type": "ListItem", "position": 3, "name": L["title"], "item": o + path}]},
        _org(o)]})
    return _page(o, title, L["summary"], path, ld, body)


def index_html(o):
    ix = Curriculum.index()
    parts = ['<h1>Every lesson, from first fund to quant</h1>',
             '<p class="lead">%d free lessons in %d tracks. Each one ends with question cards whose answers stay hidden '
             'until you open them.</p>' % (len(ix["lessons"]), len(ix["tracks"])),
             '<p><a class="cta" href="%s/#learn">Learn in the app</a></p>' % _esc(o)]
    items = []
    for t in ix["tracks"]:
        rows = []
        for lid in t["lessons"]:
            L = ix["lessons"][lid]
            rows.append('<li><span class="n">%d.%d</span><div><a href="%s/lessons/%s">%s</a><p>%s &middot; %d min. %s</p></div></li>'
                        % (t["n"], L["pos"], _esc(o), _esc(lid), _esc(L["title"]), _esc(L["level"]), int(L["minutes"]),
                           _esc(L["summary"])))
            items.append({"@type": "ListItem", "position": len(items) + 1, "url": "%s/lessons/%s" % (o, lid), "name": L["title"]})
        parts.append('<section class="track" id="%s"><h2>%d. %s</h2><p class="note">%s</p><ol>%s</ol></section>'
                     % (_esc(t["id"]), t["n"], _esc(t["title"]), _esc(t["blurb"]), "".join(rows)))
    ld = _ld({"@context": "https://schema.org", "@graph": [
        {"@type": "CollectionPage", "@id": o + "/lessons#page", "url": o + "/lessons", "name": "Master Investor lessons",
         "description": "Every free Master Investor lesson, from a first index fund to quantitative investing.",
         "isPartOf": {"@id": o + "/#site"}, "mainEntity": {"@type": "ItemList", "numberOfItems": len(items),
                                                            "itemListElement": items}},
        _org(o)]})
    return _page(o, "All lessons: learn investing free, from first fund to quant | Master Investor",
                 "Every Master Investor lesson in one place: %d free lessons on investing, from compounding and fees to "
                 "valuing a company, risk, trading and quant methods." % len(ix["lessons"]), "/lessons", ld, "\n".join(parts))


def not_found_html(o):
    body = ('<h1>That lesson isn\'t here</h1><p class="lead">It may have moved.</p>'
            '<p><a class="cta" href="%s/lessons">See every lesson</a></p>' % _esc(o))
    return _page(o, "Lesson not found | Master Investor", "That lesson isn't here.", "/lessons", "{}", body)


def _respond(status, text):
    return anvil.server.HttpResponse(status, anvil.BlobMedia("text/html; charset=utf-8", text.encode("utf-8")),
                                     headers={"Cache-Control": "public, max-age=3600"})


ROUTE = getattr(anvil.server, "route", None)
if ROUTE:  # hosted Anvil (Python 3.10+ runtimes); see seo_routes.py
    @ROUTE("/lessons")
    def lessons_index(**params):
        return _respond(200, index_html(seo_routes.origin()))

    @ROUTE("/lessons/:lesson_id")
    def lesson_page(lesson_id="", **params):
        o = seo_routes.origin()
        page = lesson_html(o, str(lesson_id or "")[:80])
        return _respond(200, page) if page else _respond(404, not_found_html(o))
