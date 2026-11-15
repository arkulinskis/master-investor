"""Page addresses: #name/arg1/arg2 -> a page Form (open_form), with sign-in rules.

Links in templates are plain <a href="#home">; code calls router.go("item", id).

    PAGES[name] = (who may open it, browser-tab title)   who: None = anyone, "guest" = signed out only, "user", "admin"
    NAV = the main menu (header + phone tab bar, signed-in people): (page, label, icon). At most 4.
New page: add it to PAGES, to _form() and (if it belongs in the menu) to NAV.
"""
import anvil
import anvil.js
from anvil.js import window

from . import state

PAGES = {
    "landing": (None, "Learn investing, from first fund to quant"),
    "auth": ("guest", "Sign in"),
    "home": ("user", "Today"),
    "learn": (None, "Learn"),
    "track": (None, "Track"),
    "lesson": (None, "Lesson"),
    "practice": (None, "Practice"),
    "tools": (None, "Calculators"),
    "library": (None, "Library"),
    "glossary": (None, "Glossary"),
    "profile": ("user", "Your profile"),
    "admin": ("admin", "Admin"),
}
# The header menu. Members also get "Today" (their dashboard) first. The phone tab bar shows the first 4 + You/Sign in.
NAV = [("learn", "Learn", "book"), ("practice", "Practice", "cards"), ("tools", "Calculators", "calc"), ("library", "Library", "database")]
MEMBER_NAV = [("home", "Today", "home")] + NAV
APP_NAME = "Master Investor"
_r: dict = {"after": "", "listening": False}


def _form(name):
    """The page's Form class (imported when first needed, so start-up stays quick)."""
    if name == "landing":
        from .Pages.Landing import Landing
        return Landing
    if name == "auth":
        from .Pages.Auth import Auth
        return Auth
    if name == "home":
        from .Pages.Home import Home
        return Home
    if name == "learn":
        from .Pages.Learn import Learn
        return Learn
    if name == "track":
        from .Pages.Track import Track
        return Track
    if name == "lesson":
        from .Pages.Lesson import Lesson
        return Lesson
    if name == "practice":
        from .Pages.Practice import Practice
        return Practice
    if name == "tools":
        from .Pages.Tools import Tools
        return Tools
    if name == "library":
        from .Pages.Library import Library
        return Library
    if name == "glossary":
        from .Pages.Glossary import Glossary
        return Glossary
    if name == "profile":
        from .Pages.Profile import Profile
        return Profile
    from .Pages.Admin import Admin
    return Admin


def nav():
    """The menu for whoever is here now."""
    return MEMBER_NAV if state.me() else NAV


def tabs():
    """The phone tab bar: four main pages (members: Today replaces Library, still in the header and footer)."""
    return MEMBER_NAV[:4] if state.me() else NAV


def parse(hash_text):
    h = (hash_text or "").lstrip("#").lstrip("!").lstrip("/").split("?")[0]
    parts = [window.decodeURIComponent(p) for p in h.split("/") if p]
    return (parts[0] if parts else ""), parts[1:]


def href(name, *args):
    """'#name/arg1/arg2' with every part URL-encoded (row ids contain brackets and commas)."""
    return "#" + "/".join([name] + [window.encodeURIComponent(str(a)) for a in args if a not in (None, "")])


def home_page():
    return "home" if state.me() else "landing"


def show():
    """Open the page for the current address."""
    name, args = parse(window.location.hash)
    if name not in PAGES:
        name, args = home_page(), []
    who = PAGES[name][0]
    if who == "guest" and state.me():
        name, args = "home", []
    elif who in ("user", "admin") and not state.me():
        _r["after"] = window.location.hash
        name, args = "auth", []
    elif who == "admin" and not state.is_admin():
        state.toast("That page is for admins only.", "error")
        name, args = "home", []
    window.document.title = PAGES[name][1] + " · " + APP_NAME
    window.UI_READY = False
    page = _form(name)(args=args)
    anvil.open_form(page)
    shell = getattr(page, "layout", None)
    if shell is not None and hasattr(shell, "refresh"):
        shell.refresh(name)  # Anvil reuses the layout between pages: tell it who is signed in and which page is open
    window.scrollTo(0, 0)
    window.UI_READY = True  # tests and screenshots wait for this


def go(name, *args):
    """Go to a page. Same address again = reload the page."""
    target = href(name, *args)
    if window.location.hash == target:
        show()
    else:
        window.location.hash = target


def replace(name, *args):
    """Change the address without opening anything (a page that switches its own view)."""
    window.history.replaceState(None, "", href(name, *args))


def after_sign_in():
    """Where to go once someone signs in: the page they were heading for, or home."""
    target = _r["after"]
    _r["after"] = ""
    if target and target != window.location.hash:
        window.location.hash = target
    else:
        go("home")


def remember_after(target):
    _r["after"] = target


def _on_hash(event):
    show()


def start():
    if not _r["listening"]:
        window.addEventListener("hashchange", anvil.js.report_exceptions(_on_hash))
        _r["listening"] = True
    show()
