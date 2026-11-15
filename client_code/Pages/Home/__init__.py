from anvil import *
import anvil.server

from ._anvil_designer import HomeTemplate
from ... import router, state


class Home(HomeTemplate):
    """#home ("Today"), the member's dashboard: cards due, the next lesson, this week, track progress, saved lessons."""

    def __init__(self, args=(), **properties):
        super().__init__(**properties)
        state.heading(self.hello, 1)
        me = state.me() or {}
        first = (me.get("name") or "there").split(" ")[0]
        d = anvil.server.call("get_home")
        s = d["stats"]
        self.hello.text = "Hello, %s" % first
        self.sub.text = "%d of %d lessons done · %d of %d cards seen" % (s["lessons_done"], s["lessons"], s["cards_seen"], s["cards"])
        n = min(20, d["due"] + d["fresh"])
        self.due_num.text = str(n)
        if n:
            self.due_text.text = "cards ready: %d due for review, %d new from finished lessons." % (d["due"], d["fresh"])
        elif s["cards_seen"]:
            self.due_text.text = "cards due. You're up to date: come back tomorrow, or try a mixed deck."
            self.due_button.text = "Try a mixed deck"
        else:
            self.due_text.text = "cards yet. Finish a lesson (or try the placement check) to start your deck."
            self.due_button.text = "Take the placement check"
        self._due = n
        self._fresh_user = not s["cards_seen"]
        nxt = d["next"]
        self.next_box.visible = bool(nxt)
        self.all_done_box.visible = not nxt
        if nxt:
            self._next = nxt["id"]
            self.next_k.text = "Your first lesson" if not s["lessons_done"] else "Next lesson"
            self.next_title.text = nxt["title"]
            self.next_meta.text = "%s · %s · %d min" % (nxt["track_title"], nxt["level"], nxt["minutes"])
        top = max([w["cards"] + 3 * w["lessons"] for w in d["week"]] + [1])
        self.week_panel.items = [dict(w, h=int(100.0 * (w["cards"] + 3 * w["lessons"]) / top)) for w in d["week"]]
        self.streak.text = ("%s streak" % state.plural(d["streak"], "day")) if d["streak"] else "Start a streak today"
        self.s_lessons.text = str(s["lessons_done"])
        self.s_seen.text = str(s["cards_seen"])
        self.s_mastered.text = str(s["mastered"])
        self.tracks_panel.items = d["tracks"]
        self.saved_panel.items = [dict(L, show_track=True) for L in d["saved"]]
        self.no_saved.visible = not d["saved"]

    @handle("due_button", "click")
    def due_button_click(self, **event_args):
        if self._due:
            router.go("practice", "due")
        elif self._fresh_user:
            router.go("practice", "placement")
        else:
            router.go("practice", "mixed")

    @handle("next_button", "click")
    def next_button_click(self, **event_args):
        router.go("lesson", self._next)
