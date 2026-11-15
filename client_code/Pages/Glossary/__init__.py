from anvil import *
import anvil.server

from ._anvil_designer import GlossaryTemplate
from ... import state


class Glossary(GlossaryTemplate):
    """#glossary: every key term from every lesson, A to Z, filtered as you type."""

    def __init__(self, args=(), **properties):
        super().__init__(**properties)
        state.heading(self.title, 1)
        self._terms = anvil.server.call("get_glossary")["terms"]
        self._draw()

    def _draw(self):
        q = (self.search_box.text or "").strip().lower()
        rows = [t for t in self._terms if not q or q in t["term"].lower() or q in t["definition"].lower()]
        rows.sort(key=lambda t: (0 if t["term"].lower().startswith(q) else 1, t["term"].lower()))
        self.terms_panel.items = rows
        self.empty.visible = not rows
        self.count.text = ("%d terms, each linked to the lesson that explains it" % len(self._terms)) if not q else \
            "%s of %d" % (state.plural(len(rows), "term"), len(self._terms))

    @handle("search_box", "change")
    def search_box_change(self, **event_args):
        self._draw()
