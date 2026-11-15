from anvil import *

from ._anvil_designer import RevealCardTemplate
from ... import state

BOX_WORDS = {1: "new to you", 2: "learning", 3: "getting there", 4: "nearly mastered", 5: "mastered"}


class RevealCard(RevealCardTemplate):
    """A hide-and-reveal self-test card: the question shows, the answer waits behind "Reveal answer".
    item = a card dict (id, q, a, level, lesson_title, box) plus optional:
      open      start revealed (the page's "Reveal all")
      no_grade  hide the Got it / Not yet buttons (review lists)
      show_lesson  show which lesson the card comes from
    Grading saves the review for members (spaced repetition) and raises x-graded(knew=...) on the RepeatingPanel."""

    def __init__(self, **properties):
        super().__init__(**properties)
        c = self.item
        bits = [c.get("level") or ""]
        if c.get("show_lesson"):
            bits.append(c.get("lesson_title") or "")
        if c.get("box"):
            bits.append(BOX_WORDS.get(int(c["box"]), ""))
        self.meta.text = " · ".join([b for b in bits if b])
        self._show(bool(c.get("open")))

    def _show(self, revealed):
        self.cover.visible = not revealed
        self.answer_box.visible = revealed
        self.grade.visible = revealed and not self.item.get("no_grade")
        self.classes["is-open"] = revealed

    @handle("reveal_button", "click")
    def reveal_button_click(self, **event_args):
        self._show(True)
        if not self.item.get("no_grade"):
            state.focus(self.got_it_button)

    @handle("got_it_button", "click")
    def got_it_button_click(self, **event_args):
        self._grade(True)

    @handle("not_yet_button", "click")
    def not_yet_button_click(self, **event_args):
        self._grade(False)

    def _grade(self, knew):
        self.grade.visible = False
        self.graded.visible = True
        self.graded.role = ["rv-graded", "is-good" if knew else "is-again"]
        words = "Nice. " if knew else "No problem: it comes back sooner. "
        if state.me():
            r = state.call_quiet("review_card", self.item["id"], knew)
            if r and r.get("ok"):
                words += "Saved (%s)." % BOX_WORDS.get(int(r["box"]), "")
            else:
                words += "Couldn't save just now."
        else:
            words += "Sign in to keep a review schedule."
        self.graded.text = words
        state.live(self.graded)
        if self.parent is not None:
            self.parent.raise_event("x-graded", knew=knew, card=self.item["id"])
