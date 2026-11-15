from anvil import *

from ._anvil_designer import BondTemplate
from ... import calc


class Bond(BondTemplate):
    """Calculator: Bond. Recalculates on every keystroke (calc.wire); results go into a sheet of Items.SheetRow."""

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

    BOXES = ("face_box", "coupon_box", "yield_box", "years_box", "freq_box")

    def price(self, face, c, y, years, m):
        n = int(round(years * m))
        cpn = face * c / m
        yy = y / m
        pv, wt = 0.0, 0.0
        for t in range(1, n + 1):
            cf = cpn + (face if t == n else 0)
            d = cf / (1 + yy) ** t
            pv += d
            wt += d * t / m
        return pv, (wt / pv if pv else 0)

    def recalc(self, **event_args):
        face, c, y, years, m = [calc.num(getattr(self, b)) for b in self.BOXES]
        if None in (face, c, y, years, m) or face <= 0 or years <= 0 or years > 100 or m not in (1, 2, 4, 12) or y <= -50:
            return self.fail("Fill in every box: payments per year 1, 2, 4 or 12; years up to 100.")
        c, y, m = c / 100.0, y / 100.0, int(m)
        p, mac = self.price(face, c, y, years, m)
        mod = mac / (1 + y / m)
        p_up, _ = self.price(face, c, y + 0.01, years, m)
        word = "at a discount (yield above coupon)" if p < face - 0.005 else ("at a premium (yield below coupon)" if p > face + 0.005 else "at par")
        self.ok(calc.rows([("Price", calc.money(p, 2)), ("Price as % of face", calc.pct(100 * p / face, 2)), ("Trades", word),
                           ("Current yield", calc.pct(100 * face * c / p, 2)), ("Macaulay duration, years", "%.2f" % mac),
                           ("Modified duration", "%.2f" % mod), ("Price if yields rise 1%", calc.money(p_up, 2))], mark=0))
        pts = []
        top = max(12.0, 100 * y + 4)
        for i in range(1, 61):
            yy = top * i / 60.0
            pts.append([yy, self.price(face, c, yy / 100.0, years, m)[0]])
        self.chart_title.text = "Price at each yield: the curve bends (convexity), and longer bonds bend more"
        self.chart.show_spec({"label": "Bond price against yield", "x_fmt": "pct", "y_fmt": "num",
                              "marks": [{"x": 100 * y, "label": "now"}],
                              "series": [{"points": pts, "tone": "brand", "kind": "line"}]})
