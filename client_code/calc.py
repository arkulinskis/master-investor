"""Helpers for the calculators (client_code/Calcs/*): read numbers typed in boxes, format results, build sheet rows.

    calc.num(box)            the number in a TextBox ("1,250", "7%", " 3.5 " all work), or None
    calc.money(v) / pct(v)   "12,345.68" / "7.2%"
    calc.rows([(label, value), ...], mark=i)   items for a RepeatingPanel of Items.SheetRow (2 cells; mark = highlighted row)
    calc.wire(form, boxes)   recalculate on every keystroke and Enter
"""


def num(box):
    t = (box.text or "").replace(",", "").replace("%", "").replace(" ", "").strip()
    if t in ("", "-", ".", "-."):
        return None
    try:
        return float(t)
    except ValueError:
        return None


def money(v, dp=2):
    if v is None:
        return "-"
    s = ("{:,.%df}" % dp).format(abs(v))
    return ("-" if v < 0 else "") + s


def pct(v, dp=1):
    if v is None:
        return "-"
    return ("{:.%df}" % dp).format(v) + "%"


def rows(pairs, mark=None, head=None):
    out = []
    if head:
        out.append({"cells": list(head), "head": True})
    for i, pair in enumerate(pairs):
        out.append({"cells": list(pair), "mark": 1 if i == mark else None})
    return out


def wire(form, boxes):
    for b in boxes:
        b.add_event_handler("change", form.recalc)
        if type(b).__name__ == "TextBox":  # a TextArea has no pressed_enter (Enter adds a line)
            b.add_event_handler("pressed_enter", form.recalc)
