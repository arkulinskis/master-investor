from anvil import *
import anvil.server
from anvil.js import window

from ._anvil_designer import LessonTemplate
from ... import router, state

CALC_NAMES = {"compound": "the compound growth calculator", "dcf": "the DCF calculator", "position": "the position size calculator",
              "kelly": "the Kelly calculator", "bond": "the bond calculator", "options": "the option payoff calculator",
              "sharpe": "the Sharpe and Sortino calculator", "crash": "the crash rehearsal (hold or sell, on real history)"}


class Lesson(LessonTemplate):
    """#lesson/<id>: the lesson (markdown), a worked example, key terms, a calculator link, the hide-and-reveal cards
    (Reveal all, or one at a time in Practice), Mark as done / Save for members, previous and next lesson."""

    def __init__(self, args=(), **properties):
        super().__init__(**properties)
        state.heading(self.title, 1)
        self.cards_panel.add_event_handler("x-graded", self._graded)
        self._tally = {"knew": 0, "seen": 0}
        r = anvil.server.call("get_lesson", args[0] if args else "")
        self.found.visible = bool(r.get("ok"))
        self.missing.visible = not r.get("ok")
        if not r.get("ok"):
            self.track_link.visible = False
            return
        L = r["lesson"]
        self._L = L
        self._cards = r["cards"]
        window.document.title = L["title"] + " · Master Investor"
        state.set_attr(self.track_link, "href", router.href("track", L["track"]))
        self.track_label.text = L["track_title"]
        self.level.text = L["level"]
        self.meta.text = "Lesson %d of %d · %d min read · %s" % (L["pos"], L["of"], L["minutes"], state.plural(len(self._cards), "card"))
        self.title.text = L["title"]
        self.summary.text = L["summary"]
        self.body.content = L["body"]
        ex = L.get("example")
        self.example_box.visible = bool(ex)
        if ex:
            self.example_title.text = ex["title"]
            self.example_body.content = ex["body"].strip()
        self.calc_link.visible = bool(L.get("calc"))
        if L.get("calc"):
            state.set_attr(self.calc_link, "href", router.href("tools", L["calc"]))
            self.calc_label.text = "Try the numbers yourself in " + CALC_NAMES.get(L["calc"], "the calculators")
        state.set_attr(self.public_link, "href", "/lessons/" + L["id"])
        self.terms_panel.items = L["terms"]
        self.links_box.visible = bool(L["links"])
        self.links_panel.items = L["links"]
        self._open = False
        self._draw_cards()
        me = state.me()
        self.member_finish.visible = bool(me)
        self.guest_finish.visible = not me
        self._done, self._saved = L["done"], L["saved"]
        self._draw_finish()
        for link, label, other, word in ((self.prev_link, self.prev_label, r["prev"], "Previous: "),
                                         (self.next_link, self.next_label, r["next"], "Next: ")):
            link.visible = bool(other)
            if other:
                state.set_attr(link, "href", router.href("lesson", other["id"]))
                label.text = word + other["title"]

    def _draw_cards(self):
        self.cards_panel.items = [dict(c, open=self._open) for c in self._cards]
        self.reveal_all_button.text = "Hide all" if self._open else "Reveal all"
        self.reveal_all_button.role = ["btn", "btn-sm", "ic-x" if self._open else "ic-eye"]

    def _draw_finish(self):
        self.done_badge.visible = self._done
        self.done_button.text = "Done: mark as not done" if self._done else "Mark lesson as done"
        self.done_button.role = ["btn", "ic-check"] if self._done else ["btn", "btn-primary", "ic-check"]
        self.save_button.text = "Saved" if self._saved else "Save for later"
        state.set_control_attr(self.save_button, "aria-pressed", "true" if self._saved else "false")

    def _graded(self, knew=False, card=None, **event_args):
        self._tally["seen"] += 1
        self._tally["knew"] += 1 if knew else 0
        self.score.visible = True
        self.score.text = "You knew %d of the %d cards you've graded here." % (self._tally["knew"], self._tally["seen"])
        if self._tally["seen"] == len(self._cards) and not self._done and state.me():
            self.score.text += " Nicely done. Mark the lesson as done below when you're ready."

    @handle("reveal_all_button", "click")
    def reveal_all_button_click(self, **event_args):
        self._open = not self._open
        self._draw_cards()

    @handle("share_button", "click")
    def share_button_click(self, **event_args):
        """The lesson's public page (/lessons/<id>, readable without the app): the phone's share sheet where there
        is one, otherwise the link goes to the clipboard, otherwise it's shown to copy by hand."""
        url = window.location.origin + "/lessons/" + self._L["id"]
        nav = window.navigator
        if getattr(nav, "share", None):
            try:
                nav.share({"title": self._L["title"] + " · Master Investor", "text": self._L["summary"], "url": url})
                return
            except Exception as e:
                if "AbortError" in str(e) or "abort" in str(e).lower():
                    return  # they closed the share sheet
        try:
            nav.clipboard.writeText(url)
            state.toast("Link copied: " + url, "ok")
        except Exception:
            box = TextBox(text=url)
            alert(box, title="Copy this link", buttons=[("Done", True)])

    @handle("practice_button", "click")
    def practice_button_click(self, **event_args):
        router.go("practice", "lesson", self._L["id"])

    @handle("done_button", "click")
    def done_button_click(self, **event_args):
        r = state.call("mark_lesson", self._L["id"], not self._done)
        if r is None:
            return
        self._done = r["done"]
        self._draw_finish()
        if r["done"] and r["track_done"]:
            state.toast("Track finished: every lesson in %s is done!" % self._L["track_title"], "ok")
        elif r["done"]:
            state.toast("Lesson done. Its cards join your review deck.", "ok")

    @handle("save_button", "click")
    def save_button_click(self, **event_args):
        r = state.call("save_lesson", self._L["id"], not self._saved)
        if r is not None:
            self._saved = r["saved"]
            self._draw_finish()
            state.toast("Saved for later" if self._saved else "Removed from saved", "ok")
