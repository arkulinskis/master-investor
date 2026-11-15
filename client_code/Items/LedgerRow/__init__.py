from anvil import *

from ._anvil_designer import LedgerRowTemplate
from ... import router, state


class LedgerRow(LedgerRowTemplate):
    """Landing: one track as a spreadsheet row (row number, track, level, lessons, cards)."""

    def __init__(self, **properties):
        super().__init__(**properties)
        t = self.item
        state.set_attr(self, "href", router.href("track", t["id"]))
        self.num.text = str(t["n"] + 1)
        self.lessons.text = str(t["lessons"])
        self.cards.text = str(t["cards"])
