from anvil import *
import anvil.js
import anvil.server
from anvil.js import window

from ._anvil_designer import PracticeTemplate
from ... import router, state

LEVELS = ["Beginner", "Intermediate", "Advanced", "Pro"]
COLS = "ABCDEFGH"


class Practice(PracticeTemplate):
    """#practice: choose a deck; #practice/<mode>/<arg> starts one straight away (due, mixed, placement, saved,
    level/<Level>, track/<id>, lesson/<id>). A session shows one card, Reveal, then Got it / Not yet (keys Space, 1, 2).
    "Not yet" cards come back once at the end of the session; the score counts first tries only.
    Members' grades are saved (spaced repetition, Study.review_card); guests just see their score."""

    def __init__(self, args=(), **properties):
        super().__init__(**properties)
        state.heading(self.title, 1)
        self._keys = anvil.js.report_exceptions(self._key)
        self._listening = False
        self._deck: list = []
        self._i, self._revealed, self._first = 0, False, {}
        self._mode, self._arg = "", ""
        for b, lv in zip([self.lv_beginner, self.lv_intermediate, self.lv_advanced, self.lv_pro], LEVELS):
            b.tag.level = lv
            b.add_event_handler("click", self._level_click)
        self.place_box.visible = False
        if args:
            self._start(args[0], args[1] if len(args) > 1 else "")
        else:
            self._menu()

    # ---------------------------------------------------------------- the menu
    def _menu(self):
        self._view("menu")
        d = anvil.server.call("get_practice")
        counts = {x["level"]: x["count"] for x in d["levels"]}
        for b, lv in zip([self.lv_beginner, self.lv_intermediate, self.lv_advanced, self.lv_pro], LEVELS):
            b.text = "%s (%d cards)" % (lv, counts.get(lv, 0))
        self.track_drop.items = [("%s (%d cards)" % (t["title"], t["cards"]), t["id"]) for t in d["tracks"]]
        state.set_control_attr(self.track_drop, "aria-label", "Track")
        signed = d["signed_in"]
        self.guest_box.visible = not signed
        self.due_box.visible = signed
        self.saved_button.visible = signed and d["saved"] > 0
        if signed:
            n = d["due"] + d["fresh"]
            if n:
                self.due_title.text = "%s waiting for you" % state.plural(min(n, 20), "card")
                self.due_sub.text = "%d due for review, %d new from lessons you've finished. %d mastered so far." % (
                    d["due"], d["fresh"], d["mastered"])
                self.due_button.enabled = True
            else:
                self.due_title.text = "Nothing due right now"
                self.due_sub.text = "Finish a lesson to add its cards, or try a deck below. %d mastered so far." % d["mastered"]
                self.due_button.enabled = False

    def _view(self, which):
        self.menu_part.visible = which == "menu"
        self.session_part.visible = which == "session"
        self.done_part.visible = which == "done"
        if which == "session" and not self._listening:
            window.document.addEventListener("keydown", self._keys)
            self._listening = True
        elif which != "session" and self._listening:
            window.document.removeEventListener("keydown", self._keys)
            self._listening = False

    # ---------------------------------------------------------------- starting a deck
    def _start(self, mode, arg=""):
        r = anvil.server.call("get_deck", mode, arg)
        if not r.get("ok"):
            state.toast(r.get("error") or "That deck isn't available.", "error")
            router.replace("practice")
            self._menu()
            return
        if not r["cards"]:
            state.toast("No cards in that deck yet.", "error")
            self._menu()
            return
        self._mode, self._arg, self._title = r["mode"], r["arg"], r["title"]
        router.replace("practice", mode, arg) if arg else router.replace("practice", mode)
        self._run(r["cards"])

    def _run(self, cards):
        self._deck = [dict(c) for c in cards]
        self._total = len(self._deck)
        self._i, self._first, self._requeued = 0, {}, set()
        self.deck_title.text = self._title
        self._view("session")
        self._show_card()

    def _show_card(self):
        c = self._deck[self._i]
        self._revealed = False
        n_done = len(self._first)
        self.progress_label.text = "Card %d of %d" % (min(n_done + 1, self._total), self._total) if c["id"] not in self._first \
            else "Second look"
        self.fill.style["width"] = "%d%%" % int(100.0 * n_done / max(1, self._total))
        self.cell_ref.text = "%s%d" % (COLS[self._i % len(COLS)], self._i + 1)
        self.card_meta.text = "%s · %s" % (c["track_title"], c["level"])
        self.question.text = c["q"]
        self.answer.text = c["a"]
        self.from_label.text = "From the lesson: " + c["lesson_title"]
        state.set_attr(self.from_link, "href", router.href("lesson", c["lesson"]))
        self.answer_box.visible = False
        self.grade.visible = False
        self.reveal_button.visible = True
        self.card.classes["is-open"] = False
        state.focus(self.reveal_button)

    def _reveal(self):
        if self._revealed:
            return
        self._revealed = True
        self.answer_box.visible = True
        self.reveal_button.visible = False
        self.grade.visible = True
        self.card.classes["is-open"] = True
        state.live(self.answer)
        state.focus(self.yes_button)

    def _grade(self, knew):
        if not self._revealed:
            return
        c = self._deck[self._i]
        if c["id"] not in self._first:
            self._first[c["id"]] = knew
        if state.me():
            state.call_quiet("review_card", c["id"], knew)
        if not knew and c["id"] not in self._requeued:
            self._requeued.add(c["id"])
            self._deck.append(c)
        self._i += 1
        if self._i >= len(self._deck):
            self._finish()
        else:
            self._show_card()

    # ---------------------------------------------------------------- the end
    def _finish(self):
        self._view("done")
        right = len([k for k in self._first.values() if k])
        n = len(self._first)
        self.result_title.text = self._title + ": done"
        self.result_score.text = "%d / %d" % (right, n)
        pct = int(round(100.0 * right / max(1, n)))
        if pct >= 90:
            words = "Excellent. These are sticking."
        elif pct >= 70:
            words = "Good work. A few more passes and they'll stick."
        elif pct >= 40:
            words = "A solid start. Re-read the lessons behind the misses, then go again."
        else:
            words = "This deck is new ground. Read the lessons first, then the cards will make sense."
        if state.me():
            words += " Your answers are saved and each card is scheduled."
        else:
            words += " Sign up to have each card scheduled for you."
        self.result_text.text = words
        missed = [c for c in self._deck if self._first.get(c["id"]) is False]
        uniq, seen = [], set()
        for c in missed:
            if c["id"] not in seen:
                seen.add(c["id"])
                uniq.append(dict(c, open=True, no_grade=True, show_lesson=True))
        self._missed = uniq
        self.missed_box.visible = bool(uniq)
        self.missed_panel.items = uniq
        self.again_button.visible = bool(uniq)
        self.place_box.visible = False
        if self._mode == "placement":
            by_level: dict = {}
            for c in self._deck:
                if self._first.get(c["id"]):
                    by_level[c["level"]] = by_level.get(c["level"], 0) + 1
            a = anvil.server.call("placement_advice", by_level)
            if a.get("ok"):
                self.place_box.visible = True
                self.place_level.text = "Your level: " + a["level"]
                self.place_text.text = a["text"]
                self.place_button.text = "Start with " + a["track"]["title"]
                self._place_track = a["track"]["id"]

    # ---------------------------------------------------------------- buttons and keys
    @handle("due_button", "click")
    def due_button_click(self, **event_args):
        self._start("due")

    @handle("mixed_button", "click")
    def mixed_button_click(self, **event_args):
        self._start("mixed")

    @handle("placement_button", "click")
    def placement_button_click(self, **event_args):
        self._start("placement")

    @handle("saved_button", "click")
    def saved_button_click(self, **event_args):
        self._start("saved")

    def _level_click(self, sender, **event_args):
        self._start("level", sender.tag.level)

    @handle("track_button", "click")
    def track_button_click(self, **event_args):
        if self.track_drop.selected_value:
            self._start("track", self.track_drop.selected_value)

    @handle("reveal_button", "click")
    def reveal_button_click(self, **event_args):
        self._reveal()

    @handle("yes_button", "click")
    def yes_button_click(self, **event_args):
        self._grade(True)

    @handle("no_button", "click")
    def no_button_click(self, **event_args):
        self._grade(False)

    @handle("end_button", "click")
    def end_button_click(self, **event_args):
        if self._first:
            self._finish()
        else:
            router.replace("practice")
            self._menu()

    @handle("again_button", "click")
    def again_button_click(self, **event_args):
        self._title = "Second round"
        self._mode = "again"
        self._run([{k: v for k, v in c.items() if k not in ("open", "no_grade", "show_lesson")} for c in self._missed])

    @handle("menu_button", "click")
    def menu_button_click(self, **event_args):
        router.replace("practice")
        self._menu()

    @handle("place_button", "click")
    def place_button_click(self, **event_args):
        router.go("track", self._place_track)

    def _key(self, event):
        tag = str(getattr(event.target, "tagName", "") or "").upper()
        if tag in ("INPUT", "TEXTAREA", "SELECT") or getattr(event, "ctrlKey", False) or getattr(event, "metaKey", False):
            return
        key = getattr(event, "key", None)
        if key == " " and not self._revealed:
            event.preventDefault()
            self._reveal()
        elif key in ("1", "2") and self._revealed:
            event.preventDefault()
            self._grade(key == "2")

    @handle("", "hide")
    def form_hide(self, **event_args):
        if self._listening:
            window.document.removeEventListener("keydown", self._keys)
            self._listening = False
