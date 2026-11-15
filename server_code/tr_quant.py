"""Track: The quant's world. Content for Master Investor (see tools/CONTENT_BRIEF.md)."""

TRACK = {
    "id": "quant",
    "title": "The quant's world",
    "level": "Pro",
    "blurb": "How quantitative investors work: the jobs, factor models, honest backtesting, statistical arbitrage, "
             "execution, machine learning and derivatives pricing.",
    "lessons": [
        # ------------------------------------------------------------------
        {
            "id": "what-quants-do",
            "title": "What quants actually do",
            "level": "Advanced",
            "minutes": 8,
            "summary": "The quant jobs, buy side versus sell side, the skills that matter, the kinds of firms and a typical research loop.",
            "body": """
A **quant** (quantitative analyst) uses maths, statistics and code to make financial decisions. The word covers several quite different jobs.

### The main roles

- **Quant researcher:** looks for predictive signals in data, builds models of returns and risk, and tests them. Closest to a scientist.
- **Quant trader:** runs and adjusts systematic strategies, decides sizing and risk limits, and often handles execution. More market-facing.
- **Quant developer:** builds the data pipelines, backtesting engines and trading systems. Strong software engineering matters more than finance here.
- **Risk quant:** measures and limits the risk of a portfolio or a bank's book, using tools such as value at risk and stress tests, and validates other people's models.
- **Sell-side and structuring quants:** at banks, price and hedge derivatives and design structured products for clients.

### Buy side and sell side

The **buy side** manages money: hedge funds, asset managers, pension funds, proprietary trading firms. Quants there are paid, directly or indirectly, for returns. The **sell side** (banks and brokers) sells services to the buy side: execution, market making, derivatives, research. Sell-side quants are paid for accurate pricing, hedging and serving clients, not for predicting markets.

Firm types include systematic hedge funds, high-frequency and market-making firms (speed and microstructure), large asset managers running factor funds, banks, and fintech or data vendors.

### The skills

1. **Maths:** linear algebra, calculus, probability, optimisation; stochastic calculus for derivatives roles.
2. **Statistics:** regression, time series, hypothesis testing, and above all scepticism about noisy results.
3. **Programming:** usually Python for research, often C++ for fast systems, plus SQL and solid version control.
4. **Markets:** how instruments, costs and trading rules actually work, so models stay grounded.

### A typical research loop

1. Form a hypothesis with an economic reason (for example, investors under-react to earnings news).
2. Gather and clean data, checking for errors and survivorship.
3. Build the signal and test it, with realistic costs.
4. Check robustness: other periods, markets and settings.
5. Paper trade or trade small, compare live with backtest.
6. Monitor for decay and retire signals that stop working.

> Rule of thumb: most ideas fail. A good quant's main skill is killing bad ideas quickly and cheaply.
""",
            "example": {"title": "Worked example: one pass of the research loop", "body": """
A researcher at a fictional fund, Cedar Ridge Capital, tests the idea that stocks with **upward analyst revisions** beat those with downward revisions.

1. **Universe:** 1,000 stocks over 15 years, including companies that were later delisted.
2. **Signal:** each month, rank stocks by the net share of analysts raising estimates.
3. **Portfolio:** buy the top 10% (100 stocks), short the bottom 10%, equal weights.
4. **Gross result:** the long-short portfolio returned an average of **0.50% a month**, about 6% a year.
5. **Costs:** turnover is 60% of the book a month; at 0.30% cost per unit of turnover that is 0.60 x 0.30% = **0.18% a month**.
6. **Net:** 0.50% - 0.18% = **0.32% a month**, about 3.8% a year.
7. **Robustness:** the effect is half as large in the last five years, so the researcher flags possible decay before anyone allocates capital.
"""},
            "terms": [
                ("Quant", "A quantitative analyst who uses maths, statistics and programming to make or support financial decisions."),
                ("Buy side", "Firms that manage money and invest it, such as hedge funds, asset managers and pension funds."),
                ("Sell side", "Banks and brokers that sell services such as execution, market making, derivatives and research to investors."),
                ("Systematic strategy", "An investment approach where rules coded in advance, rather than case-by-case judgement, decide the trades."),
                ("Signal", "A measurable quantity that is expected to predict future returns or risk."),
                ("Alpha decay", "The fading of a signal's predictive power over time, often as more traders exploit it."),
            ],
            "cards": [
                ("What is the difference between a quant researcher and a quant developer?",
                 "The researcher looks for and tests predictive signals and models; the developer builds the data pipelines, backtesting tools and trading systems they run on."),
                ("How are buy-side and sell-side quants paid for different things?",
                 "Buy-side quants are rewarded, directly or indirectly, for investment returns. Sell-side quants are rewarded for accurate pricing, hedging and serving clients, not for predicting the market."),
                ("What does a risk quant do?",
                 "Measures and limits the risk of a portfolio or a bank's positions, using tools such as value at risk and stress tests, and often validates models built by others."),
                ("Name the four skill areas quants need.",
                 "Maths (linear algebra, probability, optimisation), statistics (regression, time series, testing), programming (often Python and C++), and practical knowledge of markets and trading costs."),
                ("List the steps of a typical quant research loop.",
                 "Hypothesis with an economic reason, data gathering and cleaning, signal building and testing with costs, robustness checks, small live or paper trading, then monitoring for decay."),
                ("A signal makes 0.50% a month gross with 60% monthly turnover at 0.30% cost per unit of turnover. What is the net?",
                 "Cost = 0.60 x 0.30% = 0.18% a month, so net = 0.50% - 0.18% = 0.32% a month, about 3.8% a year."),
                ("Why should a hypothesis have an economic reason behind it?",
                 "A pattern found only by searching data is likely to be chance. A reason, such as a risk being rewarded or investors under-reacting, makes it more likely the effect is real and will persist."),
                ("True or false: a good quant's main output is a stream of new working strategies.",
                 "False. Most ideas fail, so a key skill is rejecting bad ideas quickly and cheaply. Only a small share of tested ideas ever reach live trading."),
            ],
            "calc": None,
            "links": [],
        },
        # ------------------------------------------------------------------
        {
            "id": "factor-investing",
            "title": "Factor investing",
            "level": "Pro",
            "minutes": 10,
            "summary": "From CAPM to the Fama-French models, momentum, quality and low volatility, long-short factors and the factor zoo debate.",
            "body": """
A **factor** is a common characteristic that helps explain why groups of securities earn different returns. Factor investing builds portfolios that deliberately tilt towards characteristics that have historically earned a premium.

### From CAPM to Fama-French

The **capital asset pricing model (CAPM)** says one factor matters: exposure to the market, measured by **beta**.

`E(R) = rf + beta x (E(Rm) - rf)`

Here rf is the risk-free rate and E(Rm) - rf is the market risk premium. In the data, CAPM explains less than hoped: small companies and cheap (high book-to-market) companies earned more than their betas predicted.

Eugene Fama and Kenneth French added two factors in their **three-factor model**: **SMB** (small minus big, the return of small stocks over large) and **HML** (high minus low book-to-market, value over growth). Their **five-factor model** later added **RMW** (robust minus weak profitability) and **CMA** (conservative minus aggressive investment).

`R - rf = alpha + b x (Rm - rf) + s x SMB + h x HML + e`

The coefficients (b, s, h) are a portfolio's **factor loadings**; **alpha** is the return the factors do not explain.

### Other well-known factors

- **Momentum:** recent 12-month winners (usually skipping the latest month) beat recent losers. It is often called UMD or WML.
- **Quality:** profitable, stable, low-debt companies have tended to beat weak ones.
- **Low volatility:** low-risk stocks have historically earned about as much as, or more than, high-risk stocks, against CAPM's prediction.

### Long-short factor portfolios

Academic factors are **long-short**: buy the top group (say the cheapest 30%), short the bottom group, so market exposure roughly cancels and what is left is the factor's own return. Real-world factor funds are often **long-only tilts**, which keep most of their return from the market.

### The factor zoo

Researchers have published hundreds of "factors". With so many tests, some will look significant by chance. Campbell Harvey and co-authors argued that new factors should clear a t-statistic of about 3 rather than the usual 2. Replication studies disagree on how serious the problem is: some found many published anomalies weaken or vanish with careful testing, others found most of the main ones hold up. Many factors have also become weaker after publication.

> Common mistake: calling a fund's return alpha when it is just a tilt to well-known factors that could be bought far more cheaply.
""",
            "example": {"title": "Worked example: CAPM and a factor regression", "body": """
**CAPM:** risk-free rate 3%, market risk premium 5%, and Juniper Growth Fund has a beta of 1.2.

- Expected return = 3% + 1.2 x 5% = 3% + 6% = **9%**

The fund actually returned **11%** a year, apparently 2% of alpha.

**Three-factor regression** of the fund's monthly excess returns gives:

- b (market) = 1.0, s (SMB) = 0.4, h (HML) = 0.5, alpha = 0.06% a month (about 0.7% a year, not statistically significant)

Over the same years: market premium 5%, SMB 2%, HML 3% a year.

- Explained excess return = 1.0 x 5% + 0.4 x 2% + 0.5 x 3% = 5% + 0.8% + 1.5% = **7.3%**
- Plus risk-free 3% = **10.3%**, leaving only about 0.7% as alpha, too small to tell apart from noise

So most of the "alpha" was a tilt to small and value stocks.
"""},
            "terms": [
                ("Factor", "A shared characteristic, such as size or value, that helps explain differences in returns across securities."),
                ("Beta", "A measure of how much an asset moves with the market: 1.2 means about 1.2% for each 1% market move."),
                ("CAPM", "The capital asset pricing model: expected return equals the risk-free rate plus beta times the market risk premium."),
                ("Factor loading", "A portfolio's sensitivity to a factor, estimated as a regression coefficient."),
                ("Alpha", "The part of a portfolio's return that its factor exposures do not explain."),
                ("Factor zoo", "The hundreds of published factors, many of which may be false discoveries from repeated testing."),
            ],
            "cards": [
                ("What is the CAPM formula?",
                 "E(R) = rf + beta x (E(Rm) - rf): expected return is the risk-free rate plus beta times the market risk premium."),
                ("Risk-free 3%, beta 1.2, market premium 5%. What does CAPM predict?",
                 "3% + 1.2 x 5% = 3% + 6% = 9% a year."),
                ("What factors did Fama and French add in the three-factor and five-factor models?",
                 "Three-factor: market, SMB (small minus big) and HML (value minus growth by book-to-market). Five-factor adds RMW (robust minus weak profitability) and CMA (conservative minus aggressive investment)."),
                ("Why are academic factors built as long-short portfolios?",
                 "Buying the top group and shorting the bottom group roughly cancels market exposure, so the portfolio isolates the factor's own return."),
                ("What is the low-volatility anomaly?",
                 "Low-risk stocks have historically earned about as much as or more than high-risk stocks, which contradicts CAPM's prediction that higher beta should earn more."),
                ("What is the factor zoo problem?",
                 "Hundreds of factors have been published, and with that many tests some will look significant by chance. Harvey and co-authors proposed a t-statistic hurdle of about 3 instead of 2."),
                ("A fund beats CAPM by 2% a year. Is that alpha?",
                 "Not necessarily. A multi-factor regression may show the excess is explained by tilts to known factors such as small and value stocks, which can be bought cheaply in index funds."),
                ("True or false: replication studies all agree that most published factors are false.",
                 "False. Studies disagree: some found many anomalies weaken or vanish with careful testing, others found most major factors replicate. Many have weakened after publication."),
            ],
            "calc": None,
            "links": [("Kenneth French data library", "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html")],
        },
        # ------------------------------------------------------------------
        {
            "id": "backtesting",
            "title": "Backtesting without fooling yourself",
            "level": "Pro",
            "minutes": 10,
            "summary": "The backtest pipeline, the classic biases, costs, walk-forward testing and the idea behind the deflated Sharpe ratio.",
            "body": """
A **backtest** simulates how a strategy would have performed on past data. It is the main tool of systematic investing and the easiest way to fool yourself.

### The pipeline

1. Clean, point-in-time data (what was actually known on each date).
2. Signal rules defined in code.
3. Portfolio construction and position sizing.
4. Realistic execution: costs, slippage, delays, borrowing limits.
5. Performance and risk statistics.
6. Out-of-sample checks.

### The classic biases

- **Survivorship bias:** using only companies that still exist today leaves out the ones that went bankrupt or were delisted, so results look too good.
- **Look-ahead bias:** using information that was not available at the time, such as annual results dated to the year-end rather than the day they were published, or revised economic data.
- **Data snooping:** reusing the same history to try idea after idea until something works.
- **Multiple testing:** if you test 100 strategies with no real edge at a 5% significance level, you expect about 5 to look significant by luck.
- **Overfitting:** tuning so many parameters that the model fits past noise rather than a real pattern. The tell-tale sign is great in-sample results that collapse on new data.

### Costs and slippage

Many paper edges disappear once you subtract commissions, spreads, market impact and borrowing costs for shorts. High-turnover strategies are the most exposed.

`Net return = gross return - turnover x cost per round trip`

### Out-of-sample and walk-forward

Keep some data untouched until the end: the **out-of-sample** test. **Walk-forward** testing repeats this through time: fit on, say, years 1 to 5, test on year 6, then refit on years 2 to 6 and test on year 7, and so on. Only the test-period results count.

### The deflated Sharpe ratio

When you pick the best of many trials, its Sharpe ratio is biased upwards: the more trials, the higher the best one looks by chance. The **deflated Sharpe ratio**, proposed by David Bailey and Marcos Lopez de Prado, adjusts the observed Sharpe for the number of trials, the length of the track record and non-normal returns (skew and fat tails), and asks how likely it is that the true Sharpe is above zero.

> Rule of thumb: record every variant you try. The number of trials is part of the result.
""",
            "example": {"title": "Worked example: costs and multiple testing", "body": """
A researcher at Granite Lane Partners tries **200 variants** of a short-term reversal strategy and keeps the best one.

**Best variant:** gross return **12% a year**, volatility 10%, so a gross Sharpe of about 1.2 (ignoring the risk-free rate).

**Costs:** the strategy turns over its portfolio **20 times a year**, at **0.20%** per round trip.

- Cost drag = 20 x 0.20% = **4% a year**
- Net return = 12% - 4% = **8%**, net Sharpe about 0.8

**Multiple testing:** even if none of the 200 variants had real skill, at a 5% significance level about 200 x 5% = **10** would look significant by chance. The best of 200 would look good almost by construction.

**Walk-forward check:** refitted every year on the previous five years, the chosen rules returned **2% a year net** in the test years. That, not 12%, is the honest estimate, and it is too small to trust.
"""},
            "terms": [
                ("Backtest", "A simulation of how a trading strategy would have performed on historical data."),
                ("Survivorship bias", "Overstated results from testing only on securities that survived, leaving out failures and delistings."),
                ("Look-ahead bias", "Using information in a backtest that was not available at the time of the simulated decision."),
                ("Overfitting", "Fitting a model so closely to past data that it captures noise and fails on new data."),
                ("Walk-forward testing", "Repeatedly fitting a model on one window of history and testing it on the following period, rolling forward through time."),
                ("Deflated Sharpe ratio", "A Sharpe ratio adjusted for the number of strategies tried, track-record length and non-normal returns."),
            ],
            "cards": [
                ("What is survivorship bias in a backtest?",
                 "Testing only on companies that exist today, leaving out those that went bankrupt or were delisted. Results look better than an investor could really have achieved."),
                ("Give an example of look-ahead bias.",
                 "Using a company's annual results from the year-end date instead of the later date they were published, or using revised economic data that was not available at the time."),
                ("You test 100 strategies with no real edge at a 5% significance level. How many look significant?",
                 "About 100 x 5% = 5, purely by chance. That is why the number of trials must be reported and corrected for."),
                ("A strategy makes 12% gross and turns over 20 times a year at 0.20% per round trip. What is the net?",
                 "Cost drag = 20 x 0.20% = 4%, so the net return is 12% - 4% = 8% a year, before any market impact beyond that cost estimate."),
                ("How does walk-forward testing work?",
                 "Fit on one window (for example years 1 to 5), test on the next period (year 6), then roll forward and repeat. Only the results from the test periods count."),
                ("What is the main symptom of overfitting?",
                 "Excellent in-sample results that collapse out of sample, often with many tuned parameters and rules that have no economic reason."),
                ("What does the deflated Sharpe ratio adjust for?",
                 "The number of strategies tried, the length of the track record, and non-normal returns such as skew and fat tails. It estimates how likely the true Sharpe is above zero."),
                ("Why record every variant you test?",
                 "The best of many trials looks good by chance, so the number of trials is needed to judge whether a result is real. Hiding failed trials inflates confidence."),
            ],
            "calc": "sharpe",
            "links": [],
        },
        # ------------------------------------------------------------------
        {
            "id": "stat-arb",
            "title": "Statistical arbitrage and pairs trading",
            "level": "Pro",
            "minutes": 10,
            "summary": "Correlation versus cointegration, the spread z-score, half-life of mean reversion, entry and exit rules and why pairs break.",
            "body": """
**Statistical arbitrage** trades many small, temporary mispricings between related securities, expecting them to correct on average. It is not true arbitrage: any single trade can lose. The simplest form is **pairs trading**.

### Correlation is not enough

Two stocks can be highly **correlated** (their daily returns move together) yet drift apart for years. What pairs traders want is **cointegration**: a combination of the two prices, the **spread**, that tends to return to a stable mean.

`Spread = price A - hedge ratio x price B`

The **hedge ratio** is usually estimated by regressing price A on price B. You then test whether the spread is stationary (has a stable mean and variance), for example with the Engle-Granger or Johansen tests. Cointegration is about prices staying tied together; correlation is about returns moving together.

### The z-score

To judge how stretched the spread is, standardise it:

`z = (spread - mean of spread) / standard deviation of spread`

The mean and standard deviation are usually measured over a rolling look-back window.

### Half-life of mean reversion

How fast does the spread come back? Regress the daily change in the spread on yesterday's spread level:

`change in spread = lambda x spread yesterday + c`

If lambda is negative, the spread mean-reverts, and the **half-life** (the typical time for half of a gap to close) is about:

`half-life = -ln(2) / lambda`

A half-life of days to a few weeks suits trading; a very long half-life ties up capital and risk for too long.

### Entry and exit rules

A classic rule set:

- **Enter** when |z| > 2: if z is +2, short A and buy hedge ratio x B; if -2, the reverse.
- **Exit** when z returns towards 0 (for example |z| < 0.5).
- **Stop** if |z| goes beyond a limit such as 4, or after a time limit of a few half-lives.

### Why pairs break

The relationship rests on the two businesses staying similar. Takeovers, a lost contract, new regulation, a change in strategy or a scandal can permanently shift the spread. Pairs also fail together in crowded unwinds, when many funds holding similar trades sell at the same time.

> Common mistake: finding cointegrated pairs by testing thousands of combinations. Some will pass by chance; prefer pairs with an economic link and check them out of sample.
""",
            "example": {"title": "Worked example: a pairs trade by the numbers", "body": """
Two fictional rail companies, **Northline** (A) and **Eastgate** (B), share a hedge ratio of **1.5**.

Today A = 61.00 and B = 38.60.

1. Spread = 61.00 - 1.5 x 38.60 = 61.00 - 57.90 = **3.10**
2. Over the look-back window the spread's mean is **2.00** and its standard deviation **0.50**
3. z = (3.10 - 2.00) / 0.50 = **2.2**, above the entry level of 2

**Trade:** short 1,000 Northline and buy 1,500 Eastgate.

**Half-life:** regressing the daily change in the spread on yesterday's spread gives lambda = **-0.10**, so half-life = 0.693 / 0.10 = about **6.9 trading days**.

**Exit:** a week later A = 60.20 and B = 38.80. Spread = 60.20 - 58.20 = 2.00, z = 0.

- Short A: 1,000 x (61.00 - 60.20) = **+800**
- Long B: 1,500 x (38.80 - 38.60) = **+300**
- Total before costs = **1,100**, which equals 1,000 x (3.10 - 2.00), the change in the spread.
"""},
            "terms": [
                ("Statistical arbitrage", "Trading many small, temporary mispricings between related securities, profiting on average rather than on every trade."),
                ("Cointegration", "A property of two or more price series where some combination of them stays stationary around a stable mean."),
                ("Hedge ratio", "The number of units of one security traded against one unit of another to form the spread."),
                ("Z-score", "How many standard deviations a value is from its mean: (value - mean) / standard deviation."),
                ("Half-life of mean reversion", "The typical time for half of a gap between the spread and its mean to close."),
                ("Stationary series", "A series whose mean and variance stay stable over time, so it tends to return to its average."),
            ],
            "cards": [
                ("What is the difference between correlation and cointegration?",
                 "Correlation means returns move together day to day; cointegration means a combination of prices stays tied to a stable mean. Highly correlated stocks can still drift apart for years."),
                ("How is a pair's spread z-score calculated?",
                 "z = (spread - mean of spread) / standard deviation of spread, usually over a rolling look-back window."),
                ("Spread 3.10, mean 2.00, standard deviation 0.50. What is z?",
                 "(3.10 - 2.00) / 0.50 = 1.10 / 0.50 = 2.2."),
                ("Spread = A - 1.5 x B and z is +2.2. What trade do you put on?",
                 "The spread is too high, so sell the spread: short A and buy 1.5 units of B for each unit of A, expecting the spread to fall back towards its mean."),
                ("A regression of the spread's daily change on yesterday's spread gives lambda = -0.10. What is the half-life?",
                 "Half-life = -ln(2) / lambda = 0.693 / 0.10 = about 6.9 days."),
                ("What is a classic set of pairs entry and exit rules?",
                 "Enter when |z| exceeds 2, exit when z returns near 0 (for example |z| < 0.5), and stop out if |z| exceeds a limit such as 4 or the trade lasts several half-lives."),
                ("Why do pairs break?",
                 "The two businesses stop being similar: a takeover, lost contract, new regulation, strategy change or scandal can permanently shift the spread. Crowded unwinds can also hit many pairs at once."),
                ("True or false: statistical arbitrage is risk-free.",
                 "False. It profits on average across many trades, but any single trade can lose, and spreads can widen far beyond normal before they revert, or never revert at all."),
            ],
            "calc": None,
            "links": [],
        },
        # ------------------------------------------------------------------
        {
            "id": "execution",
            "title": "Execution and market impact",
            "level": "Pro",
            "minutes": 9,
            "summary": "Implementation shortfall, VWAP, TWAP and POV algorithms, the square-root impact rule and why capacity limits strategies.",
            "body": """
A good idea can be ruined by poor execution. For large investors, trading costs are often the biggest controllable drag on returns.

### Implementation shortfall

**Implementation shortfall** compares your real result with a paper portfolio that traded instantly at the **decision price** (the price when you decided to trade). It includes:

- **Execution cost:** the difference between your average fill and the decision price, plus fees.
- **Opportunity cost:** the move in price on any shares you failed to buy or sell.

Measuring it forces an honest view: trading slowly reduces impact but risks the price running away; trading fast does the opposite.

### The main algorithms

- **VWAP (volume-weighted average price):** trade in proportion to the market's typical volume pattern through the day, aiming to match the day's VWAP.
- **TWAP (time-weighted average price):** split the order into equal slices over a set time.
- **POV (percentage of volume):** trade a fixed share of market volume, for example 10%, speeding up when the market is busy.
- **Implementation shortfall (arrival price) algorithms:** trade faster at the start to reduce the risk of price drift, balancing impact against timing risk.

`VWAP = sum of (price x volume) / sum of volume`

### The square-root rule of thumb

Studies of many large orders across markets have found that impact grows roughly with the **square root** of order size relative to volume, not in a straight line:

`Impact = Y x daily volatility x sqrt(order size / daily volume)`

Y is a constant of order 1, estimated from a firm's own trades. Quadrupling order size roughly doubles impact per share. It is an approximation, useful for planning, not a law.

### Why capacity limits strategies

Because cost per share rises with size, a strategy's profit does not scale forever. As assets grow, impact eats more of each trade's edge until extra money adds nothing, or even lowers total profit. That size is the strategy's **capacity**. Fast, high-turnover strategies in small stocks have low capacity; slow strategies in large, liquid markets have high capacity.

> Rule of thumb: estimate costs at the size you plan to trade, not at the size of your backtest.
""",
            "example": {"title": "Worked example: shortfall and square-root impact", "body": """
A portfolio manager at Saltmarsh Asset Management decides to buy **10,000 shares** of Kestrel Foods at a decision price of **50.00**: a paper portfolio of 500,000.

The trader fills **8,000 shares at an average of 50.20**, pays **80** in fees, and the remaining 2,000 shares go unfilled as the price ends the day at **51.00**.

1. Execution cost = 8,000 x (50.20 - 50.00) + 80 = 1,600 + 80 = **1,680**
2. Opportunity cost = 2,000 x (51.00 - 50.00) = **2,000**
3. Implementation shortfall = 1,680 + 2,000 = **3,680**, or 3,680 / 500,000 = **0.74%**

**Square-root estimate** for a bigger order: daily volatility 2%, order = 10% of daily volume, Y = 1.

- Impact = 1 x 2% x sqrt(0.10) = 2% x 0.316 = **about 0.63%**
- At 40% of daily volume: 2% x sqrt(0.40) = 2% x 0.632 = **about 1.26%**, double the cost per share for four times the size.
"""},
            "terms": [
                ("Implementation shortfall", "The gap between a paper portfolio traded at the decision price and the real result, including fees and missed trades."),
                ("VWAP", "Volume-weighted average price: the sum of price times volume divided by total volume over a period."),
                ("TWAP", "Time-weighted average price: an execution method that splits an order into equal slices over time."),
                ("Percentage of volume", "An execution algorithm that trades a fixed share of market volume as it happens."),
                ("Market impact", "The price move caused by your own trading, which raises the cost of buying or lowers the price of selling."),
                ("Capacity", "The amount of money a strategy can run before trading costs eat most of its extra profit."),
            ],
            "cards": [
                ("What two parts make up implementation shortfall?",
                 "Execution cost (average fill versus the decision price, plus fees) and opportunity cost (the price move on shares you planned to trade but did not)."),
                ("Decision price 50.00; 8,000 filled at 50.20 with 80 fees; 2,000 unfilled and the price ends at 51.00. What is the shortfall?",
                 "Execution 8,000 x 0.20 + 80 = 1,680; opportunity 2,000 x 1.00 = 2,000; total 3,680, or 0.74% of the 500,000 paper portfolio."),
                ("How do VWAP, TWAP and POV algorithms differ?",
                 "VWAP trades along the market's typical daily volume pattern, TWAP trades equal slices over time, and POV trades a fixed percentage of actual volume as it happens."),
                ("How is VWAP calculated?",
                 "Sum of (price x volume) for every trade divided by total volume. For 100 shares at 10 and 300 at 11, VWAP = (1,000 + 3,300) / 400 = 10.75."),
                ("What is the square-root impact rule of thumb?",
                 "Impact is roughly Y x daily volatility x sqrt(order size / daily volume), with Y of order 1. Impact per share grows with the square root of size, not in a straight line."),
                ("Using the square-root rule, what happens to impact per share if you quadruple the order?",
                 "It roughly doubles, because sqrt(4) = 2. Total impact cost (per-share impact times shares) rises about eightfold."),
                ("What limits a strategy's capacity?",
                 "Trading costs per share rise with size, so as assets grow, impact eats more of the edge until extra money adds little or no profit. High-turnover strategies in small stocks have the lowest capacity."),
                ("What is the trade-off between trading fast and trading slowly?",
                 "Fast trading pays more market impact; slow trading risks the price drifting away before you finish (timing or opportunity cost). Shortfall algorithms try to balance the two."),
            ],
            "calc": None,
            "links": [],
        },
        # ------------------------------------------------------------------
        {
            "id": "machine-learning",
            "title": "Machine learning in finance",
            "level": "Pro",
            "minutes": 10,
            "summary": "Why ML is hard in markets, features and labels, triple-barrier labelling, purged cross-validation, leakage and feature importance.",
            "body": """
Machine learning (ML) has transformed image and speech recognition. In return prediction it helps, but far less dramatically, because financial data is unusual.

### Why markets are hard for ML

- **Low signal-to-noise:** most of a price move is noise. A model that predicts direction correctly 52% of the time can be very valuable; one that claims 70% is usually leaking information.
- **Non-stationarity:** relationships change as markets, rules and participants change, and as others trade away patterns.
- **Little independent data:** decades of daily prices are only thousands of observations, heavily overlapping and correlated.

Flexible models fit noise easily, so overfitting is the central danger.

### Features and labels

**Features** are the inputs: past returns, volatility, valuation ratios, volume, sentiment. **Labels** are what you try to predict. A naive label is "the return over the next 10 days was positive". It ignores the path: a trade that fell 15% before recovering would have hit any sensible stop.

**Triple-barrier labelling**, described by Marcos Lopez de Prado in *Advances in Financial Machine Learning*, sets three barriers from the entry: an upper profit-take, a lower stop-loss and a vertical time limit. The label is whichever is touched first: +1 for the upper, -1 for the lower, and at the time limit either 0 or the sign of the return.

### Cross-validation done right

Ordinary k-fold cross-validation shuffles data and assumes observations are independent. In finance, labels span time, so a training sample whose label window overlaps the test period leaks test information into training.

- **Purging:** remove training samples whose label windows overlap the test period.
- **Embargo:** also drop a short stretch of samples just after the test period, because of serial correlation.

### Leakage and feature importance

**Leakage** is any way future information reaches the model: look-ahead data, overlapping labels, scaling with statistics from the full sample, or choosing features using the whole dataset. **Feature importance** methods (such as mean decrease in accuracy, which shuffles one feature and measures the drop in out-of-sample score) help check that the model relies on sensible inputs. Correlated features share importance, so interpret them as groups.

> Rule of thumb: if a model's out-of-sample accuracy looks too good for markets, assume leakage until you have proved otherwise.
""",
            "example": {"title": "Worked example: triple barriers and purging", "body": """
**Triple barrier:** you buy Alder Energy at **100** with an upper barrier at **+4% (104)**, a lower barrier at **-2% (98)** and a vertical barrier at **10 trading days**.

- Path A touches 104 on day 3: label **+1**.
- Path B dips to 97.80 on day 2 (below 98), then rallies to 106: label **-1**, because the stop came first. A naive "10-day return" label would have called it a winner.
- Path C stays between 98 and 104 and ends day 10 at 101: label **0** (or +1 if you use the return's sign).

**Purged cross-validation:** 1,000 daily samples, each label spanning up to 10 days, split into 5 folds of 200.

- Testing on samples 401 to 600, the training samples **391 to 400** have labels that reach into the test window, so they are **purged**.
- With an embargo of 1% of samples (**10**), samples **601 to 610** are also dropped from training.
- Training uses 1 to 390 and 611 to 1,000: **780 samples** instead of 800.
"""},
            "terms": [
                ("Signal-to-noise ratio", "How large the predictable part of a series is compared with its random part; very low for asset returns."),
                ("Non-stationarity", "When the statistical properties of data, such as its mean or relationships, change over time."),
                ("Triple-barrier labelling", "Labelling a trade by which comes first: a profit-take barrier, a stop-loss barrier or a time limit."),
                ("Purged cross-validation", "Cross-validation that removes training samples whose label windows overlap the test period."),
                ("Embargo", "A gap of samples dropped from training just after a test period to stop leakage through serial correlation."),
                ("Leakage", "Any way information from the future, or from the test set, reaches a model during training."),
            ],
            "cards": [
                ("Why is machine learning harder in markets than in image recognition?",
                 "Returns have a very low signal-to-noise ratio, relationships change over time (non-stationarity), and there is little independent data, so flexible models easily fit noise."),
                ("What is triple-barrier labelling?",
                 "Each trade gets three barriers: a profit-take above, a stop-loss below and a time limit. The label is whichever is touched first: +1 upper, -1 lower, and 0 or the return's sign at the time limit."),
                ("Entry 100, barriers at 104 and 98, 10-day limit. The price hits 97.80 on day 2 then rises to 106. What is the triple-barrier label?",
                 "-1, because the lower barrier at 98 was touched first. A simple 10-day return label would wrongly call this a winning trade."),
                ("Why does ordinary k-fold cross-validation leak information in finance?",
                 "Labels span time, so training samples whose label windows overlap the test period carry information about test outcomes. Shuffling also mixes past and future."),
                ("What are purging and embargoing?",
                 "Purging removes training samples whose label windows overlap the test period. Embargoing also drops a short stretch of samples right after the test period because of serial correlation."),
                ("Name three common sources of leakage.",
                 "Look-ahead data, overlapping labels between training and test sets, and scaling or selecting features using statistics from the full dataset including the test period."),
                ("A return model shows 70% directional accuracy out of sample. What should you suspect?",
                 "Leakage. In markets even 52% to 55% accuracy can be valuable, so a much higher figure usually means future information has slipped into training."),
                ("How does mean decrease in accuracy measure feature importance?",
                 "It shuffles one feature at a time and measures how much the out-of-sample score drops. Correlated features share importance, so they are best judged as groups."),
            ],
            "calc": None,
            "links": [],
        },
        # ------------------------------------------------------------------
        {
            "id": "derivatives-pricing",
            "title": "Pricing derivatives",
            "level": "Pro",
            "minutes": 11,
            "summary": "No-arbitrage and put-call parity, risk-neutral pricing, Black-Scholes, implied volatility, the smile and Monte Carlo pricing.",
            "body": """
A derivative's value depends on another asset, the **underlying**. Derivatives pricing starts from one idea: there should be no **arbitrage**, no way to make a riskless profit with no money down.

### Put-call parity

For European options (exercisable only at expiry) on a stock paying no dividends, with the same strike K and expiry T:

`C - P = S - K x e^(-r x T)`

C is the call price, P the put price, S the stock price and r the continuously compounded risk-free rate. The reason: a long call plus a short put pays exactly S_T - K at expiry, the same as owning the stock and owing K. Two positions with identical payoffs must cost the same today, or traders would buy the cheap one, sell the dear one and lock in a profit.

### Risk-neutral pricing

If an option can be hedged perfectly by trading the underlying, its price cannot depend on how much investors expect the stock to rise. So we can price it **as if** everyone were risk-neutral: assume the stock grows at the risk-free rate, compute the expected payoff, and discount it at the risk-free rate. This is a pricing trick, not a forecast.

### Black-Scholes

The Black-Scholes formula for a European call:

`C = S x N(d1) - K x e^(-r x T) x N(d2)`

`d1 = (ln(S/K) + (r + sigma^2 / 2) x T) / (sigma x sqrt(T)), d2 = d1 - sigma x sqrt(T)`

N() is the standard normal cumulative distribution. The inputs are price, strike, time, interest rate and **volatility (sigma)**. Only volatility is not directly observable. N(d2) is the risk-neutral probability that the call ends in the money; N(d1) is the call's delta (how much its price moves per 1 move in the stock). The model assumes constant volatility, continuous trading and lognormal prices without jumps.

### Implied volatility and the smile

Turn the formula around: given the market price, solve for the sigma that matches it. That is **implied volatility**. If Black-Scholes were exactly right, every strike would show the same implied volatility. In practice, equity index options show a **skew**: lower strikes (downside puts) have higher implied volatility, reflecting crash fears and demand for protection. Some markets show a more symmetric **smile**.

### Monte Carlo pricing

For complex payoffs, simulate many risk-neutral price paths, compute the payoff on each, average, and discount:

`S_T = S x e^((r - sigma^2 / 2) x T + sigma x sqrt(T) x Z), Z ~ standard normal`

The error shrinks with the square root of the number of paths: four times as many paths halves it.

> Common mistake: reading implied volatility as a forecast of realised volatility. It also contains a risk premium and supply and demand for options.
""",
            "example": {"title": "Worked example: Black-Scholes and put-call parity", "body": """
A one-year European option on Birchwood Mills: **S = 100, K = 100, r = 5%, sigma = 20%, T = 1**, no dividends.

1. d1 = (ln(1) + (0.05 + 0.04 / 2) x 1) / (0.20 x 1) = (0 + 0.07) / 0.20 = **0.35**
2. d2 = 0.35 - 0.20 = **0.15**
3. N(0.35) = 0.6368, N(0.15) = 0.5596
4. K x e^(-0.05) = 100 x 0.9512 = **95.12**
5. C = 100 x 0.6368 - 95.12 x 0.5596 = 63.68 - 53.23 = **10.45**

**Put by parity:** P = C - S + K x e^(-rT) = 10.45 - 100 + 95.12 = **5.57**

**Arbitrage check:** if the market put traded at 6.50 while the call stayed at 10.45, the put is too dear. Sell the put, buy the call and short the stock: you receive 6.50 + 100 - 10.45 = 96.05 today. Invested at 5% it grows to 96.05 x e^(0.05) = about 100.98. At expiry the call and short put combine to buy one share at 100, which closes the short stock. Profit about **0.98** with no risk, which is (6.50 - 5.57) x e^(0.05).
"""},
            "terms": [
                ("Arbitrage", "A set of trades that makes a riskless profit with no net money invested."),
                ("Put-call parity", "The no-arbitrage link between European call and put prices: C - P = S - K x e^(-rT) for a non-dividend stock."),
                ("Risk-neutral pricing", "Valuing a derivative as the expected payoff, assuming assets grow at the risk-free rate, discounted at that rate."),
                ("Implied volatility", "The volatility that makes an option-pricing model's price equal the option's market price."),
                ("Volatility skew", "The pattern where implied volatility differs by strike, typically higher for low-strike equity index options."),
                ("Monte Carlo simulation", "Pricing by simulating many random price paths, averaging the payoffs and discounting."),
            ],
            "cards": [
                ("State put-call parity for European options on a non-dividend stock.",
                 "C - P = S - K x e^(-rT). A long call plus a short put has the same payoff as owning the stock and owing the strike, so the two must cost the same today."),
                ("S = 100, K = 100, r = 5%, T = 1, call = 10.45. What must the European put be worth?",
                 "P = C - S + K x e^(-rT) = 10.45 - 100 + 100 x 0.9512 = 10.45 - 100 + 95.12 = 5.57."),
                ("What is the idea behind risk-neutral pricing?",
                 "If an option can be hedged with the underlying, its price cannot depend on investors' risk preferences, so we price it as the expected payoff under risk-free growth, discounted at the risk-free rate. It is a pricing method, not a forecast."),
                ("What are the five inputs to Black-Scholes, and which cannot be observed directly?",
                 "Stock price, strike, time to expiry, risk-free rate and volatility. Volatility is the one that cannot be observed and must be estimated or implied."),
                ("What do N(d1) and N(d2) mean for a call in Black-Scholes?",
                 "N(d1) is the call's delta, its price change per 1 move in the stock. N(d2) is the risk-neutral probability that the call ends in the money."),
                ("What is implied volatility?",
                 "The volatility you plug into an option model to make its price equal the market price. It reflects expected movement plus a risk premium and supply and demand for options."),
                ("What is the equity index volatility skew, and why does it exist?",
                 "Low-strike options (downside puts) trade at higher implied volatility than high strikes, reflecting crash risk and strong demand for portfolio protection."),
                ("How do you price an option by Monte Carlo, and how does accuracy improve?",
                 "Simulate many risk-neutral paths, compute each payoff, average and discount at the risk-free rate. Error falls with the square root of the number of paths, so four times as many paths halves it."),
                ("True or false: if Black-Scholes held exactly, all strikes would show the same implied volatility.",
                 "True. The model assumes one constant volatility, so the smile or skew seen in real markets shows where its assumptions, such as no jumps, fail."),
            ],
            "calc": "options",
            "links": [],
        },
    ],
}
