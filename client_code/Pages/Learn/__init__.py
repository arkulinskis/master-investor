from anvil import *
import anvil.server

from ._anvil_designer import LearnTemplate
from ... import router, state

LEVELS = ["all", "Beginner", "Intermediate", "Advanced", "Pro"]


class Learn(LearnTemplate):
    """#learn (and #learn/search/<words>): the nine tracks as cards, a level filter, lesson search, and for members
    the lesson to continue with. Open to everyone."""

    def __init__(self, args=(), **properties):
        super().__init__(**properties)
        state.heading(self.title, 1)
        state.set_control_attr(self.search_button, "aria-label", "Search")
        self._level = "all"
        self._buttons = dict(zip(LEVELS, [self.lv_all, self.lv_beginner, self.lv_intermediate, self.lv_advanced, self.lv_pro]))
        for lv, b in self._buttons.items():
            b.tag.level = lv
            b.add_event_handler("click", self._level_click)
        d = anvil.server.call("get_learn")
        self._tracks = d["tracks"]
        t = d["totals"]
        self.totals.text = "%d tracks · %d lessons · %d hide-and-reveal cards · %d key terms" % (
            t["tracks"], t["lessons"], t["cards"], t["terms"])
        if state.me():
            self.totals.text += " · you've finished %d" % t["done"]
        nxt = d.get("next")
        self.next_box.visible = bool(nxt)
        if nxt:
            self._next = nxt["id"]
            self.next_title.text = "%s: %s" % (nxt["track_title"], nxt["title"])
            if t["done"] == 0:
                self.next_kicker.text = "Your first lesson"
                self.next_button.text = "Start"
        self._draw_tracks()
        if len(args) >= 2 and args[0] == "search":
            self.search_box.text = args[1]
            self._search(args[1])
        else:
            self._show_search(False)

    def _draw_tracks(self):
        self.tracks_panel.items = [t for t in self._tracks if self._level == "all" or t["level"] == self._level]
        for lv, b in self._buttons.items():
            b.role = ["seg", "on"] if lv == self._level else ["seg"]
            state.set_control_attr(b, "aria-pressed", "true" if lv == self._level else "false")

    def _level_click(self, sender, **event_args):
        self._level = sender.tag.level
        self._draw_tracks()

    def _show_search(self, on):
        self.search_part.visible = on
        self.browse_part.visible = not on

    def _search(self, text):
        words = (text or "").strip()
        if not words:
            self._show_search(False)
            router.replace("learn")
            return
        d = anvil.server.call("search_lessons", words)
        rows = [dict(r, show_track=True) for r in d["results"]]
        self.results_panel.items = rows
        self.no_results.visible = not rows
        self.results_label.text = "%s for \u201c%s\u201d" % (state.plural(len(rows), "lesson"), words)
        self._show_search(True)
        router.replace("learn", "search", words)

    @handle("search_box", "pressed_enter")
    def search_box_pressed_enter(self, **event_args):
        self._search(self.search_box.text)

    @handle("search_button", "click")
    def search_button_click(self, **event_args):
        self._search(self.search_box.text)

    @handle("clear_button", "click")
    def clear_button_click(self, **event_args):
        self.search_box.text = ""
        self._search("")

    @handle("next_button", "click")
    def next_button_click(self, **event_args):
        router.go("lesson", self._next)
