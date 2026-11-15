from anvil import *

from ._anvil_designer import KellyTemplate
from ... import calc


class Kelly(KellyTemplate):
    """Calculator: Kelly. Recalculates on every keystroke (calc.wire); results go into a sheet of Items.SheetRow."""

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

    BOXES = ("p_box", "b_box")

    def growth(self, f, p, b):
        import math
        if f >= 1 or 1 + b * f <= 0:
            return None
        return p * math.log(1 + b * f) + (1 - p) * math.log(1 - f)

    def recalc(self, **event_args):
        p, b = [calc.num(getattr(self, x)) for x in self.BOXES]
        if p is None or b is None or not 0 < p < 100 or b <= 0:
            return self.fail("The chance must be between 0 and 100, and the payoff above 0.")
        p = p / 100.0
        f = p - (1 - p) / b
        edge = p * b - (1 - p)
        if f <= 0:
            self.ok(calc.rows([("Edge per unit risked", "%.3f" % edge), ("Kelly fraction", "0%: no edge, don't bet")], mark=1))
            self.chart_title.text = ""
            self.chart.spec = ""
            return
        g_full, g_half = self.growth(f, p, b), self.growth(f / 2, p, b)
        self.ok(calc.rows([("Edge per unit risked", "%.3f" % edge), ("Full Kelly", calc.pct(100 * f)),
                           ("Half Kelly", calc.pct(50 * f)), ("Growth per bet, full Kelly", calc.pct(100 * g_full, 2)),
                           ("Growth per bet, half Kelly", calc.pct(100 * g_half, 2)),
                           ("Half Kelly keeps", calc.pct(100 * g_half / g_full if g_full else 0, 0) + " of the growth")], mark=1))
        top = min(0.99, 2.2 * f)
        pts = []
        for i in range(0, 61):
            x = top * i / 60.0
            g = self.growth(x, p, b)
            if g is not None:
                pts.append([100 * x, 100 * g])
        self.chart_title.text = "Growth per bet (%) for each bet size: it peaks at full Kelly and turns negative past about twice that"
        self.chart.show_spec({"label": "Growth per bet by bet size", "x_fmt": "pct", "y_fmt": "pct", "zero": True,
                              "marks": [{"x": 100 * f, "label": "Kelly"}, {"x": 50 * f, "label": "Half"}],
                              "series": [{"points": pts, "tone": "brand", "kind": "line"}]})
