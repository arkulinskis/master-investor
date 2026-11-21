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

    BOXES = ("start_box", "monthly_box", "rate_box", "years_box", "infl_box", "fee_box")

    def recalc(self, **event_args):
        start, monthly, rate, years, infl, fee = [calc.num(getattr(self, b)) for b in self.BOXES]
        if None in (start, monthly, rate, years, infl, fee) or not 0 < years <= 80 or start < 0 or monthly < 0 or rate <= -100:
            return self.fail("Fill in every box: amounts of 0 or more, 1 to 80 years.")
        if not 0 <= fee < 20:
            return self.fail("The yearly fee must be 0 or more and under 20%.")
        n = int(round(years * 12))
        rm = (1 + rate / 100.0) ** (1 / 12.0) - 1
        fm = (1 - fee / 100.0) ** (1 / 12.0)  # the fee, taken a twelfth at a time from the whole balance
        value, gross, paid = start, start, start
        pts_v, pts_g, pts_p = [[0, value]], [[0, gross]], [[0, paid]]
        for m in range(1, n + 1):
            value = value * (1 + rm) * fm + monthly
            gross = gross * (1 + rm) + monthly
            paid += monthly
            if m % 12 == 0 or m == n:
                pts_v.append([m / 12.0, value])
                pts_g.append([m / 12.0, gross])
                pts_p.append([m / 12.0, paid])
        real = value / (1 + infl / 100.0) ** (n / 12.0)
        pairs = [("Value at the end", calc.money(value, 0)), ("You put in", calc.money(paid, 0)),
                 ("Growth on top", calc.money(value - paid, 0)),
                 ("Growth share of the total", calc.pct(100.0 * (value - paid) / value if value else 0)),
                 ("In today's money", calc.money(real, 0))]
        series = [{"points": pts_p, "tone": "muted", "kind": "line", "dash": True}]
        if fee > 0:
            pairs += [("Lost to fees", calc.money(gross - value, 0)), ("Value with no fees", calc.money(gross, 0))]
            series.append({"points": pts_g, "tone": "ink", "kind": "line", "dash": True})
            self.chart_title.text = "Value after fees (green), with no fees (dark dashes) and what you paid in (grey), by year"
        else:
            self.chart_title.text = "Value (green) against what you paid in (grey), by year"
        series.append({"points": pts_v, "tone": "brand", "kind": "area"})
        self.ok(calc.rows(pairs, mark=0))
        self.chart.show_spec({"label": "Value against money paid in", "x_fmt": "num", "y_fmt": "money", "series": series})
