import json

from anvil import *
import anvil.js
from anvil.js import window

from ._anvil_designer import LineChartTemplate


class LineChart(LineChartTemplate):
    """A chart for the calculators. Set .spec (JSON text, or call .show_spec(dict)); the JS engine MIChart draws it."""

    def __init__(self, **properties):
        self._spec, self._shown = "", False
        super().__init__(**properties)

    @property
    def spec(self):
        return self._spec

    @spec.setter
    def spec(self, value):
        self._spec = value or ""
        self._draw()

    def show_spec(self, d):
        self.spec = json.dumps(d)

    def _draw(self):
        if self._shown and self._spec and window.get("MIChart"):
            window.MIChart.draw(self.dom_nodes["box"], self._spec)

    @handle("", "show")
    def form_show(self, **event_args):
        self._shown = True
        self._draw()

    @handle("", "hide")
    def form_hide(self, **event_args):
        self._shown = False
