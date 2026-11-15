from anvil import *

from ._anvil_designer import DayBarTemplate
from ... import state

DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]


class DayBar(DayBarTemplate):
    """Home: one day of the last week. item = {day (ISO), cards, knew, lessons, today, h (0..100, set by the page)}."""

    def __init__(self, **properties):
        super().__init__(**properties)
        d = self.item
        y, m, dd = [int(x) for x in d["day"].split("-")]
        import datetime
        self.day.text = "Today" if d["today"] else DAYS[datetime.date(y, m, dd).weekday()]
        self.count.text = str(d["cards"]) if d["cards"] else ""
        self.fill.style["height"] = "%d%%" % max(d["h"], 4 if d["cards"] or d["lessons"] else 0)
        self.classes["is-today"] = bool(d["today"])
        state.set_attr(self, "aria-label", "%s: %s, %s" % (self.day.text, state.plural(d["cards"], "card"),
                                                          state.plural(d["lessons"], "lesson")))
        state.set_attr(self, "role", "img")
