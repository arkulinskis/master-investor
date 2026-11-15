# Master Investor: content brief (for the people/agents writing the curriculum)

Master Investor is a free learning app that teaches investing from the first lesson to quant level: beginners, serious
DIY investors and advanced traders. Each lesson is short and clear, and ends with hide-and-reveal cards: the learner
reads a question, thinks, presses Reveal, then marks "Got it" or "Not yet" (spaced repetition). The cards are the main
way people test themselves, so they matter as much as the lesson text.

## Files

One Python module per track: `server_code/tr_<trackid>.py`, defining one dict `TRACK`. The exact schema and rules
are in the docstring of `tools/content_check.py` (read it). Run `python -I tools/content_check.py` from the app folder
(`C:\Users\arkvi\Documents\CLAUDE\master-investor`) until it prints CONTENT OK for your files. Other writers work on
other tr_ files at the same time: only create/edit your own files.

Template:

```python
"""Track: <Title>. Content for Master Investor (see tools/CONTENT_BRIEF.md)."""

TRACK = {
    "id": "foundations",
    "title": "Foundations",
    "level": "Beginner",            # the track's main level
    "blurb": "One or two sentences on what this track gives you.",
    "lessons": [
        {
            "id": "compounding",
            "title": "Compounding and the time value of money",
            "level": "Beginner",
            "minutes": 7,
            "summary": "Why money now is worth more than money later, and how growth on growth builds wealth.",
            "body": """
Paragraph...

### A subheading

- a list item
- **bold** for the key idea

`FV = PV x (1 + r)^n`

> Rule of thumb: ...
""",
            "example": {"title": "Worked example: 10,000 for 30 years", "body": """markdown with the numbers worked step by step"""},
            "terms": [("Future value", "What a sum grows to at a given rate after a number of years."), ...],
            "cards": [("What does the rule of 72 tell you?", "Roughly how many years money takes to double: 72 divided by the yearly return in percent. At 8% a year, about 9 years."), ...],
            "calc": "compound",
            "links": [("Investor.gov compound interest calculator", "https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator")],
        },
    ],
}
```

## How to write

- **Accurate first.** Only state facts, formulas, rules and numbers you are sure of. Formulas must be right (check
  each worked example's arithmetic; round sensibly). When evidence is mixed, say so ("studies disagree", "the evidence
  for X is weak"). Never invent statistics, studies or quotes. Country-neutral: use plain amounts (10,000), and when an
  account type matters give examples from several countries (401(k)/IRA, ISA, TFSA/RRSP...).
- **Clear, plain English** (British/Canadian spelling: favourite, colour, behaviour). Short sentences. Explain every
  term the first time. Concrete numbers beat abstractions. A beginner lesson assumes nothing; a Pro lesson can assume
  the earlier tracks but still explains its own terms.
- **No hype, no advice.** Teach how things work and how professionals think; never tell people what to buy. No
  buzzwords (unlock, supercharge, seamless, game-changer...). No em dashes or en dashes anywhere.
- **Body:** 250-450 words is the sweet spot (checker allows 180-650), 2-4 `###` subheadings, a formula in backticks on
  its own line where useful (use `x` or `*` for multiply, `/` for divide, `^` for powers), one `>` rule of thumb or
  common mistake. No tables, links or HTML in markdown.
- **Example:** a worked example with numbers that a learner could redo in a spreadsheet (fictional companies, e.g.
  "Northwind Tools", never real tickers for made-up numbers). Use None only where an example would be forced.
- **Cards (6-9 per lesson):** a mix of: definitions ("What is free cash flow?"), why ("Why do bond prices fall when
  rates rise?"), how-to ("How do you turn EV/EBITDA into a share price?"), small calculations ("A stock at 50 with EPS
  of 2.50: what is the P/E?" with the working in the answer), judgement ("A company's profits grow but operating cash
  flow falls three years running. What should you suspect?"), and misconceptions ("True or false: ..."). Answers 1-3
  sentences, self-contained (they are shown out of context in Practice), with the key idea first. Each card must be
  answerable from the lesson.
- **Terms:** 3-7 per lesson, one-sentence definitions (they build the glossary; avoid duplicating a term another
  lesson in your tracks already defines).
- **calc:** link a lesson to a calculator when it fits: compound (growth with contributions), dcf (5-year DCF +
  terminal value per share), position (shares to buy from account size, risk %, entry, stop), kelly (Kelly fraction
  from win rate and payoff), bond (price from coupon, yield, years), options (payoff at expiry of calls/puts),
  sharpe (Sharpe/Sortino from returns). Otherwise None.
- **links:** 0-4 per lesson, only stable official pages you are confident exist (sec.gov, investor.gov,
  fred.stlouisfed.org, federalreserve.gov, ecb.europa.eu, mba.tuck.dartmouth.edu/pages/faculty/ken.french,
  pages.stern.nyu.edu/~adamodar, cfainstitute.org, bis.org, github.com/<real repo>...). Fewer is better than wrong.
