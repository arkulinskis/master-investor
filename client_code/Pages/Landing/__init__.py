from anvil import *
import anvil.server

from ._anvil_designer import LandingTemplate
from ... import state


class Landing(LandingTemplate):
    """#landing, the front page: the spreadsheet hero (reveal the answer cell), how the loop works, the tracks as a
    ledger, three live sample cards, features, FAQ. Static copy is in the template; the counts come from the server."""

    def __init__(self, args=(), **properties):
        super().__init__(**properties)
        me = state.me()
        self.guest_cta.visible = not me
        self.member_cta.visible = bool(me)
        if me:
            state.set_attr(self.band_link, "href", "#home")
        d = anvil.server.call("get_learn")
        t = d["totals"]
        self.proof.text = "%d lessons · %d questions to test yourself · beginner to pro · free" % (t["lessons"], t["cards"])
        self.ledger_panel.items = d["tracks"]
        self.sum_lessons.text = str(t["lessons"])
        self.sum_cards.text = str(t["cards"])
        self.cards_panel.items = [dict(c, show_lesson=True) for c in d["samples"]]
