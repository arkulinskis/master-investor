from anvil import *
import anvil.server
from anvil.js import window

from ._anvil_designer import TrackTemplate
from ... import router, state


class Track(TrackTemplate):
    """#track/<id>: one track's lessons as a sheet, with Start / Continue and Practise this track."""

    def __init__(self, args=(), **properties):
        super().__init__(**properties)
        state.heading(self.title, 1)
        r = anvil.server.call("get_track", args[0] if args else "")
        self.found.visible = bool(r.get("ok"))
        self.missing.visible = not r.get("ok")
        if not r.get("ok"):
            self.crumb.text = "Not found"
            return
        t = r["track"]
        self._id, self._next = t["id"], r["next_id"]
        window.document.title = t["title"] + " · Master Investor"
        self.crumb.text = t["title"]
        self.icon.classes.add("ic-" + t["icon"])
        self.title.text = t["title"]
        self.blurb.text = t["blurb"]
        self.meta.text = "Track %d of 9 · %s · %s · about %d minutes · %s" % (
            t["n"], t["level"], state.plural(t["lessons"], "lesson"), t["minutes"], state.plural(t["cards"], "card"))
        self.lessons_panel.items = r["lessons"]
        me = state.me()
        self.progress_box.visible = bool(me)
        self.fill.style["width"] = "%d%%" % t["pct"]
        self.progress_label.text = "%d of %d done" % (t["done"], t["lessons"])
        if me and t["done"]:
            self.start_button.text = "Continue" if self._next else "Read it again"
        if not self._next:
            self._next = r["lessons"][0]["id"]
        for link, label, other, word in ((self.prev_link, self.prev_label, r["prev_track"], "Previous: "),
                                         (self.next_link, self.next_label, r["next_track"], "Next: ")):
            link.visible = bool(other)
            if other:
                state.set_attr(link, "href", router.href("track", other["id"]))
                label.text = word + other["title"]

    @handle("start_button", "click")
    def start_button_click(self, **event_args):
        router.go("lesson", self._next)

    @handle("practice_button", "click")
    def practice_button_click(self, **event_args):
        router.go("practice", "track", self._id)
