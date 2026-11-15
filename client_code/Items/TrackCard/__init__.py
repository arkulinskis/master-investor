from anvil import *

from ._anvil_designer import TrackCardTemplate
from ... import router, state


class TrackCard(TrackCardTemplate):
    """A track on the Learn page. item = a track dict from get_learn (title, level, lessons, minutes, cards, done, pct)."""

    def __init__(self, **properties):
        super().__init__(**properties)
        t = self.item
        state.set_attr(self, "href", router.href("track", t["id"]))
        self.icon.classes.add("ic-" + t["icon"])
        self.num.text = "Track %d" % t["n"]
        meta = "%s · %d min · %s" % (state.plural(t["lessons"], "lesson"), t["minutes"], state.plural(t["cards"], "card"))
        if state.me():
            meta += " · %d of %d done" % (t["done"], t["lessons"])
        self.meta.text = meta
        self.bar.visible = bool(state.me())
        self.fill.style["width"] = "%d%%" % t["pct"]
        state.set_attr(self.bar, "role", "img")
        state.set_attr(self.bar, "aria-label", "%d%% done" % t["pct"])
