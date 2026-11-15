from anvil import *
import anvil.server

from ._anvil_designer import LibraryTemplate
from ... import router, state

TABS = ["sources", "repos", "books"]


class Library(LibraryTemplate):
    """#library/<sources|repos|books>: data sources, GitHub repositories and books, with a kind filter and search."""

    def __init__(self, args=(), **properties):
        super().__init__(**properties)
        state.heading(self.title, 1)
        self._d = anvil.server.call("get_library")
        self._tabs = dict(zip(TABS, [self.tab_sources, self.tab_repos, self.tab_books]))
        for name, b in self._tabs.items():
            b.tag.tab = name
            b.add_event_handler("click", self._tab_click)
        self._tab = args[0] if args and args[0] in TABS else "sources"
        self._fill_kinds()
        self._draw()

    def _fill_kinds(self):
        kinds = sorted({it.get("kind") or it.get("level") or "" for it in self._d[self._tab]} - {""})
        word = "Every level" if self._tab == "books" else "Every kind"
        self.kind_drop.items = [(word, "")] + [(k, k) for k in kinds]
        self.kind_drop.selected_value = ""
        state.set_control_attr(self.kind_drop, "aria-label", "Filter by kind")

    def _draw(self):
        q = (self.search_box.text or "").strip().lower()
        k = self.kind_drop.selected_value or ""
        rows = []
        for it in self._d[self._tab]:
            if k and (it.get("kind") or it.get("level")) != k:
                continue
            if q and q not in " ".join(str(v) for v in it.values()).lower():
                continue
            rows.append(it)
        self.items_panel.items = rows
        self.empty.visible = not rows
        word = {"sources": "data source", "repos": "repository", "books": "book"}[self._tab]
        self.count.text = state.plural(len(rows), word, "repositories" if word == "repository" else None)
        self.repo_note.visible = self._tab == "repos"
        for name, b in self._tabs.items():
            b.role = ["seg", "on"] if name == self._tab else ["seg"]
            state.set_control_attr(b, "aria-pressed", "true" if name == self._tab else "false")

    def _tab_click(self, sender, **event_args):
        self._tab = sender.tag.tab
        self.search_box.text = ""
        self._fill_kinds()
        self._draw()
        router.replace("library", self._tab)

    @handle("kind_drop", "change")
    def kind_drop_change(self, **event_args):
        self._draw()

    @handle("search_box", "change")
    def search_box_change(self, **event_args):
        self._draw()
