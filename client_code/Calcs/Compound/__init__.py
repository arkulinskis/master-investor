from anvil import *

from ._anvil_designer import CompoundTemplate
from ... import calc


class Compound(CompoundTemplate):
    """Calculator: Compound. Recalculates on every keystroke (calc.wire); results go into a sheet of Items.SheetRow."""

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

    BOXES = ("start_box", "monthly_box", "rate_box", "years_box", "infl_box")

    def recalc(self, **event_args):
        start, monthly, rate, years, infl = [calc.num(getattr(self, b)) for b in self.BOXES]
        if None in (start, monthly, rate, years, infl) or not 0 < years <= 80 or start < 0 or monthly < 0 or rate <= -100:
            return self.fail("Fill in every box: amounts of 0 or more, 1 to 80 years.")
        n = int(round(years * 12))
        rm = (1 + rate / 100.0) ** (1 / 12.0) - 1
        value, paid = start, start
        pts_v, pts_p = [[0, value]], [[0, paid]]
        for m in range(1, n + 1):
            value = value * (1 + rm) + monthly
            paid += monthly
            if m % 12 == 0 or m == n:
                pts_v.append([m / 12.0, value])
                pts_p.append([m / 12.0, paid])
        real = value / (1 + infl / 100.0) ** (n / 12.0)
        self.ok(calc.rows([("Value at the end", calc.money(value, 0)), ("You put in", calc.money(paid, 0)),
                           ("Growth on top", calc.money(value - paid, 0)),
                           ("Growth share of the total", calc.pct(100.0 * (value - paid) / value if value else 0)),
                           ("In today's money", calc.money(real, 0))], mark=0))
        self.chart_title.text = "Value (green) against what you paid in (grey), by year"
        self.chart.show_spec({"label": "Value against money paid in", "x_fmt": "num", "y_fmt": "money",
                              "series": [{"points": pts_p, "tone": "muted", "kind": "line", "dash": True},
                                         {"points": pts_v, "tone": "brand", "kind": "area"}]})
