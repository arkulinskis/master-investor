from anvil import *

from ._anvil_designer import TermRowTemplate
from ... import router, state


class TermRow(TermRowTemplate):
    """A glossary term: term, definition, and (glossary only) a link to the lesson it comes from."""

    def __init__(self, **properties):
        super().__init__(**properties)
        lesson = self.item.get("lesson")
        self.from_link.visible = bool(lesson)
        if lesson:
            state.set_attr(self.from_link, "href", router.href("lesson", lesson))
            self.from_label.text = "From: " + self.item.get("lesson_title", "")
