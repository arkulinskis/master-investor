from anvil import *

from ._anvil_designer import ToolsTemplate
from ... import router, state

# calculator key -> (title, lesson that explains it, lesson title)
CALCS = {
    "compound": ("Compound growth", "compounding", "Compounding and the time value of money"),
    "dcf": ("Discounted cash flow value", "dcf", "The discounted cash flow model, step by step"),
    "bond": ("Bond price and duration", "bonds", "Bonds: price, yield and duration"),
    "options": ("Option payoff at expiry", "options", "Options from zero"),
    "sharpe": ("Sharpe, Sortino and drawdown", "risk-metrics", "Measuring risk"),
    "position": ("Position size from your stop", "risk-per-trade", "Risk per trade"),
    "kelly": ("Kelly bet size", "position-sizing", "Position sizing"),
    "crash": ("Crash rehearsal: hold or sell?", "behaviour", "Your brain on markets"),
}


def _make(key):
    if key == "compound":
        from ...Calcs.Compound import Compound
        return Compound()
    if key == "dcf":
        from ...Calcs.Dcf import Dcf
        return Dcf()
    if key == "bond":
        from ...Calcs.Bond import Bond
        return Bond()
    if key == "options":
        from ...Calcs.Options import Options
        return Options()
    if key == "sharpe":
        from ...Calcs.Sharpe import Sharpe
        return Sharpe()
    if key == "position":
        from ...Calcs.Position import Position
        return Position()
    if key == "crash":
        from ...Calcs.Crash import Crash
        return Crash()
    from ...Calcs.Kelly import Kelly
    return Kelly()


class Tools(ToolsTemplate):
    """#tools/<calc>: eight calculators, one at a time (each a Form in Calcs/, made when first opened)."""

    def __init__(self, args=(), **properties):
        super().__init__(**properties)
        state.heading(self.title, 1)
        self._buttons = {"compound": self.t_compound, "dcf": self.t_dcf, "bond": self.t_bond, "options": self.t_options,
                         "sharpe": self.t_sharpe, "position": self.t_position, "kelly": self.t_kelly,
                         "crash": self.t_crash}
        for key, b in self._buttons.items():
            b.tag.key = key
            b.add_event_handler("click", self._tab_click)
        self._open(args[0] if args and args[0] in CALCS else "compound")

    def _open(self, key):
        self._key = key
        title, lesson, lesson_title = CALCS[key]
        self.calc_title.text = title
        state.set_attr(self.lesson_link, "href", router.href("lesson", lesson))
        self.lesson_label.text = "The lesson: " + lesson_title
        self.holder.clear()
        self.holder.add_component(_make(key))
        for k, b in self._buttons.items():
            b.role = ["seg", "on"] if k == key else ["seg"]
            state.set_control_attr(b, "aria-pressed", "true" if k == key else "false")

    def _tab_click(self, sender, **event_args):
        self._open(sender.tag.key)
        router.replace("tools", sender.tag.key)
