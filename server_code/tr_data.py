"""Track: Data and tools. Content for Master Investor (see tools/CONTENT_BRIEF.md)."""

TRACK = {
    "id": "data",
    "title": "Data and tools",
    "level": "Intermediate",
    "blurb": "Where investing data comes from, how to pull it with code, the traps that quietly ruin research, "
             "and the workflow, open-source tools and alternative data that professionals use.",
    "lessons": [
        {
            "id": "where-to-get-data",
            "title": "Where to get investing data",
            "level": "Beginner",
            "minutes": 8,
            "summary": "The main sources of company, economic and price data, what each is good for, and what the "
                       "free versions leave out.",
            "body": """
Good research starts with knowing where numbers come from. A figure on a finance website was copied from somewhere; the closer you get to that original source, the fewer errors you inherit.

### Company filings: the primary source

Listed companies must publish audited reports. In the United States they file with the SEC on **EDGAR**: the 10-K (annual report), 10-Q (quarterly report) and 8-K (news such as results or a new chief executive). EDGAR is free and has a full-text search. Every company also has an **investor relations** page with results slides, call recordings and transcripts. Other countries have their own registries: **Companies House** in the UK, **SEDAR+** in Canada, and national regulators or exchanges elsewhere.

### Economic data

For the economy, go to **FRED** (the St. Louis Fed's free database of hundreds of thousands of series), central banks such as the Federal Reserve and the ECB, and national statistics offices (BLS and BEA in the US, the ONS in the UK, Statistics Canada, Eurostat for the EU). The **World Bank** and **IMF** cover countries side by side.

### Prices

Exchanges own the official price record and sell it. Free sites show delayed or end-of-day prices that are fine for learning and long-term investing, but they can have gaps, errors and unclear adjustments for splits and dividends, and their terms often forbid bulk downloading or reuse.

### Professional terminals

Banks and funds pay for terminals such as **Bloomberg**, **LSEG Workspace** (formerly Refinitiv Eikon), **FactSet** and **S&P Capital IQ**. A single seat typically costs thousands to tens of thousands per year. You pay for clean, standardised history, deep coverage, news, analyst estimates and support, not for secret information: the underlying filings are public.

### Screeners and charting tools

Screeners filter thousands of shares by rules such as "P/E under 15 and debt falling". Charting tools draw prices and indicators. Both are good for finding ideas, but they are a starting point: check anything important against the filing.

> Rule of thumb: use convenient sites to find ideas and the primary source to confirm the numbers you will act on.
""",
            "example": {"title": "Worked example: checking one number", "body": """
A screener says Northwind Tools has revenue of 1,240 million and net income of 93 million, so a net margin of:

`93 / 1,240 = 7.5%`

You open the latest 10-K on EDGAR. The income statement shows revenue of 1,240 million but net income of 81 million, and a note explains a one-off gain of 12 million that the screener had added back.

`81 / 1,240 = 6.5%`

The one-point gap matters: at a price of 15 times earnings, 93 million of profit implies a value of about 1,395 million, while 81 million implies about 1,215 million. Same company, 180 million apart, because of one line in a note.
"""},
            "terms": [
                ("EDGAR", "The SEC's free online system where US-listed companies file their reports and where anyone can read them."),
                ("10-K", "The audited annual report a US-listed company files with the SEC."),
                ("Primary source", "The original publisher of a number, such as a company filing or a statistics office, rather than a site that copied it."),
                ("Screener", "A tool that filters a large list of securities by rules you set, such as valuation or growth limits."),
                ("Financial terminal", "A paid professional data platform with standardised history, news, estimates and analytics, such as Bloomberg or FactSet."),
            ],
            "cards": [
                ("What is the primary source for a US-listed company's audited numbers?", "Its filings on SEC EDGAR, mainly the 10-K (annual) and 10-Q (quarterly). Websites and screeners copy from these and can add errors or adjustments."),
                ("What is an 8-K?", "A US filing for important events between regular reports, such as results, a new chief executive, a big acquisition or a default."),
                ("Name three free sources of economic data.", "Any three of: FRED, central banks (Federal Reserve, ECB), national statistics offices (BLS, BEA, ONS, Statistics Canada, Eurostat), the World Bank and the IMF."),
                ("Where would you find filings for a UK or Canadian company?", "Companies House for UK companies and SEDAR+ for Canadian ones, plus the company's own investor relations page."),
                ("What do you mainly pay for with a Bloomberg or FactSet seat?", "Clean, standardised history, wide coverage, news, analyst estimates and support. The underlying company filings are public and free."),
                ("Why should you not rely on a free price site for serious backtests?", "Free data can have gaps, errors and unclear split or dividend adjustments, and the terms often forbid bulk downloading."),
                ("A screener's margin differs from the 10-K. Which do you trust, and what do you check?", "Trust the 10-K, then read the notes to see what the screener changed, for example adding back one-off items."),
                ("True or false: professional terminals contain secret information unavailable to the public.", "False. Their value is convenience, cleaning and breadth; the filings and most raw facts they use are public."),
            ],
            "calc": None,
            "links": [
                ("SEC EDGAR full-text search", "https://www.sec.gov/edgar/search/"),
                ("FRED economic data", "https://fred.stlouisfed.org/"),
                ("Investor.gov: researching investments", "https://www.investor.gov/"),
            ],
        },
        {
            "id": "apis-and-python",
            "title": "Getting data with code",
            "level": "Intermediate",
            "minutes": 10,
            "summary": "Pull filings, economic series and prices with APIs, then turn prices into returns, monthly "
                       "series and rolling statistics with pandas.",
            "body": """
Copying numbers by hand stops working once you follow more than a few companies. An **API** (application programming interface) lets a program ask a server for data and get back a structured answer, usually JSON.

### Filings: the SEC EDGAR APIs

The SEC offers free JSON APIs on data.sec.gov with no key. The **submissions** endpoint lists a company's filings; **company facts** returns every figure the company has tagged in **XBRL** (the machine-readable labels inside filings), such as revenue or shares outstanding, across all its reports. Companies are identified by a **CIK** number, not the ticker. Two rules: send a **User-Agent** header that names you and gives a contact email, and stay under the SEC's limit of **10 requests per second**, or you will be blocked.

### Economic data and prices

**FRED** has a free API that needs a free **API key**; the Python library fredapi wraps it. For prices, the popular **yfinance** library is **unofficial**: it reads Yahoo Finance's website, which can change without notice, so it breaks from time to time and its terms are meant for personal use. Freemium and paid services such as **Alpha Vantage**, **Tiingo** and **Nasdaq Data Link** give documented APIs with keys, rate limits and paid tiers for more history or faster updates.

### pandas basics

Once prices are in a pandas DataFrame indexed by date:

- **Returns:** `prices.pct_change()` gives the simple return, today divided by yesterday minus 1.
- **Log returns:** `np.log(prices).diff()`; these add up over time, simple returns compound.
- **Resampling:** `prices.resample("ME").last()` keeps the last price of each month (older pandas used "M").
- **Rolling windows:** `returns.rolling(20).std()` gives a 20-day moving volatility.

`Annual volatility = daily standard deviation x sqrt(252)`

The 252 is the usual count of trading days in a year.

> Common mistake: averaging daily simple returns and multiplying by 252. Compound them, or use log returns, to get the true growth.
""",
            "example": {"title": "Worked example: four closing prices", "body": """
Closing prices: 50.00, 51.00, 49.98, 50.98.

Simple returns (`pct_change`):

- 51.00 / 50.00 - 1 = 2.00%
- 49.98 / 51.00 - 1 = -2.00%
- 50.98 / 49.98 - 1 = 2.00%

Adding them gives 2.00%, but the real gain is 50.98 / 50.00 - 1 = **1.96%**. Compounding gives the right answer: 1.02 x 0.98 x 1.02 = 1.0196.

Log returns: ln(1.02) = 0.0198, ln(0.98) = -0.0202, ln(1.02) = 0.0198. Sum = 0.0194, and ln(1.0196) = 0.0194, so log returns add exactly.

3-day rolling mean of price: (50.00 + 51.00 + 49.98) / 3 = 50.33, then (51.00 + 49.98 + 50.98) / 3 = 50.65.

If the daily standard deviation is 1.2%, annual volatility is about 1.2% x 15.87 = **19.0%**.
"""},
            "terms": [
                ("API", "A documented way for a program to request data from a server and receive a structured reply, often JSON."),
                ("XBRL", "Machine-readable tags inside company filings that label each number, such as revenue, so software can extract it."),
                ("CIK", "The Central Index Key, the permanent number the SEC uses to identify a filer."),
                ("Rate limit", "The maximum number of requests a data service allows in a given time before it slows or blocks you."),
                ("Log return", "The natural logarithm of today's price divided by yesterday's; log returns add up across periods."),
                ("Resampling", "Changing the frequency of a time series, for example turning daily prices into month-end prices."),
            ],
            "cards": [
                ("What two rules must you follow when calling the SEC EDGAR APIs?", "Send a User-Agent header with your name and a contact email, and stay under 10 requests per second."),
                ("What does the EDGAR company facts endpoint return?", "Every XBRL-tagged figure a company has reported, such as revenue or shares outstanding, across all its filings, as JSON."),
                ("Why can code that uses yfinance suddenly stop working?", "yfinance is unofficial: it reads Yahoo Finance's website, which can change without notice. It is fine for learning but fragile for anything important."),
                ("What do you need before calling the FRED API?", "A free API key from the St. Louis Fed, sent with each request."),
                ("Prices go 100, 110, 99. What are the simple returns and the total return?", "10% then 99/110 - 1 = -10%. The total is 99/100 - 1 = -1%, not 0%, because returns compound."),
                ("Why are log returns handy?", "They add across periods: the sum of daily log returns equals the log return over the whole period."),
                ("Daily volatility is 1%. Roughly what is the annual volatility?", "About 1% x sqrt(252), which is roughly 15.9%."),
                ("What does returns.rolling(60).mean() compute?", "For each day, the average return over the latest 60 rows, a moving window that slides forward one day at a time."),
                ("True or false: the ticker is the best key for EDGAR data.", "False. EDGAR identifies filers by CIK; tickers change and can be reused, so map tickers to CIKs first."),
            ],
            "calc": "sharpe",
            "links": [
                ("SEC EDGAR API documentation", "https://www.sec.gov/edgar/sec-api-documentation"),
                ("FRED API documentation", "https://fred.stlouisfed.org/docs/api/fred/"),
                ("fredapi on GitHub", "https://github.com/mortada/fredapi"),
            ],
        },
        {
            "id": "data-pitfalls",
            "title": "Data pitfalls that ruin research",
            "level": "Advanced",
            "minutes": 10,
            "summary": "Survivorship and look-ahead bias, restated numbers, adjusted prices, calendars, bad ticks and "
                       "delistings: the quiet errors behind too-good backtests.",
            "body": """
Most strategies that look brilliant on paper fail because of the data, not the idea. These errors rarely crash your code; they just make results look better than reality.

### Biases in what you test

**Survivorship bias** means testing only on things that still exist. Today's index members or today's funds are the winners; companies that went bust or were taken over are missing, so results look too good. Use a database that includes **delisted** securities and their final returns.

**Look-ahead bias** means using information before it was available. A company's year-end results come out weeks or months after the year ends; if your test buys on 31 December using those numbers, it is cheating. Lag every fundamental to its real publication date.

### Point-in-time versus restated

Companies and statistics offices **restate** figures. GDP is revised for years; a company may restate after an error or a change in accounting. A database that keeps only the latest number is **restated**. A **point-in-time** database stores each figure as it was known on each date. For economic series, ALFRED (the vintage version of FRED) keeps old releases.

### Prices that need adjusting

A 2-for-1 split halves the share price without anyone losing money. **Split-adjusted** prices divide earlier prices so the chart is continuous. **Dividend-adjusted** (total return) prices also scale earlier prices down for each dividend, so returns include payouts. Use adjusted prices for returns, but raw prices for things like "shares under 5", and remember adjusted history changes after every new dividend.

### Calendars, ticks and identities

- **Time zones and calendars:** markets close at different times and on different holidays; aligning a Tokyo close with a New York close on the same date mixes information.
- **Bad ticks:** a single wrong print can create a fake 50% move; filter outliers and check them.
- **Ticker changes:** tickers are renamed and reused. Track securities with a permanent identifier, not the ticker.

> Rule of thumb: if a backtest looks amazing, assume a data error until you have ruled each one out.
""",
            "example": {"title": "Worked example: how much survivorship flatters", "body": """
Ten fictional funds start a ten-year period. Seven survive with an average return of 8% a year. Three closed after poor years; their average return while open was -4% a year.

Survivors only:

`average = 8%`

All ten, weighting each fund equally:

`(7 x 8% + 3 x -4%) / 10 = (56% - 12%) / 10 = 4.4%`

Testing only today's funds overstates the typical result by 3.6 points a year.

Split check: Northwind Tools traded at 120, then did a 3-for-1 split and opened at 40. Raw prices show a fall of 40 / 120 - 1 = -66.7%. Split-adjusted history divides all earlier prices by 3, so the day before reads 40 and the true change is about 0%.

Dividend check: on the ex-date the price is 40 and the dividend 0.40. The adjustment factor is 1 - 0.40 / 40 = 0.99, applied to every earlier price.
"""},
            "terms": [
                ("Survivorship bias", "Overstated results from studying only securities or funds that still exist, leaving out failures."),
                ("Look-ahead bias", "Using data in a test before it would have been publicly available at that date."),
                ("Point-in-time data", "Data stored as it was known on each past date, before later revisions."),
                ("Restatement", "A later correction or revision of previously published figures."),
                ("Adjusted price", "A price history rescaled for splits, and often dividends, so returns are continuous and comparable."),
                ("Bad tick", "An erroneous price print in a data feed that can create fake jumps."),
            ],
            "cards": [
                ("What is survivorship bias in a backtest?", "Testing only on securities that still exist today, so the failures are missing and results look better than they were."),
                ("Your test buys on 31 December using that year's annual results. What is wrong?", "Look-ahead bias: the results were published weeks or months later. Lag fundamentals to their real release dates."),
                ("What is the difference between point-in-time and restated data?", "Point-in-time keeps each figure as known on each date; restated data keeps only the latest revised value, which no one knew back then."),
                ("Which FRED companion keeps old releases of economic series?", "ALFRED, which stores the vintages of each series as originally published and revised."),
                ("A stock at 90 does a 3-for-1 split. What is the split-adjusted price of a day when it traded at 90?", "90 / 3 = 30. All pre-split prices are divided by 3."),
                ("Why might you use raw rather than adjusted prices for a rule like 'shares under 5'?", "Adjusted prices are rescaled, so old adjusted values were not the prices traders actually saw."),
                ("Why is the ticker a poor identifier in historical data?", "Tickers change and get reused by other companies, so you can join the wrong histories. Use a permanent security identifier."),
                ("True or false: if code runs without errors, the data is fine.", "False. Bias, restatements, bad ticks and misaligned calendars give wrong results silently."),
            ],
            "calc": None,
            "links": [
                ("ALFRED vintage economic data", "https://alfred.stlouisfed.org/"),
            ],
        },
        {
            "id": "research-workflow",
            "title": "A research workflow and spreadsheet model",
            "level": "Intermediate",
            "minutes": 10,
            "summary": "From idea to decision: a checklist, a clean model layout, sanity checks, a one-page memo and a "
                       "decision log you review later.",
            "body": """
Professionals repeat the same process for every idea. A fixed workflow stops you skipping steps when you are excited, and makes your past decisions easy to review.

### Ideas and a checklist

Ideas come from screeners, annual reports of companies you already know, suppliers and competitors of those companies, industry news, and fund holdings filings. Before building anything, run a short **checklist**: Do I understand how the business makes money? Is the balance sheet safe? Who runs it, and how are they paid? What would make this a bad investment? The checklist kills weak ideas cheaply.

### Model layout: inputs, calculations, outputs

Keep a spreadsheet model in three clear parts:

1. **Inputs:** historical figures from filings plus your assumptions (growth, margins, tax rate, share count). Each assumption lives in one cell.
2. **Calculations:** formulas that only point at inputs or other calculations, never typed numbers.
3. **Outputs:** the few answers you care about: earnings per share, free cash flow, value per share, and a sensitivity table.

Use the common **colour convention**: **blue** font for hard-coded inputs, **black** for formulas (many analysts add green for links to other sheets). Anyone opening the file can then see at a glance what is an assumption.

### Sanity checks

- Does the balance sheet balance?
- Are forecast margins and growth inside the company's own history and its peers' range? If not, can you say why?
- Change one input: does the output move in the direction and size you expect?

### The memo and the decision log

Write a **one-page memo**: the thesis in two sentences, the three key drivers, the valuation range, the main risks, and what evidence would prove you wrong. Then record the decision in a **decision log** with the date, price, reasoning and your confidence. Reviewing the log later shows whether you were right for the right reasons, which outcomes alone cannot tell you.

> Common mistake: typing a number into a formula cell. It hides an assumption that you will forget to update.
""",
            "example": {"title": "Worked example: a small Northwind Tools model", "body": """
Inputs (blue): revenue last year 500 million, growth 6%, operating margin 15%, tax rate 25%, shares 40 million, no debt.

Calculations (black):

- Revenue next year: 500 x 1.06 = 530
- Operating profit: 530 x 15% = 79.5
- Net income: 79.5 x (1 - 25%) = 59.6
- Earnings per share: 59.6 / 40 = 1.49

Output: at a share price of 22.35, the forward P/E is 22.35 / 1.49 = **15.0**.

Sanity check: Northwind's margin was 12% to 16% over the past five years, so 15% is near the top. At 12%: operating profit 63.6, net income 47.7, EPS 1.19, P/E 18.8. The memo should say the valuation depends on margins staying near their high.
"""},
            "terms": [
                ("Investment checklist", "A fixed list of questions answered for every idea before deeper work, to catch weak ideas early."),
                ("Hard-coded input", "A number typed directly into a cell rather than calculated, usually shown in blue."),
                ("Sensitivity table", "A grid showing how an output, such as value per share, changes as one or two inputs change."),
                ("Investment memo", "A short written case for a decision: thesis, drivers, valuation, risks and what would prove it wrong."),
                ("Decision log", "A dated record of each decision, the price, the reasoning and your confidence, kept for later review."),
            ],
            "cards": [
                ("What are the three parts of a well-laid-out model?", "Inputs (history and assumptions), calculations (formulas only) and outputs (the few answers you care about)."),
                ("In the standard colour convention, what do blue and black font mean?", "Blue is a hard-coded input or assumption; black is a formula. Many analysts use green for links to other sheets."),
                ("Why should a calculation cell never contain a typed number?", "It hides an assumption that is easy to forget and impossible to see or change from the inputs section."),
                ("Name two sanity checks for a model.", "Any two of: the balance sheet balances; forecasts sit inside the company's and peers' historical ranges; changing one input moves the output the expected way."),
                ("Net income 60 million, 40 million shares, price 24. What is the P/E?", "EPS is 60 / 40 = 1.50, so the P/E is 24 / 1.50 = 16."),
                ("What should a one-page investment memo include?", "A short thesis, the key drivers, a valuation range, the main risks, and what evidence would prove you wrong."),
                ("Why keep a decision log if you can see your returns?", "Returns mix skill and luck. The log shows whether your reasoning was right, so you can learn from good and bad decisions."),
                ("What is the job of an investment checklist?", "To kill weak ideas cheaply before you spend hours modelling them, and to stop you skipping steps when excited."),
            ],
            "calc": "dcf",
            "links": [
                ("Damodaran Online: spreadsheets and data", "https://pages.stern.nyu.edu/~adamodar/"),
            ],
        },
        {
            "id": "open-source-toolkit",
            "title": "The open-source toolkit",
            "level": "Intermediate",
            "minutes": 9,
            "summary": "The free libraries on GitHub for data, backtesting, portfolios, analytics and machine "
                       "learning, and how to judge whether a project can be trusted.",
            "body": """
Much of the software quants use is free and open source, mostly in Python. Knowing the main categories saves you from writing everything yourself, and from trusting the wrong tool.

### What exists

- **Data:** libraries that fetch prices, economic series and filings, such as yfinance, pandas-datareader, fredapi and edgartools, and platforms such as OpenBB that combine many sources.
- **Backtesting:** engines that replay history and simulate trades, such as backtrader, backtesting.py, vectorbt, zipline-reloaded, QuantConnect's Lean and NautilusTrader.
- **Portfolio optimisation:** PyPortfolioOpt and Riskfolio-Lib for mean-variance, risk parity and related methods.
- **Performance analytics:** quantstats and pyfolio-reloaded for returns, drawdowns and risk reports; alphalens-reloaded for testing whether a signal predicts returns.
- **Machine learning:** Microsoft's qlib and FinRL for research pipelines; general tools like scikit-learn do much of the work.
- **Lists:** "awesome" lists such as awesome-quant point to hundreds more.

### How to judge a repository

Before you build on a project, check:

1. **Activity:** recent commits and releases. A project untouched for years may not work with current Python or pandas. Look for an "archived" label.
2. **Licence:** MIT, BSD and Apache allow broad use; GPL and AGPL impose conditions if you distribute or serve the software. No licence means you have no clear right to use it.
3. **Tests:** a test suite and automated checks show the authors catch their own bugs.
4. **Issues:** read open issues. Many unanswered bug reports about wrong results are a warning.
5. **Maintainers:** one volunteer or a team or company? Single-maintainer projects can stop overnight.

Stars show popularity, not correctness.

### Never trust a backtest library blindly

Every engine makes choices: when orders fill, whether costs and slippage are included, how dividends are handled. Defaults are often optimistic. Reproduce a tiny trade by hand and check the library gives the same answer before trusting a big test.

> Rule of thumb: if you cannot explain how the library fills an order, you cannot trust its backtest.
""",
            "example": {"title": "Worked example: checking a backtest by hand", "body": """
Test: buy 100 shares of a fictional stock at 100, sell at 120. Broker fee 0.1% of each trade.

By hand:

- Buy: 100 x 100 = 10,000, fee 10, total cost 10,010
- Sell: 100 x 120 = 12,000, fee 12, proceeds 11,988
- Profit: 11,988 - 10,010 = 1,978
- Return: 1,978 / 10,010 = **19.76%**

The library reports 20.00%. The gap tells you fees are off by default. You turn them on and it now reports 19.76%.

Next check: does it fill at the close of the signal day or the next open? If the signal uses today's close and the fill is also today's close, the test has a small look-ahead problem.
"""},
            "terms": [
                ("Open source", "Software whose code is published under a licence that lets others read, use and usually change it."),
                ("Backtesting engine", "Software that replays historical data and simulates the trades a strategy would have made."),
                ("Software licence", "The legal terms for using code; permissive ones (MIT, BSD, Apache) set few conditions, copyleft ones (GPL, AGPL) set more."),
                ("Archived repository", "A GitHub project its owners have frozen as read-only, so it gets no more fixes."),
                ("Slippage", "The difference between the price a strategy expects and the price a real order would get."),
            ],
            "cards": [
                ("Name five things to check before relying on a GitHub library.", "Recent activity, licence, tests, open issues and who maintains it (one volunteer, a team or a company)."),
                ("What does an 'archived' label on a repository mean?", "The owners froze it as read-only. It gets no more fixes and may not work with newer Python or pandas."),
                ("A repository has no licence file. Can you freely use the code?", "No. Without a licence you have no clear legal right to use, copy or change it."),
                ("Why are GitHub stars a weak signal of quality?", "Stars measure popularity, not correctness. A popular library can still have wrong defaults or unfixed bugs."),
                ("Buy 100 shares at 50, sell at 60, 0.1% fee each way. What is the return?", "Cost 5,000 + 5 = 5,005; proceeds 6,000 - 6 = 5,994; profit 989; return 989 / 5,005 = about 19.8%."),
                ("What is the quickest way to test a backtest library?", "Reproduce one tiny trade by hand, including fees and fill timing, and check the library matches."),
                ("Which kinds of library would you use for portfolio optimisation and for performance reports?", "Optimisation: PyPortfolioOpt or Riskfolio-Lib. Reports: quantstats or pyfolio-reloaded."),
                ("True or false: a backtest library's defaults are realistic.", "Often false. Defaults may skip costs and slippage or fill at prices you could not have traded at."),
            ],
            "calc": None,
            "links": [
                ("awesome-quant list", "https://github.com/wilsonfreitas/awesome-quant"),
                ("Choose a License: licence comparison", "https://choosealicense.com/"),
            ],
        },
        {
            "id": "alternative-data",
            "title": "Alternative data",
            "level": "Advanced",
            "minutes": 9,
            "summary": "Satellite images, card spending, web traffic, app downloads, job posts and sentiment: what "
                       "they can tell you, what they cost, and the legal lines.",
            "body": """
**Alternative data** is any information about companies or the economy that does not come from filings, prices or official statistics. Funds use it to estimate results before they are reported, a practice called **nowcasting**.

### The main types

- **Satellite and geolocation:** car counts in shop car parks, oil tank levels, crop health, ship tracking.
- **Card transactions:** anonymised spending from a panel of credit and debit card users, used to estimate retail sales.
- **Web traffic and app downloads:** visits to a company's site or downloads of its app as a guide to customer demand.
- **Job postings:** hiring by function and location hints at a company's plans, or at trouble when listings vanish.
- **Sentiment:** text from news, social media and reviews scored as positive or negative.

### The practical problems

- **Cost:** serious datasets often cost tens or hundreds of thousands a year, which only pays off for large portfolios.
- **Coverage:** a card panel sees a slice of spending; it may miss cash, some regions or business customers, and its mix shifts as members join and leave.
- **Short histories:** many datasets go back only a few years, too short to test a signal across different market conditions.
- **Decay:** once many funds buy the same data, its edge tends to shrink.
- **Cleaning:** raw alternative data is messy and must be mapped to the right companies and tickers.

### Legal and ethical lines

**Material non-public information** (MNPI) is information a reasonable investor would find important that has not been made public. Trading on it can be illegal insider dealing, wherever it came from. Data bought from a vendor can still be MNPI if, for example, a company employee leaked it in breach of a duty. Professionals check where data came from and whether people consented.

**Scraping** websites can breach their terms of service, copyright or privacy laws such as the GDPR, even when the page is public. Check the terms, respect robots.txt and rate limits, and never collect personal data you have no right to.

> Rule of thumb: if you would be uncomfortable explaining how you got the data to a regulator, do not use it.
""",
            "example": {"title": "Worked example: a card-spending nowcast", "body": """
A fictional retailer, Northwind Home, reports next month. A card panel shows its spending up 8.0% on the same quarter last year.

Over the past four quarters the panel's growth was above reported revenue growth by 1.0, 2.0, 1.5 and 1.5 points.

`average gap = (1.0 + 2.0 + 1.5 + 1.5) / 4 = 1.5 points`

`estimate = 8.0% - 1.5% = 6.5%`

Analysts expect 5.0%, so the data suggests a beat. Cautions: four quarters is a short history, the gap ranged from 1.0 to 2.0 points (so 6.0% to 7.0%), and if the panel recently added younger customers its mix may have shifted. The dataset costs 150,000 a year, so it only makes sense if the edge is worth more than that across the portfolio.
"""},
            "terms": [
                ("Alternative data", "Information about companies or the economy from sources other than filings, prices and official statistics."),
                ("Nowcasting", "Estimating a figure, such as quarterly sales or GDP, before it is officially published."),
                ("Material non-public information", "Important information not yet public; trading on it can be illegal insider dealing."),
                ("Panel data", "Data from a fixed group of people or businesses, such as card users, followed over time."),
                ("Web scraping", "Collecting data from websites automatically with a program, which can breach terms or privacy laws."),
            ],
            "cards": [
                ("What is nowcasting?", "Estimating a figure, such as a company's quarterly sales, before it is officially reported, often with alternative data."),
                ("Name four types of alternative data.", "Any four of: satellite images, geolocation, card transactions, web traffic, app downloads, job postings and sentiment from text."),
                ("Why are short histories a problem for alternative data?", "A few years of data cannot show whether a signal works across different market conditions, so results may be luck."),
                ("A card panel showed 9% growth; the panel has run 2 points above reported growth on average. What is the estimate?", "9% - 2% = about 7% reported growth, with a range based on how much the gap has varied."),
                ("What is material non-public information?", "Information a reasonable investor would find important that is not yet public. Trading on it can be illegal insider dealing."),
                ("True or false: data bought from a vendor can never be MNPI.", "False. If it came from someone breaching a duty, such as a leaking employee, it can still be MNPI, so check where it came from."),
                ("Why can scraping a public website still be a problem?", "It can breach the site's terms of service, copyright or privacy laws such as the GDPR, even if anyone can view the page."),
                ("Why does an alternative data edge tend to shrink over time?", "As more funds buy the same data, its information gets priced in earlier, leaving less to gain."),
            ],
            "calc": None,
            "links": [],
        },
    ],
}
