from anvil import *

from ._anvil_designer import SharpeTemplate
from ... import calc


class Sharpe(SharpeTemplate):
    """Calculator: Sharpe. Recalculates on every keystroke (calc.wire); results go into a sheet of Items.SheetRow."""

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

    BOXES = ("returns_box", "ppy_box", "rf_box")

    def recalc(self, **event_args):
        import math
        raw = (self.returns_box.text or "").replace(",", " ").replace("%", " ").split()
        try:
            rets = [float(x) / 100.0 for x in raw]
        except ValueError:
            return self.fail("Returns must be numbers, separated by commas or spaces.")
        ppy, rf = calc.num(self.ppy_box), calc.num(self.rf_box)
        if len(rets) < 3 or not ppy or ppy <= 0 or rf is None:
            return self.fail("Enter at least 3 returns, and the periods per year.")
        n = len(rets)
        mean = sum(rets) / n
        sd = math.sqrt(sum((x - mean) ** 2 for x in rets) / (n - 1))
        rf_p = rf / 100.0 / ppy
        down = math.sqrt(sum(min(0.0, x - rf_p) ** 2 for x in rets) / n)
        ann_ret, ann_vol = mean * ppy, sd * math.sqrt(ppy)
        sharpe = (ann_ret - rf / 100.0) / ann_vol if ann_vol else None
        sortino = (ann_ret - rf / 100.0) / (down * math.sqrt(ppy)) if down else None
        eq, peak, mdd, pts = 1.0, 1.0, 0.0, [[0, 100.0]]
        for i, x in enumerate(rets):
            eq *= 1 + x
            peak = max(peak, eq)
            mdd = min(mdd, eq / peak - 1)
            pts.append([i + 1, 100 * eq])
        total = eq - 1
        self.ok(calc.rows([("Periods", str(n)), ("Average return per period", calc.pct(100 * mean, 2)),
                           ("Annual return (simple)", calc.pct(100 * ann_ret)), ("Annual volatility", calc.pct(100 * ann_vol)),
                           ("Sharpe ratio", "%.2f" % sharpe if sharpe is not None else "-"),
                           ("Sortino ratio", "%.2f" % sortino if sortino is not None else "no losing periods"),
                           ("Total growth over the list", calc.pct(100 * total)), ("Worst drawdown", calc.pct(100 * mdd))], mark=4))
        self.chart_title.text = "Growth of 100 over the periods"
        self.chart.show_spec({"label": "Growth of 100", "x_fmt": "num", "y_fmt": "num",
                              "series": [{"points": pts, "tone": "brand", "kind": "area"}]})
