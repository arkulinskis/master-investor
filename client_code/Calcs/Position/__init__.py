from anvil import *

from ._anvil_designer import PositionTemplate
from ... import calc


class Position(PositionTemplate):
    """Calculator: Position. Recalculates on every keystroke (calc.wire); results go into a sheet of Items.SheetRow."""

    def __init__(self, **properties):
        super().__init__(**properties)
        calc.wire(self, [getattr(self, b) for b in self.BOXES])
        self.recalc()

    def fail(self, text):
        self.msg.text, self.msg.visible = text, True
        self.out_box.visible = False
        return None

    def ok(self, rows):
        self.msg.visible = False
        self.out_box.visible = True
        self.out_panel.items = rows

    BOXES = ("account_box", "risk_box", "entry_box", "stop_box", "target_box")

    def recalc(self, **event_args):
        acct, risk, entry, stop, target = [calc.num(getattr(self, b)) for b in self.BOXES]
        if None in (acct, risk, entry, stop) or acct <= 0 or entry <= 0 or stop <= 0 or not 0 < risk <= 100:
            return self.fail("Fill in the account, risk %, entry and stop (all above 0).")
        per_share = abs(entry - stop)
        if per_share == 0:
            return self.fail("The stop can't equal the entry price.")
        side = "long" if stop < entry else "short"
        budget = acct * risk / 100.0
        shares = int(budget // per_share)
        value = shares * entry
        out = [("Direction", "Long (buy)" if side == "long" else "Short (sell)"), ("Money at risk", calc.money(budget, 2)),
               ("Risk per share", calc.money(per_share, 2)), ("Shares", "{:,}".format(shares)),
               ("Position value", calc.money(value, 2)), ("Share of the account", calc.pct(100.0 * value / acct)),
               ("Loss if the stop is hit", calc.money(shares * per_share, 2))]
        if target:
            reward = (target - entry) if side == "long" else (entry - target)
            out.append(("Target as a multiple of risk", "%.2fR" % (reward / per_share)))
            out.append(("Gain at the target", calc.money(shares * reward, 2)))
        if value > acct:
            out.append(("Note", "Bigger than the account: needs margin"))
        self.ok(calc.rows(out, mark=3))
