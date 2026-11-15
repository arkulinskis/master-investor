from anvil import *

from ._anvil_designer import SheetRowTemplate


class SheetRow(SheetRowTemplate):
    """A spreadsheet row in a calculator table. item = {"cells": [str, ...] (1-5), "head": bool, "mark": index or None}.
    head = the column-header row; mark = the cell to highlight (the base case in a sensitivity grid)."""

    def __init__(self, **properties):
        super().__init__(**properties)
        cells = list(self.item.get("cells", []))
        mark = self.item.get("mark")
        for i, lab in enumerate([self.c0, self.c1, self.c2, self.c3, self.c4]):
            lab.visible = i < len(cells)
            if i < len(cells):
                lab.text = cells[i]
                roles = ["sh-cell"] + (["sh-key"] if i == 0 else []) + (["sh-mark"] if mark == i else [])
                lab.role = roles
        self.classes["sh-head"] = bool(self.item.get("head"))
        self.classes["sh-n%d" % len(cells)] = True
