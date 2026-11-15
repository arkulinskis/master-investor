from anvil import *

from ._anvil_designer import LibItemTemplate
from ... import state


class LibItem(LibItemTemplate):
    """One library entry: a data source, a GitHub repository or a book. item = a dict from get_library."""

    def __init__(self, **properties):
        super().__init__(**properties)
        it = self.item
        self.kind.text = it.get("kind") or ("Book" if it.get("author") else "")
        self.kind.visible = bool(self.kind.text)
        extra = it.get("cost") or it.get("lang") or it.get("author") or ""
        self.extra.text = extra
        self.extra.visible = bool(extra)
        self.level.visible = bool(it.get("level"))
        url = it.get("url", "")
        state.set_attr(self.open_link, "href", url)
        host = url.split("//", 1)[-1].split("?", 1)[0].rstrip("/")
        self.url_label.text = host if len(host) < 48 else host[:46] + "..."
        state.set_attr(self.open_link, "aria-label", "Open %s (new tab)" % it.get("name", ""))
