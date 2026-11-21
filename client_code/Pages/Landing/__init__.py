from anvil import *
import anvil.server

from ._anvil_designer import LandingTemplate
from ... import state


# The app's video on the Addanapp YouTube channel (APP_MAKER/youtube/manifest.json), shown in the Watch section.
YT_VIDEO = "Yr5bnP8S8KQ"


class Landing(LandingTemplate):
    """#landing, the front page: the spreadsheet hero (reveal the answer cell), how the loop works, the tracks as a
    ledger, three live sample cards, features, FAQ. Static copy is in the template; the counts come from the server."""

    def __init__(self, args=(), **properties):
        super().__init__(**properties)
        self.dom_nodes["yt_cover"].addEventListener("click", self._play)
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

    def _play(self, event):
        """Swap the video's cover for YouTube's player (privacy-enhanced); nothing loads from YouTube before this click."""
        self.dom_nodes["yt_frame"].innerHTML = (
            '<iframe src="https://www.youtube-nocookie.com/embed/' + YT_VIDEO + '?autoplay=1&rel=0&playsinline=1" '
            'title="Master Investor video" allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen '
            'referrerpolicy="strict-origin-when-cross-origin"></iframe>')
