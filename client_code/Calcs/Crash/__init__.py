import random

from anvil import *

from ._anvil_designer import CrashTemplate
from ... import calc, state
from ... import history_data as H

# preset button -> (start year, years): famous falls, each with some years after it
PRESETS = {"p_1929": (1929, 15), "p_1973": (1973, 10), "p_2000": (2000, 12), "p_2007": (2007, 10), "p_2021": (2021, 5)}


class Crash(CrashTemplate):
    """Calculator: Crash rehearsal (#tools/crash). Replays real US yearly returns (client_code/history_data.py) for a
    start year, a number of years and a stock/bond split (rebalanced every year). The chart stops at the low point and
    asks: hold, or move to cash? The rest of the story (kept going vs moved to T-bills after that year, the worst fall,
    the years to recover) stays hidden until the person picks one. Any change to the inputs hides it again."""

    BOXES = ("year_box", "years_box", "stocks_box", "amount_box")

    def __init__(self, **properties):
        super().__init__(**properties)
        calc.wire(self, [getattr(self, b) for b in self.BOXES])
        for name in PRESETS:
            b = getattr(self, name)
            b.tag.key = name
            b.add_event_handler("click", self._preset_click)
        state.live(self.ask_text)
        state.live(self.told_text)
        self._sim = None
        self._choice = None
        self.recalc()

    def fail(self, text):
        self._sim = None
        self.msg.text, self.msg.visible = text, True
        for part in (self.out_box, self.ask_box, self.told_box, self.chart_box):
            part.visible = False
        return None

    # ---------------------------------------------------------------- inputs -> a simulated path
    def recalc(self, **event_args):
        y0, n, w, amt = [calc.num(getattr(self, b)) for b in self.BOXES]
        self._mark_preset(y0, n)
        if None in (y0, n, w, amt):
            return self.fail("Fill in every box with a number.")
        if y0 != int(y0) or n != int(n):
            return self.fail("Use whole years for the start year and the number of years.")
        y0, n = int(y0), int(n)
        if not H.FIRST <= y0 < H.LAST:
            return self.fail("The data runs from %d to %d: pick a start year from %d to %d." % (H.FIRST, H.LAST, H.FIRST, H.LAST - 1))
        if not 2 <= n <= 40:
            return self.fail("Pick 2 to 40 years, so there is something after the low point.")
        if y0 + n - 1 > H.LAST:
            return self.fail("The data ends in %d. Starting in %d, pick at most %d years." % (H.LAST, y0, H.LAST - y0 + 1))
        if not 0 <= w <= 100:
            return self.fail("Stocks must be 0 to 100%.")
        if not 0 < amt <= 1e12:
            return self.fail("The amount must be more than 0.")
        self._sim = self._simulate(y0, n, w / 100.0, amt)
        self._choice = None
        self.msg.visible = False
        self._draw()

    def _simulate(self, y0, n, w, amt):
        years = list(range(y0, y0 + n))
        vals, rets = [amt], []
        for y in years:
            s, bill, bond = H.RETURNS[y]
            r = w * s / 100.0 + (1 - w) * bond / 100.0
            rets.append(r)
            vals.append(vals[-1] * (1 + r))
        # the decision point: the deepest low before the last year (so something is left to reveal);
        # with no fall at all, the year with the weakest return
        peak, p, p_dd = vals[0], None, 0.0
        for i in range(1, n):
            peak = max(peak, vals[i])
            dd = vals[i] / peak - 1
            if dd < p_dd:
                p, p_dd = i, dd
        if p is None:
            p = min(range(1, n), key=lambda i: rets[i - 1])
            p_dd = vals[p] / max(vals[:p + 1]) - 1
        # the whole window's worst fall and how long the way back took
        peak, peak_i, worst, w_peak_i, w_low_i = vals[0], 0, 0.0, 0, None
        for i in range(1, n + 1):
            if vals[i] > peak:
                peak, peak_i = vals[i], i
            dd = vals[i] / peak - 1
            if dd < worst:
                worst, w_peak_i, w_low_i = dd, peak_i, i
        back = None
        if w_low_i is not None:
            back = next((j for j in range(w_low_i + 1, n + 1) if vals[j] >= vals[w_peak_i]), None)
        cash = [vals[p]]
        for y in years[p:]:
            cash.append(cash[-1] * (1 + H.RETURNS[y][1] / 100.0))
        return {"years": years, "vals": vals, "p": p, "p_dd": p_dd, "worst": worst, "w_peak_i": w_peak_i,
                "w_low_i": w_low_i, "back": back, "cash": cash, "amt": amt, "w": w}

    def _year_at(self, i):
        """Value index i = the end of years[i - 1]; index 0 = the start of the first year."""
        return self._sim["years"][0] - 1 + i

    # ---------------------------------------------------------------- drawing
    def _draw(self):
        S = self._sim
        if S is None:
            return
        years, vals, p = S["years"], S["vals"], S["p"]
        first, last, p_year = years[0], years[-1], self._year_at(p)
        revealed = self._choice is not None
        self.out_box.visible = self.chart_box.visible = True
        self.ask_box.visible = not revealed
        self.told_box.visible = revealed
        down = calc.pct(100 * S["p_dd"]) if S["p_dd"] < 0 else "no fall yet"
        rows = [("Put in at the start of %d" % first, calc.money(S["amt"], 0)),
                ("Value at the end of %d" % p_year, calc.money(vals[p], 0)),
                ("Down from its high so far", down)]
        pts_kept = [[self._year_at(i), vals[i]] for i in range(len(vals))]
        if not revealed:
            self.ask_text.text = "Your %s is now %s. Hold, or move to cash?" % (calc.money(S["amt"], 0), calc.money(vals[p], 0))
            self.ask_sub.text = ("It's the end of %d. %d more %s to go. Moving to cash means 3-month T-bills from here on. "
                                 "Pick one to see what happened." % (p_year, last - p_year, "year" if last - p_year == 1 else "years"))
            rows += [("Kept going, end of %d" % last, "?"), ("Moved to cash after %d" % p_year, "?")]
            self.out_panel.items = calc.rows(rows, mark=1)
            self.chart_title.text = "Value at each year end, %d to %d. The rest is hidden until you decide." % (first, p_year)
            self.chart.show_spec({"label": "Value up to the end of %d" % p_year, "x_fmt": "num", "y_fmt": "money",
                                  "series": [{"points": pts_kept[:p + 1], "tone": "brand", "kind": "area"}],
                                  "marks": [{"x": p_year, "label": "Now"}]})
            return
        kept, cash_end = vals[-1], S["cash"][-1]
        gap = kept - cash_end
        if S["w_low_i"] is None:
            worst_txt, back_txt = "none at year ends", "nothing to recover"
        else:
            worst_txt = "%s (%d to %d)" % (calc.pct(100 * S["worst"]), self._year_at(S["w_peak_i"]), self._year_at(S["w_low_i"]))
            if S["back"] is None:
                back_txt = "not back by the end of %d" % last
            else:
                n_back = S["back"] - S["w_low_i"]
                back_txt = "%d %s (end of %d)" % (n_back, "year" if n_back == 1 else "years", self._year_at(S["back"]))
        rows = [("Worst fall, high to low", worst_txt), ("Back to the old high", back_txt),
                ("Kept going, end of %d" % last, calc.money(kept, 0)),
                ("Moved to cash after %d" % p_year, calc.money(cash_end, 0)),
                ("Kept going minus cash", ("+" if gap > 0 else "") + calc.money(gap, 0))]
        self.out_panel.items = calc.rows(rows, mark=2 if self._choice == "hold" else 3)
        picked = "You held." if self._choice == "hold" else "You moved to cash."
        if abs(gap) < 0.005 * max(kept, cash_end):
            verdict = "Here, both ended within half a percent of each other."
        elif gap > 0:
            verdict = "Here, holding ended %s ahead of moving to cash." % calc.money(gap, 0)
        else:
            verdict = "Here, moving to cash ended %s ahead of holding." % calc.money(-gap, 0)
        self.told_text.text = "%s %s" % (picked, verdict)
        self.told_sub.text = ("Nobody knows at the low point which kind of window they are in. Notice how the choice felt "
                              "before you knew: that feeling is what a plan has to survive.")
        self.chart_title.text = "Kept going (green) against moved to cash after %d (dashed), %d to %d" % (p_year, first, last)
        pts_cash = [[p_year + k, v] for k, v in enumerate(S["cash"])]
        self.chart.show_spec({"label": "Kept going against moved to cash", "x_fmt": "num", "y_fmt": "money",
                              "series": [{"points": pts_kept, "tone": "brand", "kind": "area"},
                                         {"points": pts_cash, "tone": "ink", "kind": "line", "dash": True}],
                              "marks": [{"x": p_year, "label": "You decided here"}]})

    def _mark_preset(self, y0, n):
        for name, (py, pn) in PRESETS.items():
            b = getattr(self, name)
            on = y0 == py and n == pn
            b.role = ["seg", "on"] if on else ["seg"]
            state.set_control_attr(b, "aria-pressed", "true" if on else "false")

    # ---------------------------------------------------------------- buttons
    def _preset_click(self, sender, **event_args):
        y0, n = PRESETS[sender.tag.key]
        self.year_box.text, self.years_box.text = str(y0), str(n)
        self.recalc()

    def _decide(self, choice):
        if self._sim is not None:
            self._choice = choice
            self._draw()
            state.focus(self.rewind_button)

    @handle("hold_button", "click")
    def hold_button_click(self, **event_args):
        self._decide("hold")

    @handle("cash_button", "click")
    def cash_button_click(self, **event_args):
        self._decide("cash")

    @handle("rewind_button", "click")
    def rewind_button_click(self, **event_args):
        self._choice = None
        self._draw()
        state.focus(self.hold_button)

    @handle("random_button", "click")
    def random_button_click(self, **event_args):
        n = calc.num(self.years_box)
        n = int(n) if n is not None and n == int(n) and 2 <= n <= 40 else 10
        self.years_box.text = str(n)
        self.year_box.text = str(random.randint(H.FIRST, H.LAST - n + 1))
        self.recalc()
