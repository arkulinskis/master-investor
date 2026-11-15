from anvil import *

from ._anvil_designer import LinkRowTemplate
from ... import state


class LinkRow(LinkRowTemplate):
    """An outside link (opens in a new tab). item = {label, url}."""

    def __init__(self, **properties):
        super().__init__(**properties)
        state.set_attr(self, "href", self.item["url"])
