from anvil import *

from ._anvil_designer import DcfTemplate
from ... import calc


class Dcf(DcfTemplate):
    """Calculator: Dcf. Recalculates on every keystroke (calc.wire); results go into a sheet of Items.SheetRow."""

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

    BOXES = ("fcf_box", "growth_box", "rate_box", "tg_box", "debt_box", "shares_box", "price_box")

    def value(self, fcf, g, r, tg, debt, shares):
        pv, f, rows = 0.0, fcf, []
        for n in range(1, 6):
            f *= 1 + g
            d = (1 + r) ** n
            pv += f / d
            rows.append((n, f, 1 / d, f / d))
        tv = f * (1 + tg) / (r - tg)
        ptv = tv / (1 + r) ** 5
        ev = pv + ptv
        return (ev - debt) / shares, ev, pv, tv, ptv, rows

    def recalc(self, **event_args):
        fcf, g, r, tg, debt, shares, price = [calc.num(getattr(self, b)) for b in self.BOXES]
        if None in (fcf, g, r, tg, debt, shares) or shares <= 0:
            return self.fail("Fill in every box (shares above 0).")
        g, r, tg = g / 100.0, r / 100.0, tg / 100.0
        if r <= tg:
            return self.fail("The discount rate must be higher than the growth after year 5, or the value is infinite.")
        per, ev, pv, tv, ptv, rows = self.value(fcf, g, r, tg, debt, shares)
        out = [("Present value of years 1 to 5", calc.money(pv, 1)), ("Terminal value (in year 5)", calc.money(tv, 1)),
               ("Terminal value, discounted", calc.money(ptv, 1)), ("Terminal share of the value", calc.pct(100 * ptv / ev if ev else 0)),
               ("Enterprise value", calc.money(ev, 1)), ("Equity value (less net debt)", calc.money(ev - debt, 1)),
               ("Value per share", calc.money(per, 2))]
        if price:
            mos = 100.0 * (1 - price / per) if per > 0 else None
            out.append(("Margin of safety at %s" % calc.money(price, 2),
                        calc.pct(mos) if mos is not None else "no value left"))
        self.ok(calc.rows(out, mark=6))
        table = [{"cells": ["Year", "Cash flow", "Discount factor", "Present value"], "head": True}]
        for n, f, d, p in rows:
            table.append({"cells": [str(n), calc.money(f, 1), "%.4f" % d, calc.money(p, 1)]})
        table.append({"cells": ["Terminal", calc.money(tv, 1), "%.4f" % (1 / (1 + r) ** 5), calc.money(ptv, 1)]})
        table.append({"cells": ["Sensitivity", "Growth after 5: %s" % calc.pct(100 * tg - 0.5), calc.pct(100 * tg), calc.pct(100 * tg + 0.5)], "head": True})
        for dr in (r - 0.01, r, r + 0.01):
            cells = ["Discount %s" % calc.pct(100 * dr)]
            for t2 in (tg - 0.005, tg, tg + 0.005):
                cells.append(calc.money(self.value(fcf, g, dr, t2, debt, shares)[0], 2) if dr > t2 else "-")
            table.append({"cells": cells, "mark": 2 if abs(dr - r) < 1e-9 else None})
        self.table_panel.items = table
