from anvil import *

from ._anvil_designer import LessonRowTemplate
from ... import router, state

LEVEL_ROLE = {"Beginner": "badge-good", "Intermediate": "badge-brand", "Advanced": "badge-warn", "Pro": "badge-bad"}


class LessonRow(LessonRowTemplate):
    """One lesson as a sheet row. item = a lesson row dict (title, summary, level, minutes, pos, track_title, done);
    item["show_track"] shows the track name (search results), else the lesson's number in its track."""

    def __init__(self, **properties):
        super().__init__(**properties)
        L = self.item
        state.set_attr(self, "href", router.href("lesson", L["id"]))
        self.num.text = str(L["pos"])
        self.level.role = ["badge", LEVEL_ROLE.get(L["level"], "badge-brand")]
        bits = ["%d min" % L["minutes"], state.plural(L["cards"], "card")]
        if L.get("show_track"):
            bits.insert(0, L["track_title"])
        self.meta.text = " · ".join(bits)
        self.done_mark.visible = bool(L.get("done"))
        self.classes["is-done"] = bool(L.get("done"))
