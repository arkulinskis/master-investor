"""Track: Valuing a company. Content for Master Investor (see tools/CONTENT_BRIEF.md)."""

TRACK = {
    "id": "valuation",
    "title": "Valuing a company",
    "level": "Intermediate",
    "blurb": "How professionals put a number on a business: multiples, discounted cash flow, discount rates, "
             "reverse DCF, moats and the companies that break the usual rules.",
    "lessons": [
        # ------------------------------------------------------------------ price-vs-value
        {
            "id": "price-vs-value",
            "title": "Price versus value",
            "level": "Intermediate",
            "minutes": 7,
            "summary": "Price is what you pay, value is what you get: intrinsic value, efficient markets, Mr Market "
                       "and the margin of safety.",
            "body": """
A share price is simply the last price at which a buyer and a seller agreed to trade. **Intrinsic value** is
something else: the amount the business is worth to an owner, which in theory equals all the cash it will hand
to its owners in the future, adjusted for time and risk. Price is a fact you can look up. Value is an estimate,
and two careful analysts can reach different numbers.

### How efficient is the market?

The **efficient market hypothesis** says prices already reflect available information, so it is hard to find
shares that are reliably cheap. Most evidence supports a practical version of this: the large majority of
professional fund managers fail to beat a low-cost index fund over long periods once fees are counted. But
markets are not perfectly efficient. Prices sometimes swing far more than the underlying businesses change,
and bubbles and crashes happen. A sensible view is that the market is usually roughly right, sometimes very
wrong, and it is hard to know in advance which is which.

### Mr Market

Benjamin Graham, the teacher of Warren Buffett, described the market as a business partner called **Mr
Market**. Every day he offers to buy your share of the business or sell you his, at a price that depends on
his mood. Some days he is euphoric and asks far too much; other days he is gloomy and sells cheaply. You are
free to ignore him. His offers are useful only when they are clearly wrong in your favour, and you should never
let his mood set your own view of what the business is worth.

### Margin of safety

Because value is an estimate, Graham's answer was to buy only when the price is well below your estimate. The
gap is the **margin of safety**:

`Margin of safety = (Intrinsic value - Price) / Intrinsic value`

The margin protects you against errors in your forecasts, bad luck and things you did not think of. The less
certain the business, the bigger the margin you should demand.

> Common mistake: treating your own valuation as a fact. A precise-looking number such as 52.37 per share is
> still built on guesses about the future. Think in ranges, and ask what you would need to believe for the
> current price to be fair.
""",
            "example": {
                "title": "Worked example: Bramble Bakeries",
                "body": """
You estimate that Bramble Bakeries is worth about **50 per share**. The shares trade at **35**.

1. Margin of safety = (50 - 35) / 50 = 15 / 50 = **30%**.
2. Suppose your estimate was too optimistic by 20%. True value would be 50 x 0.8 = **40**. You still paid less
   than value: 35 is below 40, so the margin absorbed the error.
3. If you had paid 48 instead, the margin was only (50 - 48) / 50 = 4%. The same 20% error would leave you
   paying 48 for something worth 40, a loss of value of 8 / 48 = about **17%**.

The lesson: the margin of safety is what lets a wrong estimate still turn out acceptably.
""",
            },
            "terms": [
                ("Intrinsic value", "What a business is worth to an owner, based on the cash it is expected to produce over its life, adjusted for time and risk."),
                ("Efficient market hypothesis", "The idea that market prices already reflect available information, so beating the market consistently is very hard."),
                ("Mr Market", "Benjamin Graham's picture of the market as a moody partner who offers to buy or sell every day at prices driven by emotion."),
                ("Margin of safety", "The gap between your estimate of intrinsic value and the price you pay, kept as a cushion against errors."),
            ],
            "cards": [
                ("What is the difference between price and intrinsic value?", "Price is what the last trade happened at, a fact you can look up. Intrinsic value is an estimate of what the business is worth based on the cash it will produce, so it is uncertain and depends on the analyst."),
                ("A stock trades at 60 and you estimate its value at 80. What is your margin of safety?", "(80 - 60) / 80 = 25%. The margin of safety is measured as a share of your value estimate."),
                ("What does the efficient market hypothesis claim, and what is the strongest practical evidence for it?", "It claims prices already reflect available information, so bargains are rare. The strongest practical evidence is that most professional fund managers fail to beat a low-cost index fund over long periods after fees."),
                ("In Graham's Mr Market story, how should you treat his daily price offers?", "As offers you are free to ignore. Use them only when they are clearly wrong in your favour, and never let his mood change your own view of the business's value."),
                ("Why demand a margin of safety at all if you have done careful work?", "Because intrinsic value is an estimate built on forecasts that can be wrong. Buying well below your estimate means that even a sizeable error or some bad luck can still leave you with a fair result."),
                ("Should a stable utility and an unproven biotech need the same margin of safety?", "No. The less predictable the business, the wider your range of possible values, so the bigger the margin of safety you should demand."),
                ("True or false: a share that has fallen 50% must now be cheap.", "False. A falling price says nothing by itself about value. The business may have got worse, or the old price may have been far too high; only a comparison with a value estimate tells you whether it is cheap."),
            ],
            "calc": None,
            "links": [],
        },
        # ------------------------------------------------------------------ multiples
        {
            "id": "multiples",
            "title": "Valuation multiples",
            "level": "Intermediate",
            "minutes": 9,
            "summary": "P/E, EV/EBITDA, EV/Sales, P/B, PEG and dividend yield: how to compute them, how to pick peers, "
                       "and when each one fits.",
            "body": """
A **multiple** compares a company's price to one measure of what it earns or owns. Multiples are quick,
widely quoted and good for comparing similar companies. They hide assumptions about growth and risk, so treat
them as a shortcut, not a full valuation.

### Equity multiples and enterprise multiples

Some multiples use the **share price** (what shareholders pay), others use **enterprise value** (what it would
cost to buy the whole business, debt included).

`Enterprise value = Market cap + Debt + Preferred shares + Minority interests - Cash`

The rule: match the numerator to the denominator. Profit that belongs to everyone who funds the company (EBITDA,
sales) goes with enterprise value. Profit that belongs only to shareholders (net income, book equity, dividends)
goes with the share price or market cap.

- **P/E** = Price / Earnings per share. The most quoted multiple; distorted by debt levels, one-off items and
  tax differences.
- **EV/EBITDA** = Enterprise value / EBITDA (earnings before interest, tax, depreciation and amortisation).
  Useful for comparing companies with different debt levels; ignores the cost of replacing equipment.
- **EV/Sales**. For companies with little or no profit yet; only meaningful next to margins.
- **P/B** = Price / Book value per share. Fits banks and insurers, whose assets are mostly financial and
  carried near market value.
- **PEG** = P/E / expected yearly EPS growth in percent. A rough way to compare P/Es across growth rates.
- **Dividend yield** = Dividend per share / Price. Fits mature payers such as utilities.

### Choosing peers

A multiple only means something next to a fair comparison. Good peers share the same industry and business
model, similar growth, margins, size and risk. Compare against several peers and look at the median, not the
single cheapest or dearest.

### When a low multiple is not cheap

A low P/E can signal a bargain, or a business in decline, a cyclical company at peak profits, or one-off gains
inflating earnings. A high multiple can be justified by strong, durable growth. Always ask *why* the multiple
differs.

> Rule of thumb: a company deserves a higher multiple when it grows faster, earns higher returns on capital and
> carries less risk. If none of those apply, a premium multiple needs a very good explanation.
""",
            "example": {
                "title": "Worked example: Harbour Foods against its peers",
                "body": """
Harbour Foods: share price **40**, **100 million** shares, debt **1,200m**, cash **200m**, EBITDA **500m**,
sales **2,500m**, net income **200m**, book equity **1,600m**, dividend **0.80** per share, expected EPS growth
**10%** a year.

1. Market cap = 40 x 100m = **4,000m**.
2. Enterprise value = 4,000 + 1,200 - 200 = **5,000m**.
3. EV/EBITDA = 5,000 / 500 = **10x**. EV/Sales = 5,000 / 2,500 = **2.0x**.
4. EPS = 200 / 100 = 2.00, so P/E = 40 / 2 = **20x**. PEG = 20 / 10 = **2.0**.
5. Book value per share = 1,600 / 100 = 16, so P/B = 40 / 16 = **2.5x**. Dividend yield = 0.80 / 40 = **2%**.

Now suppose similar food companies trade at a median of **8x EBITDA**:

- Implied EV = 8 x 500 = 4,000m.
- Implied equity = 4,000 - 1,200 + 200 = 3,000m.
- Implied price = 3,000 / 100 = **30 per share**, against 40 in the market.

Before calling Harbour expensive, check whether it grows faster or earns better margins than the peers.
""",
            },
            "terms": [
                ("Enterprise value", "Market cap plus debt, preferred shares and minority interests, minus cash: the price of the whole business."),
                ("EBITDA", "Earnings before interest, tax, depreciation and amortisation, a rough measure of operating profit before financing and asset wear."),
                ("P/E ratio", "Share price divided by earnings per share."),
                ("PEG ratio", "The P/E divided by expected yearly earnings growth in percent."),
                ("Peer group", "A set of comparable companies used as the benchmark for a multiple."),
            ],
            "cards": [
                ("A stock at 50 with EPS of 2.50: what is the P/E?", "50 / 2.50 = 20. Investors are paying 20 times one year's earnings per share."),
                ("How do you compute enterprise value?", "Market cap plus debt, preferred shares and minority interests, minus cash. It is the price of buying the whole business, not just the shares."),
                ("Why is EV/EBITDA paired with enterprise value rather than market cap?", "EBITDA is profit before interest, so it belongs to both lenders and shareholders. Enterprise value also covers both, so the two match; using market cap would make heavily indebted companies look cheap."),
                ("How do you turn a peer EV/EBITDA multiple into a share price?", "Multiply the company's EBITDA by the peer multiple to get enterprise value, subtract net debt (and other claims like minority interests) to get equity value, then divide by the number of shares."),
                ("Which multiple usually fits a bank best, and why?", "Price to book. A bank's assets and liabilities are mostly financial and carried near market value, and EBITDA has no meaning when interest is the core business."),
                ("A company has a P/E of 30 and expected EPS growth of 15% a year. What is its PEG?", "30 / 15 = 2.0. A PEG near 1 is often called fair for a growth stock, but the rule is rough and ignores risk and how long growth lasts."),
                ("A cyclical steel maker trades at a P/E of 5 at the top of a boom. Is it cheap?", "Not necessarily. Peak profits make the P/E look low; when the cycle turns, earnings can fall sharply and the true P/E on normal earnings may be much higher."),
                ("What makes a good peer group?", "Companies with the same business model and industry and similar growth, margins, size and risk. Use several peers and compare against the median."),
                ("True or false: a lower multiple always means a cheaper stock.", "False. Low multiples often reflect lower growth, higher risk or temporarily inflated earnings. A multiple is cheap only after you explain why it differs from peers."),
            ],
            "calc": None,
            "links": [
                ("SEC EDGAR full-text and company search", "https://www.sec.gov/edgar/search/"),
            ],
        },
        # ------------------------------------------------------------------ dcf
        {
            "id": "dcf",
            "title": "The discounted cash flow model, step by step",
            "level": "Intermediate",
            "minutes": 12,
            "summary": "Forecast free cash flow, discount it, add a terminal value, bridge to equity and test how "
                       "sensitive the answer is.",
            "body": """
A **discounted cash flow (DCF)** model values a business as the present value of the cash it will produce.
Cash in the future is worth less than cash today, so each year's cash is divided by a discount factor.

### Step 1: forecast free cash flow

**Free cash flow to the firm (FCFF)** is the cash left after running and maintaining the business, before
paying lenders or shareholders:

`FCFF = EBIT x (1 - tax rate) + Depreciation - Capital expenditure - Increase in working capital`

Most models forecast 5 to 10 years, based on revenue growth, margins and how much the company must reinvest.

### Step 2: discount each year

Discount at the **weighted average cost of capital (WACC)**, the return demanded by both lenders and
shareholders (see the next lesson):

`PV = FCF in year t / (1 + WACC)^t`

### Step 3: terminal value

A business does not stop after year 5, so a **terminal value (TV)** captures everything after the forecast.
Two common ways:

- **Gordon growth**: `TV = FCF in final year x (1 + g) / (WACC - g)`, where g is a modest long-run growth
  rate, usually no higher than long-run nominal economic growth. g must be below WACC.
- **Exit multiple**: `TV = final-year EBITDA x an EV/EBITDA multiple`. Simple, but it imports today's market
  mood into your valuation.

The terminal value is discounted back with the final year's factor, `TV / (1 + WACC)^n`. It is often 60 to 80%
of the total, which is why its assumptions deserve the most scrutiny.

### Step 4: the equity bridge

Adding the discounted forecast and discounted terminal value gives **enterprise value**. Then:

`Equity value = Enterprise value - Debt + Cash (- minority interests, - preferred shares)`

`Value per share = Equity value / Diluted shares`

### Step 5: sensitivity

Show the answer across a grid of discount rates and terminal growth rates. If small changes move the value a
lot, your conclusion is fragile.

> Common mistake: a terminal growth rate close to the discount rate. As g approaches WACC, the terminal value
> explodes towards infinity. Cross-check the Gordon result against the exit multiple it implies.
""",
            "example": {
                "title": "Worked example: Northwind Tools",
                "body": """
Northwind Tools produced free cash flow of **100m** last year. Assumptions: growth **8%** a year for 5 years,
WACC **9%**, terminal growth **2.5%**, debt **300m**, cash **50m**, **50m** shares.

**Forecast and discount** (figures in millions):

- Year 1: FCF 108.00, factor 1.09, PV **99.08**
- Year 2: FCF 116.64, factor 1.1881, PV **98.17**
- Year 3: FCF 125.97, factor 1.2950, PV **97.27**
- Year 4: FCF 136.05, factor 1.4116, PV **96.38**
- Year 5: FCF 146.93, factor 1.5386, PV **95.50**
- Sum of PVs = **486.4**

**Terminal value (Gordon growth):** 146.93 x 1.025 / (0.09 - 0.025) = 150.60 / 0.065 = **2,317.0**.
PV = 2,317.0 / 1.5386 = **1,505.9**.

**Enterprise value** = 486.4 + 1,505.9 = **1,992.3**. The terminal value is about 76% of it.

**Equity bridge:** 1,992.3 - 300 + 50 = **1,742.3**. Per share: 1,742.3 / 50 = **34.85**.

**Exit multiple check:** if year-5 EBITDA is 220m and peers trade at 10x, TV = 2,200, PV = 2,200 / 1.5386 =
1,429.8, EV = 1,916.3, about 33.3 per share after the bridge. The two methods roughly agree.

**Sensitivity (value per share):**

- WACC 8%: 39.00 (g 2%), 42.27 (g 2.5%), 46.20 (g 3%)
- WACC 9%: 32.56, 34.85, 37.52
- WACC 10%: 27.73, 29.40, 31.32

A reasonable range is roughly 28 to 46, not a single number.
""",
            },
            "terms": [
                ("Discounted cash flow (DCF)", "A valuation that adds up the present value of a business's expected future cash flows."),
                ("Free cash flow to the firm", "Cash from operations after tax and reinvestment, available to both lenders and shareholders."),
                ("Terminal value", "The value of all cash flows beyond the explicit forecast period, captured in one number."),
                ("Gordon growth model", "Terminal value = next year's cash flow / (discount rate - growth rate), for cash flows growing at a constant rate forever."),
                ("Equity bridge", "The step from enterprise value to equity value: subtract debt and other claims, add cash."),
            ],
            "cards": [
                ("What is free cash flow to the firm?", "EBIT after tax, plus depreciation, minus capital expenditure and the increase in working capital. It is the cash available to all providers of capital before any is paid out."),
                ("Free cash flow in year 5 is 100 and grows 2% forever after. WACC is 8%. What is the terminal value at year 5?", "100 x 1.02 / (0.08 - 0.02) = 102 / 0.06 = 1,700. Remember to discount it back with the year-5 factor."),
                ("Why must terminal growth be below the discount rate?", "In the Gordon formula the denominator is WACC minus g. As g approaches WACC the value heads to infinity, and above it the formula gives nonsense. Long-run growth should also not exceed nominal economic growth."),
                ("A cash flow of 121 arrives in two years. At 10% a year, what is its present value?", "121 / 1.1^2 = 121 / 1.21 = 100."),
                ("How do you go from enterprise value to value per share?", "Subtract debt (and minority interests and preferred shares), add cash to get equity value, then divide by diluted shares outstanding."),
                ("What are the two common ways to estimate terminal value, and a weakness of each?", "Gordon growth, which is very sensitive to the growth and discount rates; and an exit multiple, which imports today's market pricing into what should be an independent valuation."),
                ("Why is the terminal value so important in most DCFs?", "It often makes up 60 to 80% of enterprise value, so its assumptions drive the answer more than the detailed yearly forecasts."),
                ("What does a sensitivity table tell you?", "How much the value changes as you vary key inputs such as WACC and terminal growth. If the range is wide, the conclusion depends heavily on assumptions you cannot know precisely."),
                ("True or false: a DCF is objective because it uses a formula.", "False. The formula is mechanical, but every input (growth, margins, discount rate, terminal growth) is a judgement. Different reasonable inputs give very different values."),
            ],
            "calc": "dcf",
            "links": [
                ("Damodaran Online (valuation data and spreadsheets)", "https://pages.stern.nyu.edu/~adamodar/"),
            ],
        },
        # ------------------------------------------------------------------ discount-rates
        {
            "id": "discount-rates",
            "title": "Discount rates: CAPM and WACC",
            "level": "Advanced",
            "minutes": 10,
            "summary": "Where the discount rate comes from: risk-free rate, equity risk premium, beta, after-tax cost "
                       "of debt and capital weights.",
            "body": """
The discount rate is the return investors demand for the risk of a cash flow. In a DCF of the whole business
it is the **weighted average cost of capital (WACC)**, which blends what shareholders and lenders require.

### Cost of equity with CAPM

The **capital asset pricing model (CAPM)** is the most common starting point:

`Cost of equity = Risk-free rate + Beta x Equity risk premium`

- **Risk-free rate**: usually the yield on a long-term government bond in the same currency as the cash
  flows, for example the 10-year Treasury for US dollar cash flows.
- **Equity risk premium (ERP)**: the extra yearly return investors demand for holding shares rather than
  safe bonds. Estimates commonly fall around 4 to 6%; they come either from historical returns or from an
  implied premium backed out of current prices. Aswath Damodaran publishes an implied ERP each month.
- **Beta**: how much a stock tends to move with the market. A beta of 1.2 means it has moved about 1.2% for
  each 1% market move. Betas measured from past prices are noisy, so many analysts use the average beta of an
  industry, adjusted for each company's debt.

CAPM is a model, not a law: tests show beta explains returns less well than the theory predicts. It survives
because it is simple and gives a consistent framework.

### Cost of debt

The cost of debt is the yield the company would pay to borrow today, not the coupon on old bonds. Interest is
usually tax deductible, so use the after-tax figure: `Cost of debt after tax = Pre-tax cost x (1 - tax rate)`.

### Putting it together

`WACC = E/V x Cost of equity + D/V x Cost of debt x (1 - tax rate)`

E and D are the **market values** of equity and debt, and V = E + D. Use market values or a target structure,
not book values.

### Why small changes matter

Because value comes from cash flows many years away, the discount rate compounds. Moving WACC by one
percentage point can change a DCF value by 15 to 20% or more, and a change in the gap between WACC and
terminal growth moves the terminal value even more.

> Rule of thumb: keep everything consistent. Nominal cash flows need a nominal discount rate, and cash flows in
> a currency need a risk-free rate and inflation from that same currency.
""",
            "example": {
                "title": "Worked example: WACC for Larkspur Logistics",
                "body": """
Inputs: 10-year government bond yield **4%**, equity risk premium **5%**, beta **1.2**, pre-tax cost of debt
**6%**, tax rate **25%**, market value of equity **800m**, debt **200m**.

1. Cost of equity = 4% + 1.2 x 5% = 4% + 6% = **10%**.
2. After-tax cost of debt = 6% x (1 - 0.25) = **4.5%**.
3. Weights: V = 800 + 200 = 1,000, so E/V = **80%** and D/V = **20%**.
4. WACC = 0.80 x 10% + 0.20 x 4.5% = 8.0% + 0.9% = **8.9%**.

Why it matters: in the Northwind Tools DCF, value per share was 34.85 at a 9% WACC, 42.27 at 8% and 29.40 at
10% (terminal growth 2.5%). One point of WACC moved the value by about 16 to 21%.
""",
            },
            "terms": [
                ("WACC", "Weighted average cost of capital: the blended return required by shareholders and lenders, weighted by market values."),
                ("CAPM", "Capital asset pricing model: cost of equity = risk-free rate + beta x equity risk premium."),
                ("Risk-free rate", "The return on a default-free asset, usually proxied by a government bond yield in the same currency."),
                ("Equity risk premium", "The extra yearly return investors demand for owning shares instead of risk-free bonds."),
                ("Beta", "A measure of how much a stock has tended to move when the overall market moves."),
                ("Cost of debt", "The yield a company would pay to borrow today; used after tax in WACC because interest is usually deductible."),
            ],
            "cards": [
                ("Risk-free rate 3%, beta 1.5, equity risk premium 5%. What is the CAPM cost of equity?", "3% + 1.5 x 5% = 3% + 7.5% = 10.5%."),
                ("Why is the cost of debt taken after tax in WACC?", "Interest is usually tax deductible, so each unit of interest costs the company less than its face amount. The after-tax cost is the pre-tax cost x (1 - tax rate)."),
                ("Equity is 600 and debt 400 at market value. Cost of equity 11%, pre-tax cost of debt 5%, tax 20%. What is WACC?", "0.6 x 11% + 0.4 x 5% x 0.8 = 6.6% + 1.6% = 8.2%."),
                ("What does a beta of 0.7 tell you?", "The stock has tended to move about 0.7% for each 1% move in the market, so CAPM gives it a cost of equity below the market average."),
                ("Should WACC weights use book values or market values?", "Market values (or a target capital structure), because the WACC represents what investors require on what their claims are worth today."),
                ("Which risk-free rate should a DCF in euros use?", "A long-term euro government bond yield (for example a highly rated euro government bond), so that the currency and inflation built into the rate match the cash flows."),
                ("Why does a one-point change in WACC move a DCF value so much?", "Most value sits in cash flows many years out, and the discount compounds each year. The terminal value is also driven by the gap between WACC and growth, so a small change in WACC changes it a lot."),
                ("True or false: CAPM is proven to explain stock returns well.", "False. Empirical tests find beta explains returns less well than the theory predicts. CAPM is used because it is simple and consistent, not because it is precise."),
            ],
            "calc": "dcf",
            "links": [
                ("Damodaran Online", "https://pages.stern.nyu.edu/~adamodar/"),
                ("Damodaran's data sets (ERP, betas by industry)", "https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html"),
                ("FRED: 10-year US Treasury yield", "https://fred.stlouisfed.org/series/DGS10"),
            ],
        },
        # ------------------------------------------------------------------ reverse-dcf
        {
            "id": "reverse-dcf",
            "title": "Reverse DCF and scenarios",
            "level": "Advanced",
            "minutes": 9,
            "summary": "Start from the price and work out what growth it assumes, then weigh bull, base and bear cases "
                       "into one expected value.",
            "body": """
A normal DCF starts with your forecasts and produces a value. A **reverse DCF** runs the other way: it takes
the current market price as given and asks *what growth or margins would the business need to deliver to
justify it?* This shifts the question from "what is it worth?", which invites false precision, to "is the
market expecting too much or too little?", which you can judge against the company's history and industry.

### How to run one

1. Start from today's enterprise value (market cap plus net debt).
2. Fix the discount rate and terminal growth at sensible levels.
3. Change one forecast driver, usually growth in free cash flow over the next 5 or 10 years, until the DCF
   value equals the market value.
4. Ask whether that implied growth is plausible. Has the company or any peer ever grown that fast for that
   long? How big would it become, and how big is its market?

### Scenarios

The future is not one number, so build a few complete stories:

- **Bear case**: what if growth stalls or margins shrink?
- **Base case**: your central, most likely view.
- **Bull case**: what if things go well?

Give each a probability and combine them:

`Expected value = Sum of (probability x scenario value)`

Scenarios force you to think about what could go wrong and show how lopsided the outcomes are. If the bear
case loses 50% and the bull case gains 30%, the stock may be unattractive even when the base case looks fine.

### Expectations investing

Michael Mauboussin and Alfred Rappaport called this approach **expectations investing**: read the expectations
built into the price, then look for reasons those expectations will be revised. You profit not from a company
being good, but from it turning out better (or worse, if you are selling) than the market already expects.

> Common mistake: making the base case your hopes and the bear case only slightly worse. A useful bear case is
> genuinely painful and still realistic.
""",
            "example": {
                "title": "Worked example: Cobalt Software",
                "body": """
Cobalt Software trades at **60** with **100m** shares and no net debt, so enterprise value is **6,000m**.
Free cash flow last year: **200m**. Assume WACC **9%** and terminal growth **2.5%**, as in a 5-year DCF.

**Reverse DCF:**

- With 0% growth for 5 years, the DCF gives about 2,828m, or 28 per share.
- With 10% growth, about 4,329m, or 43 per share.
- To reach 6,000m, free cash flow must grow about **18% a year** for five years (from 200m to about 460m),
  then 2.5% forever.

So the price assumes cash flow roughly 2.3 times bigger in five years. That is the question to research.

**Scenarios:**

- Bear (25% probability): growth fades, value **30**
- Base (50%): value **50**
- Bull (25%): value **90**

Expected value = 0.25 x 30 + 0.50 x 50 + 0.25 x 90 = 7.5 + 25 + 22.5 = **55**, slightly below the price of 60.
The market price looks more optimistic than this probability-weighted view.
""",
            },
            "terms": [
                ("Reverse DCF", "A DCF solved backwards to find the growth or margins implied by the current market price."),
                ("Implied growth", "The growth rate that makes a DCF value equal the market value."),
                ("Scenario analysis", "Valuing a company under several complete stories (such as bear, base and bull) instead of one forecast."),
                ("Probability-weighted value", "The sum of each scenario's value multiplied by its probability."),
                ("Expectations investing", "Reading the expectations implied by a price and judging whether they are likely to be revised up or down."),
            ],
            "cards": [
                ("What question does a reverse DCF answer?", "What growth (or margins) the business must deliver to justify today's price. It turns the valuation into a judgement about whether market expectations are too high or too low."),
                ("Bear 20 (30% chance), base 40 (50%), bull 70 (20%). What is the probability-weighted value?", "0.3 x 20 + 0.5 x 40 + 0.2 x 70 = 6 + 20 + 14 = 40."),
                ("A reverse DCF shows a price implies 25% yearly growth for 10 years. How would you judge it?", "Compare it with the company's own history, peers and the size of its market. Very few companies sustain 25% for a decade, so the price needs strong evidence of an unusual business."),
                ("Why build bear, base and bull cases instead of one forecast?", "Because the future is uncertain and outcomes are often lopsided. Scenarios show how much you could lose versus gain, which a single number hides."),
                ("What is the core idea of expectations investing?", "Returns come from expectations being revised, not from a company simply being good. A great company priced for perfection can still be a poor investment."),
                ("Which inputs are usually fixed in a reverse DCF, and which one is solved for?", "The discount rate and terminal growth are fixed at sensible levels, and one driver, usually near-term free cash flow growth, is changed until the DCF value matches the market value."),
                ("True or false: if your base case value is above the price, the stock is attractive.", "Not necessarily. If the bear case is severe and fairly likely, the probability-weighted value can still be below the price."),
            ],
            "calc": "dcf",
            "links": [],
        },
        # ------------------------------------------------------------------ moats
        {
            "id": "moats",
            "title": "Moats and business quality",
            "level": "Intermediate",
            "minutes": 9,
            "summary": "What protects high returns from competition, why ROIC above WACC is the real test, and how "
                       "management's capital allocation adds or destroys value.",
            "body": """
High profits attract competitors, who usually push returns back down. A **moat** is a lasting advantage that
stops this from happening. The word is Warren Buffett's; Morningstar later organised moats into five sources.

### The five common sources

- **Network effects**: the product becomes more valuable as more people use it (marketplaces, payment
  networks, exchanges).
- **Switching costs**: changing supplier is costly, risky or slow for the customer (business software built
  into daily work, banking relationships).
- **Cost advantages**: producing more cheaply than rivals through scale, process or location (a large
  low-cost retailer, a mine with unusually rich ore).
- **Intangible assets**: brands that let a company charge more, patents and licences that block rivals.
- **Efficient scale**: a market that only has room for one or a few profitable players, so newcomers would
  ruin returns for everyone (a regional pipeline, an airport).

### The numbers test: ROIC versus WACC

A moat should show up in the numbers. **Return on invested capital (ROIC)** measures how much after-tax
operating profit a company earns on the money tied up in the business:

`ROIC = NOPAT / Invested capital`, where `NOPAT = EBIT x (1 - tax rate)`

A company creates value only when ROIC is above its WACC. Growth with ROIC below WACC destroys value, however
exciting it looks. Research on large groups of companies finds that high returns tend to fade towards average
over time; a real moat is what slows that fade. Look for ROIC that has stayed well above WACC through a full
economic cycle, not just a good year or two.

### Management and capital allocation

Managers decide what to do with the cash: reinvest, buy other companies, pay down debt, pay dividends or buy
back shares. Good capital allocators reinvest only where returns beat the cost of capital, avoid overpaying
for acquisitions, and buy back shares when they are cheap rather than when profits are high. Their pay should
reward long-term per-share value, not just size.

> Rule of thumb: a story about a moat is not a moat. If returns on capital are ordinary, the advantage is
> either weak or not yet proven.
""",
            "example": {
                "title": "Worked example: two growth plans",
                "body": """
**Kestrel Payments**: EBIT **150m**, tax rate **25%**, invested capital **750m**, WACC **9%**.

- NOPAT = 150 x (1 - 0.25) = **112.5m**.
- ROIC = 112.5 / 750 = **15%**.
- Economic profit = (ROIC - WACC) x Invested capital = (15% - 9%) x 750 = **45m** a year of value created.

**Dunmore Retail**: NOPAT **52.5m** on invested capital **750m**, so ROIC = **7%**, also WACC 9%.

- Economic profit = (7% - 9%) x 750 = **minus 15m** a year.

Now each invests a further **100m** at the same return:

- Kestrel adds 100 x (15% - 9%) = 6m of economic profit a year: growth creates value.
- Dunmore adds 100 x (7% - 9%) = minus 2m a year: growth destroys value, even though profits rise by 7m.
""",
            },
            "terms": [
                ("Moat", "A lasting competitive advantage that protects a company's returns from competitors."),
                ("Network effect", "When a product becomes more valuable to each user as more people use it."),
                ("Switching costs", "The money, time or risk a customer faces in changing to a competitor."),
                ("Efficient scale", "A market only large enough for one or a few profitable firms, which deters new entrants."),
                ("ROIC", "Return on invested capital: after-tax operating profit (NOPAT) divided by the capital tied up in the business."),
                ("Capital allocation", "How management uses the company's cash: reinvestment, acquisitions, debt repayment, dividends and buybacks."),
            ],
            "cards": [
                ("What are the five common sources of a moat?", "Network effects, switching costs, cost advantages, intangible assets (brands, patents, licences) and efficient scale."),
                ("EBIT 200, tax rate 25%, invested capital 1,000. What is ROIC?", "NOPAT = 200 x 0.75 = 150, so ROIC = 150 / 1,000 = 15%."),
                ("Why does growth destroy value when ROIC is below WACC?", "Each new unit of capital earns less than investors require for it, so the more the company invests, the more value it gives away, even though reported profits rise."),
                ("How should a moat show up in a company's numbers?", "As ROIC staying well above WACC over many years and through a full cycle, because a moat slows the usual fading of high returns towards average."),
                ("Give an example of switching costs.", "Business software built into a company's daily processes: moving to a rival means retraining staff, migrating data and risking disruption, so customers rarely leave."),
                ("What is efficient scale?", "A market only big enough for one or a few profitable players, such as a regional pipeline, so a new entrant would push returns below the cost of capital for everyone."),
                ("What marks a good capital allocator?", "Reinvesting only where returns beat the cost of capital, not overpaying for acquisitions, and buying back shares when they are cheap rather than when profits are high."),
                ("True or false: a famous brand is always a moat.", "False. A brand is a moat only if it lets the company charge more or sell more than rivals in a way that shows up as lasting high returns on capital."),
            ],
            "calc": None,
            "links": [],
        },
        # ------------------------------------------------------------------ special-cases
        {
            "id": "special-cases",
            "title": "Valuing the awkward ones",
            "level": "Advanced",
            "minutes": 11,
            "summary": "Banks, insurers, REITs, cyclicals, loss-making growth companies and conglomerates: why the "
                       "standard tools break and what professionals use instead.",
            "body": """
EV/EBITDA and free cash flow to the firm assume that debt is financing and interest is a cost of funding. For
some companies that is false, or the numbers are temporarily meaningless. Each needs its own tools.

### Banks and insurers

For a bank, borrowing (deposits) is the raw material and interest is the main revenue, so enterprise value and
EBITDA make no sense. Analysts value the **equity** directly, mostly with **price to book (P/B)** and
**return on equity (ROE)**. A bank that earns more on its equity than shareholders require deserves to trade
above book value:

`Justified P/B = (ROE - g) / (Cost of equity - g)`

Insurers are also valued on book value and ROE, with attention to the combined ratio (claims plus expenses as a
share of premiums; under 100% means underwriting is profitable) and to how much the business earns by investing
premiums before claims are paid.

### REITs

Real estate investment trusts must charge depreciation on buildings, which often hold or gain value, so net
income understates cash earnings. The industry uses **funds from operations (FFO)**:

`FFO = Net income + Real estate depreciation and amortisation - Gains on property sales`

**Adjusted FFO (AFFO)** goes further by subtracting recurring maintenance spending and smoothing accounting
rent effects. Investors compare price to FFO or AFFO and look at the value of the properties (net asset value).

### Cyclicals

Miners, steel makers, chemicals and car makers swing from boom to bust. A P/E on peak profits looks cheap, a
P/E on trough profits looks expensive. Use **normalised earnings**: average margins across a full cycle applied
to today's revenue or capacity.

### Loss-making growth companies

With no profit yet, work backwards from a mature future: forecast revenue, assume a margin similar to mature
peers, value that future business and discount it back, allowing for the chance it fails and for future
share dilution.

### Sum of the parts

A conglomerate with unrelated divisions is valued division by division, each with the multiple of its own
peers, then corporate costs and net debt are subtracted.

> Common mistake: using EV/EBITDA for a bank or a P/E on peak earnings for a miner. Choose the tool that fits
> how the business actually makes money.
""",
            "example": {
                "title": "Worked example: a bank, a REIT and a conglomerate",
                "body": """
**Fernhill Bank**: ROE **12%**, cost of equity **10%**, long-run growth **3%**, book value per share **40**.

- Justified P/B = (12% - 3%) / (10% - 3%) = 9 / 7 = **1.29x**.
- Justified price = 1.29 x 40 = about **51**.

**Granite Shelf REIT**: net income **80m**, real estate depreciation **60m**, gain on a property sale **10m**,
maintenance spending **25m**, straight-line rent adjustment **5m**, **50m** units, price **30**.

- FFO = 80 + 60 - 10 = **130m**, or 2.60 per unit. Price / FFO = 30 / 2.60 = **11.5x**.
- AFFO = 130 - 25 - 5 = **100m**, or 2.00 per unit. Price / AFFO = 30 / 2.00 = **15x**.

**Ashgrove Group** (sum of the parts): engineering EBITDA **100m** at a peer **8x** = 800m; software EBITDA
**50m** at **15x** = 750m. Corporate costs of 10m a year at 8x = minus 80m. Enterprise value = 800 + 750 - 80
= **1,470m**. Less net debt **270m** = equity **1,200m**, or **24** per share on 50m shares.
""",
            },
            "terms": [
                ("Return on equity (ROE)", "Net income divided by shareholders' equity: the return a company earns on its owners' capital."),
                ("Funds from operations (FFO)", "A REIT's net income plus real estate depreciation, minus gains on property sales."),
                ("Adjusted FFO (AFFO)", "FFO minus recurring maintenance spending and adjusted for accounting rent effects, closer to distributable cash."),
                ("Normalised earnings", "Profit estimated on average conditions across a full business cycle rather than the current year."),
                ("Sum of the parts", "Valuing each division separately with its own peers' multiples, then subtracting corporate costs and net debt."),
                ("Combined ratio", "An insurer's claims plus expenses as a share of premiums; below 100% means underwriting is profitable."),
            ],
            "cards": [
                ("Why don't analysts use EV/EBITDA to value a bank?", "For a bank, deposits and borrowing are the raw material and interest is the main revenue, so debt is not just financing and EBITDA has no meaning. Banks are valued on equity measures like P/B and ROE."),
                ("A bank earns ROE of 15%, cost of equity 10%, growth 4%. What P/B is justified?", "(15% - 4%) / (10% - 4%) = 11 / 6 = about 1.83 times book value."),
                ("A bank's ROE equals its cost of equity. What P/B would you expect?", "About 1.0. If the bank earns exactly what shareholders require, it creates no extra value, so it should trade near book value."),
                ("How do you compute a REIT's FFO?", "Net income plus real estate depreciation and amortisation, minus gains on property sales. It adds back depreciation because buildings often hold their value."),
                ("REIT net income 50, real estate depreciation 40, gain on sale 5. What is FFO?", "50 + 40 - 5 = 85."),
                ("How should you value a cyclical company at the top of its cycle?", "On normalised earnings: average margins across a full cycle applied to current revenue or capacity, because peak profits make the P/E look misleadingly low."),
                ("How do you value a growth company that is still losing money?", "Forecast revenue to a mature year, apply a margin similar to mature peers, value that business, discount it back, and allow for the risk of failure and for future share dilution."),
                ("What is a sum-of-the-parts valuation?", "Valuing each division with the multiples of its own peers, adding them up, then subtracting capitalised corporate costs and net debt. It fits conglomerates with unrelated businesses."),
                ("What does an insurer's combined ratio of 95% mean?", "Claims plus expenses were 95% of premiums, so underwriting itself made a profit of about 5% of premiums, before any investment income."),
            ],
            "calc": None,
            "links": [],
        },
    ],
}
