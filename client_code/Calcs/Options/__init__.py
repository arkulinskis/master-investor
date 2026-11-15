from anvil import *

from ._anvil_designer import OptionsTemplate
from ... import calc


class Options(OptionsTemplate):
    """Calculator: Options. Recalculates on every keystroke (calc.wire); results go into a sheet of Items.SheetRow."""

    def fail(self, text):
        self.msg.text, self.msg.visible = text, True
        self.out_box.visible = False
        return None

    def ok(self, rows):
        self.msg.visible = False
        self.out_box.visible = True
        self.out_panel.items = rows

    BOXES = ("strike_box", "premium_box", "size_box")

    def __init__(self, **properties):
        super().__init__(**properties)
        calc.wire(self, [getattr(self, b) for b in self.BOXES])
        for d in (self.type_drop, self.side_drop):
            d.add_event_handler("change", self.recalc)
        self.recalc()

    def recalc(self, **event_args):
        k, prem, size = [calc.num(getattr(self, b)) for b in self.BOXES]
        if None in (k, prem, size) or k <= 0 or prem < 0 or size <= 0:
            return self.fail("Fill in the strike, premium and contract size (above 0).")
        call = self.type_drop.selected_value == "Call"
        long = (self.side_drop.selected_value or "").startswith("Buy")
        sign = 1 if long else -1

        def pnl(s):
            intrinsic = max(s - k, 0) if call else max(k - s, 0)
            return sign * (intrinsic - prem) * size

        be = k + prem if call else k - prem
        cost = prem * size
        if long:
            max_gain = "Unlimited" if call else calc.money((k - prem) * size, 2)
            max_loss = calc.money(-cost, 2)
        else:
            max_gain = calc.money(cost, 2)
            max_loss = "Unlimited" if call else calc.money(-(k - prem) * size, 2)
        name = ("Long " if long else "Short ") + ("call" if call else "put")
        self.ok(calc.rows([("Position", name), ("Premium " + ("paid" if long else "received"), calc.money(cost, 2)),
                           ("Breakeven at expiry", calc.money(be, 2)), ("Best case", max_gain), ("Worst case", max_loss),
                           ("Profit if the share ends 10% above the strike", calc.money(pnl(k * 1.1), 2)),
                           ("Profit if it ends 10% below", calc.money(pnl(k * 0.9), 2))], mark=2))
        pts = [[k * (0.5 + i / 60.0), pnl(k * (0.5 + i / 60.0))] for i in range(0, 61)]
        self.chart_title.text = "Profit or loss at expiry for each share price"
        self.chart.show_spec({"label": "Option payoff", "x_fmt": "num", "y_fmt": "num", "zero": True,
                              "marks": [{"x": k, "label": "strike"}, {"x": be, "label": "breakeven"}],
                              "series": [{"points": pts, "tone": "brand", "kind": "line"}]})
