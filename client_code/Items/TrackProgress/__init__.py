from anvil import *

from ._anvil_designer import TrackProgressTemplate
from ... import router, state


class TrackProgress(TrackProgressTemplate):
    """Home: one track's progress bar. item = {id, title, icon, done, lessons, pct}."""

    def __init__(self, **properties):
        super().__init__(**properties)
        t = self.item
        state.set_attr(self, "href", router.href("track", t["id"]))
        self.icon.classes.add("ic-" + t["icon"])
        self.count.text = "%d / %d" % (t["done"], t["lessons"])
        self.fill.style["width"] = "%d%%" % t["pct"]
        self.classes["is-full"] = t["pct"] >= 100
        state.set_attr(self.bar, "role", "img")
        state.set_attr(self.bar, "aria-label", "%d of %d lessons done" % (t["done"], t["lessons"]))
