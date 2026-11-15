from anvil import *

from ._anvil_designer import SheetHeroTemplate
from ... import state


class SheetHero(SheetHeroTemplate):
    """The landing hero: a spreadsheet DCF whose answer cell stays hidden until the visitor presses Reveal
    (the app's hide-and-reveal idea in one cell). Numbers match the DCF calculator's defaults: 49.95 per share."""

    def __init__(self, **properties):
        super().__init__(**properties)
        self._show(False)

    def _show(self, revealed):
        self.cover.visible = not revealed
        self.value_box.visible = revealed
        self.after_row.visible = revealed
        self.note.visible = revealed
        self.classes["is-revealed"] = revealed

    @handle("reveal_button", "click")
    def reveal_button_click(self, **event_args):
        self._show(True)
        state.live(self.value)
