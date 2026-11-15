"""Track: Reading a company. Content for Master Investor (see tools/CONTENT_BRIEF.md)."""

TRACK = {
    "id": "statements",
    "title": "Reading a company",
    "level": "Intermediate",
    "blurb": "Read the three financial statements, work out the ratios that matter, find your way around an annual "
             "report and earnings call, and spot the warning signs of low-quality earnings.",
    "lessons": [
        # ------------------------------------------------------------------
        {
            "id": "income-statement",
            "title": "The income statement",
            "level": "Beginner",
            "minutes": 8,
            "summary": "How a company gets from revenue to net income, what the margins tell you, and how to read EPS and one-off items.",
            "body": """
The **income statement** (also called the profit and loss account, or P&L) shows what a company earned and spent over a period, usually a quarter or a year. It reads from top to bottom, peeling away costs until only profit is left.

### From revenue to net income

1. **Revenue:** what customers paid for goods and services in the period.
2. minus **cost of goods sold** (direct costs of making the product) gives **gross profit**.
3. minus **operating expenses** (selling, general and administrative costs, research and development) gives **operating income**, often close to EBIT (earnings before interest and tax).
4. minus interest, plus or minus other items, gives **pre-tax income**.
5. minus income tax gives **net income**, the bottom line that belongs to shareholders.

### Margins

Dividing each profit line by revenue turns raw numbers into margins you can compare across years and companies.

`gross margin = gross profit / revenue`
`operating margin = operating income / revenue`
`net margin = net income / revenue`

Gross margin shows pricing power and production cost. Operating margin shows how efficiently the whole business runs. Net margin also reflects debt and tax. Compare margins within an industry: a software firm and a supermarket have very different normal levels.

### Earnings per share

`EPS = net income / weighted average shares outstanding`

**Basic EPS** uses the shares actually outstanding. **Diluted EPS** adds shares that could be created from stock options, restricted shares and convertible bonds. Diluted is the more conservative and usually the more useful figure.

### One-off items

Restructuring charges, asset write-downs, lawsuit settlements and gains on selling a business can swing a single year. Strip them out to see the underlying trend, but be suspicious of a company that has "one-off" charges every year: then they are a normal cost of doing business.

> Common mistake: judging a company on net income alone. Look at revenue growth and operating margin over several years; the bottom line is easier to bend.
""",
            "example": {
                "title": "Worked example: Northwind Tools, one year (millions)",
                "body": """
- Revenue: **500**
- Cost of goods sold: 300, so gross profit = **200** (gross margin 200 / 500 = **40%**)
- Selling, general and administrative: 80
- Research and development: 30
- Restructuring charge (one-off): 10
- Operating income: 200 - 80 - 30 - 10 = **80** (operating margin **16%**)
- Interest expense: 10, so pre-tax income = **70**
- Tax at 25%: 17.5, so net income = **52.5** (net margin **10.5%**)

**EPS.** Weighted average shares: 50 million basic, 52.5 million diluted.

- Basic EPS = 52.5 / 50 = **1.05**
- Diluted EPS = 52.5 / 52.5 = **1.00**

**Underlying view.** Without the one-off restructuring charge, operating income would be 90, an underlying operating margin of 90 / 500 = **18%**. If Northwind books a "restructuring" charge every year, the honest margin is 16%, not 18%.
""",
            },
            "terms": [
                ("Income statement", "The financial statement showing revenue, costs and profit over a period; also called the profit and loss account."),
                ("Gross profit", "Revenue minus the direct cost of producing the goods or services sold."),
                ("Operating income", "Profit from the core business after all operating expenses, before interest and tax."),
                ("Net income", "The profit left for shareholders after all costs, interest and tax."),
                ("EPS", "Earnings per share: net income divided by the weighted average number of shares outstanding."),
                ("Diluted EPS", "EPS that also counts shares that could be created from options, restricted shares and convertible securities."),
            ],
            "cards": [
                ("Revenue is 200, gross profit 80 and operating income 30. What are the gross and operating margins?",
                 "Gross margin = 80 / 200 = 40%. Operating margin = 30 / 200 = 15%."),
                ("What is the difference between basic and diluted EPS?",
                 "Basic EPS divides net income by shares outstanding. Diluted EPS also counts shares that could be created from options, restricted stock and convertibles, so it is lower or equal and more conservative."),
                ("Net income is 40 million, basic shares 20 million and diluted shares 25 million. What are basic and diluted EPS?",
                 "Basic EPS = 40 / 20 = 2.00. Diluted EPS = 40 / 25 = 1.60."),
                ("What does gross margin tell you about a business?",
                 "How much of each unit of revenue is left after the direct cost of making the product. A high, stable gross margin often signals pricing power."),
                ("A company reports a 'one-off' restructuring charge five years running. How should you treat it?",
                 "As a recurring cost of doing business. Include it when judging margins, because charges that repeat every year are not really one-off."),
                ("List the main steps from revenue to net income.",
                 "Revenue minus cost of goods sold gives gross profit; minus operating expenses gives operating income; minus interest and other items gives pre-tax income; minus tax gives net income."),
                ("True or false: a supermarket with a 3% operating margin must be a worse business than a software firm with a 30% margin.",
                 "False. Normal margins differ hugely by industry. A supermarket turns its assets over many times a year, so compare margins against peers and the company's own history."),
            ],
            "calc": None,
            "links": [
                ("SEC EDGAR company filings search", "https://www.sec.gov/edgar/search/"),
            ],
        },
        # ------------------------------------------------------------------
        {
            "id": "balance-sheet",
            "title": "The balance sheet",
            "level": "Beginner",
            "minutes": 8,
            "summary": "What a company owns and owes at one moment, working capital, debt, book value and goodwill.",
            "body": """
The **balance sheet** is a snapshot of what a company owns and owes on a single date, usually the last day of its financial year or quarter. It always balances:

`assets = liabilities + equity`

Everything the company owns was paid for either with borrowed money and unpaid bills (liabilities) or with the owners' money and retained profits (equity).

### Assets

- **Current assets** turn into cash within a year: cash, **receivables** (money customers owe), inventory.
- **Non-current assets** last longer: property, plant and equipment, intangible assets such as patents, and **goodwill**.

**Goodwill** appears only after an acquisition: it is the price paid for a business above the fair value of its identifiable net assets. It cannot be sold on its own. If the acquired business disappoints, goodwill is written down, which tells you the company overpaid.

### Liabilities

- **Current liabilities** fall due within a year: **payables** (bills owed to suppliers), short-term debt, taxes due.
- **Non-current liabilities** include long-term debt, lease obligations and pension deficits.

### Working capital and debt

`working capital = current assets - current liabilities`

Positive working capital means short-term assets cover short-term bills. Many analysts also look at **net debt**:

`net debt = total debt - cash`

A company with large net debt and falling profits can get into trouble quickly; one with net cash has room to survive a bad year.

### Book value

**Equity**, also called **book value**, is what would be left for shareholders if all assets were sold at their balance sheet values and all liabilities paid. Book value per share is equity divided by shares outstanding. **Tangible book value** subtracts goodwill and other intangibles, a stricter measure.

Balance sheet values are mostly historical cost, not market value. A brand built over a century may not appear at all, while a factory may be carried well above what it could be sold for.

> Rule of thumb: read the balance sheet before the income statement. Profits can recover; a company that runs out of cash cannot.
""",
            "example": {
                "title": "Worked example: Northwind Tools balance sheet (millions)",
                "body": """
**Assets**

- Cash 40, receivables 70, inventory 60: current assets **170**
- Property, plant and equipment 200, goodwill 80
- Total assets: 170 + 200 + 80 = **450**

**Liabilities and equity**

- Payables 50, short-term debt 30: current liabilities **80**
- Long-term debt **120**
- Total liabilities: 80 + 120 = **200**
- Equity: 450 - 200 = **250**

**Check:** 200 + 250 = 450. It balances.

**Ratios.**

- Working capital = 170 - 80 = **90**
- Total debt = 30 + 120 = 150; net debt = 150 - 40 = **110**
- Debt to equity = 150 / 250 = **0.6**
- Book value per share (50 million shares) = 250 / 50 = **5.00**
- Tangible book value = 250 - 80 = 170, or **3.40** per share

If the shares trade at 15, the market values Northwind at three times its book value: investors expect its assets to earn well above their accounting cost.
""",
            },
            "terms": [
                ("Balance sheet", "A snapshot of a company's assets, liabilities and equity on a single date."),
                ("Working capital", "Current assets minus current liabilities: the short-term cushion for paying bills."),
                ("Net debt", "Total borrowings minus cash; negative net debt means the company holds more cash than debt."),
                ("Book value", "Shareholders' equity on the balance sheet: assets minus liabilities."),
                ("Goodwill", "The amount paid for an acquired business above the fair value of its identifiable net assets."),
                ("Receivables", "Money customers owe the company for goods or services already delivered."),
            ],
            "cards": [
                ("Write the balance sheet equation and explain why it always holds.",
                 "Assets = liabilities + equity. Everything a company owns was financed either by what it owes (liabilities) or by owners' money and retained profits (equity)."),
                ("Current assets are 150 and current liabilities 100. What is working capital?",
                 "150 - 100 = 50. Short-term assets cover short-term bills with 50 to spare."),
                ("A company has debt of 300 and cash of 50. What is its net debt?",
                 "300 - 50 = 250."),
                ("What is goodwill, and what does a large goodwill write-down tell you?",
                 "Goodwill is the premium paid for an acquisition above the fair value of the target's identifiable net assets. A large write-down means the acquisition is worth less than was paid: the company overpaid."),
                ("Equity is 400 million and there are 80 million shares. What is book value per share?",
                 "400 / 80 = 5.00 per share."),
                ("True or false: the balance sheet shows what a company's assets could be sold for today.",
                 "False. Most assets are carried at historical cost less depreciation. Many valuable things, such as a home-grown brand, may not appear at all."),
                ("Why might you prefer tangible book value to book value?",
                 "Tangible book value removes goodwill and other intangibles, which often cannot be sold separately and may be worth much less in a crisis. It is a stricter measure of asset backing."),
            ],
            "calc": None,
            "links": [],
        },
        # ------------------------------------------------------------------
        {
            "id": "cash-flow-statement",
            "title": "The cash flow statement",
            "level": "Intermediate",
            "minutes": 8,
            "summary": "Operating, investing and financing cash flows, free cash flow, and why profit is not the same as cash.",
            "body": """
The **cash flow statement** shows the actual cash that came in and went out over a period. It is the hardest statement to dress up, which makes it the best check on the other two.

### Why profit is not cash

The income statement uses **accrual accounting**: revenue is recorded when it is earned and costs when they are incurred, not when cash moves. So:

- A sale on 60-day credit counts as revenue now, but the cash arrives later (receivables rise).
- **Depreciation** spreads the cost of equipment over its life, reducing profit every year, but the cash left when the equipment was bought.
- Building up inventory uses cash but does not touch profit until the goods are sold.

A company can report profits and still run out of cash.

### The three sections

- **Operating activities:** starts from net income, adds back non-cash charges such as depreciation, amortisation and stock-based compensation, then adjusts for changes in working capital. Rising receivables or inventory reduce cash; rising payables increase it.
- **Investing activities:** spending on property and equipment (**capital expenditure**, or capex), acquisitions, and buying or selling investments.
- **Financing activities:** borrowing and repaying debt, issuing or buying back shares, and paying dividends.

The three totals add up to the change in cash on the balance sheet.

### Free cash flow

`free cash flow = cash from operations - capital expenditure`

**Free cash flow** is the cash a business generates after keeping its asset base going and growing. It is what is truly available to pay dividends, buy back shares, pay down debt or make acquisitions. Definitions vary: some analysts subtract only maintenance capex, and some companies publish their own versions, so check what is included.

### Reading the pattern

A healthy mature company usually shows positive operating cash flow, negative investing cash flow and negative financing cash flow (returning cash to owners and lenders). A young company may burn cash in operations and fund it by raising money in financing.

> Rule of thumb: over several years, cash from operations should be close to or above net income. A persistent gap where profit runs ahead of cash deserves a hard look.
""",
            "example": {
                "title": "Worked example: Northwind Tools cash flow (millions)",
                "body": """
**Operating activities**

- Net income: 52.5
- Add depreciation and amortisation: 25
- Add stock-based compensation: 5
- Receivables rose by 10: minus 10
- Inventory rose by 5: minus 5
- Payables rose by 4: plus 4
- Cash from operations: 52.5 + 25 + 5 - 10 - 5 + 4 = **71.5**

**Investing activities**

- Capital expenditure: minus 35
- Small acquisition: minus 20
- Total: **minus 55**

**Financing activities**

- Dividends paid: minus 15
- Debt repaid: minus 10
- Shares bought back: minus 5
- Total: **minus 30**

**Change in cash:** 71.5 - 55 - 30 = **minus 13.5**. Cash fell from 53.5 to 40.

**Free cash flow:** 71.5 - 35 = **36.5**. Northwind paid out 15 + 5 = 20 to shareholders and repaid 10 of debt, all covered by free cash flow, but the acquisition pushed total spending above what the business generated, so cash fell.
""",
            },
            "terms": [
                ("Cash flow statement", "The statement showing cash coming in and going out, split into operating, investing and financing activities."),
                ("Accrual accounting", "Recording revenue when earned and costs when incurred, rather than when cash changes hands."),
                ("Capital expenditure", "Cash spent on long-lived assets such as buildings, machines and equipment; often called capex."),
                ("Free cash flow", "Cash from operations minus capital expenditure: cash available for owners, lenders and acquisitions."),
                ("Depreciation", "Spreading the cost of a long-lived asset over its useful life as a yearly non-cash expense."),
            ],
            "cards": [
                ("What is free cash flow and how is it usually calculated?",
                 "The cash a business generates after investing in its assets: cash from operations minus capital expenditure. It is what is available for dividends, buybacks, debt repayment and acquisitions."),
                ("Cash from operations is 120 and capex is 45. What is free cash flow?",
                 "120 - 45 = 75."),
                ("Why is depreciation added back in the operating cash flow section?",
                 "It reduces profit but involves no cash leaving in the period; the cash went out when the asset was bought, and that appears in investing activities as capex."),
                ("Receivables rise by 30 in a year. What does that do to operating cash flow, and why?",
                 "It lowers operating cash flow by 30. Those sales count as revenue and profit, but customers have not paid yet, so the cash has not arrived."),
                ("Name the three sections of the cash flow statement.",
                 "Operating activities (cash from running the business), investing activities (capex, acquisitions, investments) and financing activities (debt, share issues and buybacks, dividends)."),
                ("A company's profits grow but operating cash flow falls three years running. What should you suspect?",
                 "Profits may be running ahead of reality: receivables or inventory piling up, aggressive revenue recognition, or capitalised costs. Look at working capital changes and the notes."),
                ("True or false: a profitable company cannot run out of cash.",
                 "False. Profit follows accrual rules. Fast growth tied up in receivables and inventory, or heavy capex and debt repayments, can drain cash even while profits are reported."),
                ("What does a typical mature, healthy company's cash flow pattern look like?",
                 "Positive operating cash flow, negative investing cash flow (capex) and negative financing cash flow (dividends, buybacks, debt repayment)."),
            ],
            "calc": "dcf",
            "links": [],
        },
        # ------------------------------------------------------------------
        {
            "id": "key-ratios",
            "title": "The ratios that matter",
            "level": "Intermediate",
            "minutes": 10,
            "summary": "Returns on equity, assets and capital, leverage and liquidity ratios, asset turnover, and the DuPont breakdown of ROE.",
            "body": """
Ratios turn the statements into numbers you can compare across years and against peers. No single ratio tells the whole story; read them as a set.

### Profitability and returns

Margins (gross, operating, net) show how much of each unit of revenue becomes profit. Return ratios show how much profit the business earns on the money tied up in it:

`ROE = net income / shareholders' equity`
`ROA = net income / total assets`
`ROIC = NOPAT / invested capital`

**NOPAT** (net operating profit after tax) is operating income x (1 - tax rate). **Invested capital** is usually equity plus debt minus cash. ROIC is the cleanest measure of business quality because it ignores how the company is financed. A company creates value when ROIC is above its cost of capital, the return investors require.

Many analysts use the average of opening and closing balance sheet figures, since profit is earned across the year.

### Efficiency

`asset turnover = revenue / total assets`

A supermarket might turn its assets over two or three times a year on thin margins; a utility well under once on fat margins.

### Leverage and solvency

- **Net debt / EBITDA:** years of EBITDA (earnings before interest, tax, depreciation and amortisation) needed to pay off net debt. Below about 2 is usually seen as comfortable for an ordinary business; much above 3 to 4 starts to worry lenders, though norms vary by industry.
- **Interest cover:** EBIT / interest expense. How many times operating profit covers interest. Low single digits leaves little room for a bad year.

### Liquidity

`current ratio = current assets / current liabilities`

Above 1 means short-term assets exceed short-term bills, though normal levels vary by industry.

### DuPont: what drives ROE

`ROE = net margin x asset turnover x equity multiplier`

where the **equity multiplier** is total assets / equity. The three terms multiply back to net income / equity. DuPont shows whether a high ROE comes from strong margins, efficient use of assets, or simply from debt. Two firms with a 20% ROE can be very different businesses.

> Common mistake: admiring a high ROE without checking leverage. Debt raises ROE in good years and magnifies losses in bad ones.
""",
            "example": {
                "title": "Worked example: Northwind Tools ratios",
                "body": """
From the earlier statements (millions): revenue 500, operating income 80, D&A 25, interest 10, tax rate 25%, net income 52.5, total assets 450, equity 250, debt 150, cash 40, current assets 170, current liabilities 80. End-of-year balances are used for simplicity.

- Net margin = 52.5 / 500 = **10.5%**
- ROE = 52.5 / 250 = **21.0%**
- ROA = 52.5 / 450 = **11.7%**
- NOPAT = 80 x (1 - 0.25) = 60; invested capital = 250 + 150 - 40 = 360; ROIC = 60 / 360 = **16.7%**
- Asset turnover = 500 / 450 = **1.11**
- EBITDA = 80 + 25 = 105; net debt = 110; net debt / EBITDA = 110 / 105 = **1.05x**
- Interest cover = 80 / 10 = **8.0x**
- Current ratio = 170 / 80 = **2.13**

**DuPont check:** equity multiplier = 450 / 250 = 1.8. ROE = 10.5% x 1.111 x 1.8 = **21.0%**, matching the direct calculation.

**Reading it.** Moderate debt, comfortable interest cover and a solid ROIC: Northwind's 21% ROE comes mostly from decent margins and asset use, with leverage adding a modest boost.
""",
            },
            "terms": [
                ("ROE", "Return on equity: net income divided by shareholders' equity."),
                ("ROIC", "Return on invested capital: after-tax operating profit divided by the debt and equity capital used in the business."),
                ("EBITDA", "Earnings before interest, tax, depreciation and amortisation: a rough measure of operating cash earnings."),
                ("Interest cover", "Operating profit (EBIT) divided by interest expense: how many times profit covers interest payments."),
                ("Asset turnover", "Revenue divided by total assets: how much sales the company generates from each unit of assets."),
                ("DuPont analysis", "Breaking ROE into net margin, asset turnover and the equity multiplier to see what drives it."),
            ],
            "cards": [
                ("Net income is 30 and shareholders' equity is 200. What is ROE?",
                 "30 / 200 = 15%."),
                ("Write the three-part DuPont formula for ROE.",
                 "ROE = net margin x asset turnover x equity multiplier, that is (net income / revenue) x (revenue / assets) x (assets / equity)."),
                ("A firm has a 5% net margin, asset turnover of 2 and an equity multiplier of 3. What is its ROE, and what drives it?",
                 "5% x 2 x 3 = 30%. Much of that comes from leverage (the multiplier of 3), so the ROE is riskier than it looks."),
                ("Why is ROIC often preferred to ROE for judging business quality?",
                 "ROIC measures operating profit on all the capital used, debt and equity, so it is not inflated by borrowing. ROE can be pushed up simply by adding debt."),
                ("Debt is 300, cash 50 and EBITDA 100. What is net debt to EBITDA?",
                 "(300 - 50) / 100 = 2.5x: it would take about two and a half years of EBITDA to pay off net debt."),
                ("EBIT is 60 and interest expense is 15. What is interest cover, and is it comfortable?",
                 "60 / 15 = 4x. Workable, but a sharp fall in profit would quickly squeeze it; many analysts like to see higher cover for cyclical businesses."),
                ("How do you calculate NOPAT and invested capital for ROIC?",
                 "NOPAT = operating income x (1 - tax rate). Invested capital is usually equity plus debt minus cash. ROIC = NOPAT / invested capital."),
                ("True or false: a current ratio below 1 always means a company is in trouble.",
                 "False. Some businesses, such as supermarkets, collect cash from customers before paying suppliers and run safely below 1. Compare with peers and look at cash flow."),
            ],
            "calc": None,
            "links": [
                ("Aswath Damodaran: data by industry", "https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datacurrent.html"),
            ],
        },
        # ------------------------------------------------------------------
        {
            "id": "annual-report",
            "title": "Reading an annual report and earnings call",
            "level": "Intermediate",
            "minutes": 9,
            "summary": "Where to find what matters in a 10-K or annual report, how to read the notes and segments, and what to listen for on calls.",
            "body": """
The annual report is the most complete, legally checked account a company gives of itself. In the United States the main filing is the **10-K**, with quarterly **10-Q** reports and **8-K** filings for major events, all free on the SEC's EDGAR system. Companies elsewhere publish an annual report, often under IFRS accounting standards, on their own investor pages and with their national regulator.

### The sections that matter

- **Business:** what the company sells, to whom, and who it competes with.
- **Risk factors:** the dangers the company itself lists. Much is boilerplate, so look for new risks and changes from last year.
- **MD&A** (management's discussion and analysis): management explains the results, the drivers behind them, liquidity and capital spending. Watch which numbers they emphasise and which they skip.
- **Financial statements and notes:** the audited numbers, plus the auditor's report.

### Read the notes

The **notes** to the accounts explain how the numbers were built: revenue recognition policies, debt maturities and interest rates, lease and pension obligations, stock-based compensation, lawsuits and other contingencies. Many surprises in the headline numbers were visible in the notes beforehand. Check that the auditor's opinion is unqualified (clean).

### Segments

Large companies report results by **segment**, such as business line or region. Segment data shows which parts actually earn the money. A fast-growing segment can hide a shrinking core, and a company-wide margin can mix a very profitable unit with a loss-maker.

### Guidance and earnings calls

Many companies give **guidance**: a forecast range for next period's revenue or earnings. Track it against what they later deliver; a habit of missing, or of beating only lowered targets, tells you about management credibility.

On the **earnings call**, management presents results and then takes analysts' questions. The questions are often more revealing than the script. Listen for:

- changes in wording from earlier calls, and topics that quietly disappear
- vague or evasive answers to direct questions
- new non-standard metrics
- what management says about demand, pricing, costs and cash

> Rule of thumb: read this year's risk factors and accounting policies side by side with last year's. What changed often matters more than what is there.
""",
            "example": {
                "title": "Worked example: Northwind's segments and guidance",
                "body": """
Northwind Tools (fictional) reports two segments (millions):

- **Hand tools:** revenue 350, operating income 70, margin 70 / 350 = **20%**
- **Software:** revenue 150, operating income 10, margin 10 / 150 = **6.7%**
- Group: revenue 500, operating income 80, margin **16%**

Last year hand tools had revenue 370 and software 100. Group revenue grew from 470 to 500, a **6.4%** rise, which looks healthy. But hand tools, which earns most of the profit, shrank 350 / 370 - 1 = **minus 5.4%**, while software grew **50%** at a thin margin.

**Guidance.** Management guides next year's revenue to 520 to 540: growth of 520 / 500 - 1 = **4%** to 540 / 500 - 1 = **8%**. Over the past three years Northwind guided to the midpoint and delivered 2%, 3% and 1% below it.

**What to ask on the call:** why is the core segment shrinking, when will software margins improve, and why should this year's guidance be more reliable than the last three?
""",
            },
            "terms": [
                ("10-K", "The detailed annual report US public companies must file with the SEC, including audited financial statements."),
                ("MD&A", "Management's discussion and analysis: the section where management explains results, trends, liquidity and plans."),
                ("Risk factors", "The section of an annual report listing the main risks the company believes it faces."),
                ("Notes to the accounts", "The detailed disclosures explaining accounting policies and the items behind the financial statement figures."),
                ("Segment reporting", "Results broken down by business line or region, showing which parts of the company earn the money."),
                ("Guidance", "A company's own forecast range for revenue, earnings or other figures for a coming period."),
            ],
            "cards": [
                ("Which sections of a 10-K should you read first, and why?",
                 "Business (what the company does), risk factors (what could go wrong), MD&A (management's explanation of results) and the financial statements with their notes (the audited numbers and how they were built)."),
                ("Why compare this year's risk factors with last year's?",
                 "Much of the section is boilerplate, so new risks, removed risks and changed wording are the real signal about what management now worries about."),
                ("What kind of information is found in the notes to the accounts?",
                 "Accounting policies such as revenue recognition, debt maturities and rates, leases, pensions, stock-based compensation, segment data, lawsuits and other contingencies."),
                ("Group revenue grows 6% but the most profitable segment shrinks 5%. Why does that matter?",
                 "The headline growth is coming from lower-margin parts of the business, so profits can stagnate or fall even as revenue rises. Segment data reveals what the group figure hides."),
                ("What is guidance, and how can it help you judge management?",
                 "A company's forecast range for a coming period. Comparing past guidance with actual results shows whether management is realistic, conservative or habitually over-optimistic."),
                ("On an earnings call, why are analysts' questions often more useful than the prepared remarks?",
                 "The remarks are scripted to show the company well. Questions force answers on specific issues, and evasive or vague replies to direct questions are themselves informative."),
                ("What are 10-Q and 8-K filings?",
                 "A 10-Q is a US company's quarterly report, with unaudited financial statements. An 8-K reports major events between regular reports, such as an acquisition, a change of auditor or a leadership change."),
                ("True or false: an unqualified audit opinion means the company is a good investment.",
                 "False. A clean opinion means the auditor found the statements fairly presented under the accounting rules. It says nothing about whether the business is good or the shares fairly priced."),
            ],
            "calc": None,
            "links": [
                ("SEC EDGAR company filings search", "https://www.sec.gov/edgar/search/"),
                ("Investor.gov: How to read a 10-K", "https://www.investor.gov/introduction-investing/getting-started/researching-investments/how-read-10-k"),
            ],
        },
        # ------------------------------------------------------------------
        {
            "id": "red-flags",
            "title": "Quality of earnings and red flags",
            "level": "Intermediate",
            "minutes": 10,
            "summary": "How to tell real, cash-backed profit from flattering accounting, and the classic warning signs in company reports.",
            "body": """
**Quality of earnings** asks how real, repeatable and cash-backed a company's reported profit is. Accounting rules leave room for judgement, and some managements use it to flatter results. None of the signs below proves wrongdoing, but each is a reason to dig deeper.

### Accruals: profit without cash

Accruals are the part of profit not yet matched by cash. A simple check:

`accruals ratio = (net income - cash from operations) / average total assets`

A high or rising ratio means more of the profit is accounting estimates and less is cash. Research going back decades has found that firms with high accruals have tended to see weaker future earnings.

### Revenue recognition tricks

- **Channel stuffing:** shipping excess goods to distributors near the period end to book sales early.
- **Bill-and-hold:** recording sales for goods still sitting in the company's warehouse.
- Booking multi-year contracts up front, or changing recognition policies quietly.

A key symptom is **receivables growing faster than sales**. Track **days sales outstanding**:

`DSO = receivables / revenue x 365`

A jump in DSO means customers are paying more slowly, or sales are being recorded before they are really earned.

### Adjusted metrics

Companies often report "adjusted" or "underlying" earnings or EBITDA that exclude some costs. Some adjustments are reasonable; many are not. Watch for costs excluded every year, "restructuring" that never ends, and adjusted figures far above the audited ones. Always reconcile back to the official numbers.

### Stock-based compensation

Paying staff in shares or options is a real cost: it dilutes existing owners. Adding it back to "adjusted" profit or cash flow makes a company look more profitable than it is. Compare it with revenue and watch the share count.

### Other warning signs

- A change of auditor, especially after a disagreement, or a late filing
- **Related-party transactions:** deals with executives, their families or companies they control
- Frequent acquisitions that make year-on-year comparison hard
- Capitalising costs that peers expense, which lifts current profit
- Inventory growing much faster than sales
- Executives selling large amounts of stock while talking up the outlook

> Rule of thumb: when the story and the cash flow disagree, believe the cash flow.
""",
            "example": {
                "title": "Worked example: Riverbend Devices, two years (millions)",
                "body": """
Riverbend Devices (fictional) reports:

- Revenue: 400 last year, **440** this year (up 10%)
- Receivables: 60 last year, **90** this year (up 50%)
- Net income: **50**; cash from operations: **20**
- Average total assets: **500**

**DSO.** Last year 60 / 400 x 365 = **54.8 days**. This year 90 / 440 x 365 = **74.7 days**. Customers are taking about 20 days longer to pay, or some sales were booked early.

**Accruals ratio.** (50 - 20) / 500 = **6%** of assets. Only 20 of the 50 of profit arrived as cash.

**Adjusted EBITDA.** Operating income is 30 and D&A 20, so EBITDA is **50**. Riverbend also adds back stock-based compensation of 25 and a "restructuring" charge of 10 (its third in three years), and headlines adjusted EBITDA of **85**, 70% above the unadjusted figure.

**Verdict.** Receivables growing five times faster than sales, weak cash conversion and aggressive add-backs together say the reported profit is low quality. Next step: read the revenue recognition note and the receivables ageing disclosure.
""",
            },
            "terms": [
                ("Quality of earnings", "How real, repeatable and cash-backed a company's reported profits are."),
                ("Accruals ratio", "Net income minus cash from operations, divided by average total assets: the share of profit not yet backed by cash."),
                ("Days sales outstanding", "Receivables divided by revenue, times 365: roughly how many days customers take to pay."),
                ("Channel stuffing", "Shipping more goods to distributors than they need, to record sales earlier than real demand justifies."),
                ("Stock-based compensation", "Paying employees with shares or options, a real cost to shareholders through dilution."),
                ("Related-party transaction", "A deal between the company and its executives, directors, major owners or businesses they control."),
            ],
            "cards": [
                ("Revenue rises 10% but receivables rise 50%. What might be happening?",
                 "Customers are paying more slowly, or sales are being recorded before they are really earned, for example through channel stuffing or generous credit terms. Check DSO and the revenue recognition note."),
                ("Receivables are 90 and annual revenue is 440. What is days sales outstanding?",
                 "90 / 440 x 365 = about 74.7 days: on average customers take about 75 days to pay."),
                ("Net income is 50, cash from operations 20 and average total assets 500. What is the accruals ratio and what does it suggest?",
                 "(50 - 20) / 500 = 6%. A large share of profit is not backed by cash, which is a sign of lower-quality earnings."),
                ("Why is adding stock-based compensation back to adjusted earnings misleading?",
                 "Paying staff in shares is a real cost: it dilutes existing shareholders just as paying cash would reduce their value. Excluding it makes the business look more profitable than it is."),
                ("A company changes its auditor shortly after a disagreement over accounting. How should you react?",
                 "Treat it as a serious warning sign. Read the filing that explains the change and look closely at the accounting area in dispute before trusting the numbers."),
                ("What is a related-party transaction, and why does it matter?",
                 "A deal between the company and its insiders or their businesses, such as renting offices from the chief executive. Prices may not be fair, so value can flow from shareholders to insiders."),
                ("True or false: 'adjusted' earnings are always less reliable than audited earnings.",
                 "Not always. Some adjustments, such as a genuine one-time gain, help show the underlying trend. But adjusted figures are unaudited and chosen by management, so reconcile them to the official numbers."),
                ("What is channel stuffing?",
                 "Pushing more goods onto distributors than they can sell, usually near a period end, to record revenue early. It often shows up later as rising receivables, returns or a sales slump."),
                ("When a company's story and its cash flow statement disagree, which should you trust?",
                 "The cash flow statement. Cash is far harder to manipulate than accrual-based profit or management's narrative."),
            ],
            "calc": None,
            "links": [
                ("SEC EDGAR company filings search", "https://www.sec.gov/edgar/search/"),
            ],
        },
    ],
}
