"""Track: Portfolio and risk. Content for Master Investor (see tools/CONTENT_BRIEF.md)."""

TRACK = {
    "id": "portfolio",
    "title": "Portfolio and risk",
    "level": "Intermediate",
    "blurb": "How to combine investments into a portfolio, measure and size risk, keep costs and taxes down, and stop "
             "your own brain from wrecking the plan.",
    "lessons": [
        {
            "id": "asset-allocation",
            "title": "Asset allocation",
            "level": "Intermediate",
            "minutes": 8,
            "summary": "How the split between stocks, bonds, cash and other assets drives most of your risk, and how horizon and temperament shape it.",
            "body": """
**Asset allocation** is how you divide your money between broad types of investment. For a diversified investor, it explains most of how bumpy the ride is: a portfolio that is 90% shares behaves very differently from one that is 30% shares, whichever funds you pick.

### The main building blocks

- **Stocks (shares)**: the highest expected long-run return of the big asset classes, with deep falls along the way. Drops of a third or more have happened several times in major markets.
- **Bonds**: lower expected return, smaller swings. High-quality government bonds have often held up or risen when stocks fell, though not always (both fell together when inflation and rates jumped).
- **Cash**: stable in value and instantly available, but tends to lose to inflation over long periods.
- **Others**: property, commodities, gold and alternatives can add diversification but bring their own risks, costs and complexity.

### Horizon and risk tolerance

Two questions shape the mix:

1. **When will you need the money?** Money needed in two years should not depend on the stock market. Money for 30 years from now can ride out several crashes.
2. **How much loss can you live with, in money and in nerves?** Risk tolerance is not what you say on a calm day; it is what you do when your portfolio is down 30%. Selling at the bottom turns a temporary fall into a permanent loss.

### Global diversification and home bias

Investors everywhere tend to hold far more of their own country's shares than its weight in world markets. This **home bias** concentrates risk in one economy, one currency and often a handful of big local companies. A global index fund spreads money across thousands of firms in many countries.

### Sample allocations (explained, not recommended)

- **Conservative, around 30/70 stocks/bonds**: smaller falls, lower expected growth; often used by people drawing income soon.
- **Balanced, around 60/40**: a long-used middle point.
- **Growth, around 90/10**: for long horizons and strong nerves.

Some people use rules like "hold your age in bonds" as a rough starting point; these are conventions, not laws.

> Rule of thumb: pick an allocation you can stick with in a crash. A slightly lower-return plan you keep beats a higher-return plan you abandon at the worst moment.
""",
            "example": {"title": "Worked example: the same crash, three portfolios", "body": """
Imagine a bad year: stocks **-40%**, bonds **+5%**, cash **0%**. Each portfolio starts at **100,000**.

**Growth, 90/10 stocks/bonds**
- 0.9 x (-40%) + 0.1 x 5% = -36% + 0.5% = **-35.5%**, ending at 64,500

**Balanced, 60/30/10 stocks/bonds/cash**
- 0.6 x (-40%) + 0.3 x 5% + 0.1 x 0% = -24% + 1.5% = **-22.5%**, ending at 77,500

**Conservative, 30/70 stocks/bonds**
- 0.3 x (-40%) + 0.7 x 5% = -12% + 3.5% = **-8.5%**, ending at 91,500

Ask yourself honestly which loss you could watch without selling. That answer matters as much as the expected return.
"""},
            "terms": [
                ("Asset allocation", "How a portfolio is divided between broad asset classes such as stocks, bonds and cash."),
                ("Asset class", "A group of investments that behave similarly, such as shares, bonds, cash or property."),
                ("Risk tolerance", "How much loss you can bear, financially and emotionally, without abandoning your plan."),
                ("Investment horizon", "How long until you need the money you are investing."),
                ("Home bias", "The tendency to hold far more of your own country's investments than its share of world markets."),
            ],
            "cards": [
                ("What decides most of how bumpy a diversified portfolio's ride is?", "Its asset allocation, especially the share in stocks versus bonds and cash, more than which individual funds are chosen."),
                ("A 70/30 stocks/bonds portfolio: stocks fall 30%, bonds rise 4%. What is the portfolio return?", "0.7 x (-30%) + 0.3 x 4% = -21% + 1.2% = -19.8%."),
                ("Why should money needed in two years usually not be in stocks?", "Stocks can fall by a third or more and take years to recover. With a short horizon there may be no time to wait for a recovery."),
                ("What is home bias and why is it a risk?", "Holding much more of your own country's shares than its weight in world markets. It concentrates your wealth in one economy, one currency and often a few large local firms."),
                ("True or false: risk tolerance is what you say on a questionnaire.", "Mostly false. Real risk tolerance shows in what you do when your portfolio is down sharply. Many people overestimate it in calm markets."),
                ("Do high-quality government bonds always rise when stocks fall?", "No. They often have, but when inflation and interest rates jump, bonds and stocks can fall together."),
                ("Why might a lower-return allocation give you a better result than a higher-return one?", "If you can stick with it through a crash. Selling a riskier portfolio at the bottom locks in losses and can leave you far worse off than steady, lower expected returns."),
            ],
            "calc": "compound",
            "links": [
                ("Investor.gov: asset allocation and diversification", "https://www.investor.gov/introduction-investing/getting-started/asset-allocation"),
            ],
        },
        {
            "id": "modern-portfolio-theory",
            "title": "Modern portfolio theory",
            "level": "Advanced",
            "minutes": 11,
            "summary": "How correlation lets you cut risk for free, the efficient frontier and tangency portfolio, CAPM, and where the theory breaks down.",
            "body": """
**Modern portfolio theory (MPT)**, introduced by Harry Markowitz in the 1950s, treats a portfolio as a whole rather than a pile of separate bets. Its key insight: combining assets that do not move together lowers risk without necessarily lowering return.

### Expected return and correlation

A portfolio's **expected return** is simply the weighted average of its assets' expected returns. Its risk is not. For two assets with weights w1 and w2, volatilities s1 and s2, and correlation c:

`Variance = w1^2 x s1^2 + w2^2 x s2^2 + 2 x w1 x w2 x c x s1 x s2`

Portfolio volatility is the square root of the variance. **Correlation** runs from -1 to +1. At +1 the portfolio's volatility is just the weighted average; anything below +1 gives a lower figure. This free reduction is **diversification**.

### The efficient frontier and the tangency portfolio

Plot every possible mix of your assets by risk and expected return. The upper edge of that cloud is the **efficient frontier**: for each level of risk, the highest expected return available. Anything below it is beaten by some other mix.

Add a risk-free asset (such as short government bills) and draw a straight line from the risk-free rate that just touches the frontier. The touching point is the **tangency portfolio**: the mix with the best return per unit of risk (the highest Sharpe ratio). In theory, everyone holds that portfolio and adjusts risk only by adding cash or borrowing.

### CAPM

The **capital asset pricing model** follows: if everyone holds the market, only risk that cannot be diversified away, **systematic risk**, earns a reward. It is measured by beta, the asset's sensitivity to the market:

`Expected return = risk-free rate + beta x (market return - risk-free rate)`

Company-specific risk can be diversified away, so in CAPM it earns nothing extra.

### What MPT gets wrong

- **Unstable inputs**: expected returns are very hard to estimate, and optimisers amplify small errors into extreme, concentrated portfolios.
- **Fat tails**: MPT summarises risk with volatility, which assumes roughly normal returns. Real markets have more extreme days than a normal curve predicts.
- **Correlations rise in crises**: assets that looked unrelated often fall together when panic hits, just when diversification is needed most.
- **CAPM's record is weak**: in many studies, beta alone explains returns poorly; factors such as size and value were added later.

> Rule of thumb: keep the lesson (diversify across things that behave differently) and distrust the precise output of an optimiser.
""",
            "example": {"title": "Worked example: two assets, 60/40", "body": """
Fictional inputs: **Stock fund** expected return 8%, volatility 20%. **Bond fund** expected return 4%, volatility 8%. Correlation **0.2**. Weights 60% stocks, 40% bonds.

1. Expected return: 0.6 x 8% + 0.4 x 4% = **6.4%**
2. Variance:
   - 0.6^2 x 0.20^2 = 0.36 x 0.04 = 0.01440
   - 0.4^2 x 0.08^2 = 0.16 x 0.0064 = 0.001024
   - 2 x 0.6 x 0.4 x 0.2 x 0.20 x 0.08 = 0.001536
   - Total = **0.01696**
3. Volatility: square root of 0.01696 = **13.0%**
4. Weighted average of the volatilities: 0.6 x 20% + 0.4 x 8% = 15.2%. Diversification saved about **2.2 points** of volatility for the same 6.4% expected return.

**CAPM check**: risk-free rate 3%, expected market return 8%, a stock with beta 1.2: 3% + 1.2 x (8% - 3%) = **9%**.
"""},
            "terms": [
                ("Correlation", "A measure from -1 to +1 of how closely two assets' returns move together."),
                ("Efficient frontier", "The set of portfolios offering the highest expected return for each level of risk."),
                ("Tangency portfolio", "The portfolio on the efficient frontier with the highest return per unit of risk, where the line from the risk-free rate touches the frontier."),
                ("Capital asset pricing model (CAPM)", "A model where an asset's expected return equals the risk-free rate plus beta times the market risk premium."),
                ("Systematic risk", "Market-wide risk that cannot be removed by diversification."),
                ("Fat tails", "More frequent extreme returns than a normal distribution predicts."),
            ],
            "cards": [
                ("Two assets each with 10% volatility, 50/50 weights, correlation +1. What is the portfolio volatility?", "10%. With perfect correlation, portfolio volatility is just the weighted average, so there is no diversification benefit."),
                ("Two assets each with 10% volatility, 50/50 weights, correlation -1. What is the portfolio volatility?", "Zero: the variance is 0.25 x 0.01 + 0.25 x 0.01 - 2 x 0.25 x 0.01 = 0. Their moves cancel out exactly."),
                ("What is the efficient frontier?", "The upper edge of all possible portfolios plotted by risk and expected return: for each level of risk, the mix with the highest expected return."),
                ("What is the tangency portfolio?", "The risky portfolio with the highest Sharpe ratio, where a line from the risk-free rate just touches the efficient frontier. In theory you then adjust risk by adding cash or borrowing."),
                ("Risk-free rate 4%, market return 9%, beta 0.8: what does CAPM give as the expected return?", "4% + 0.8 x (9% - 4%) = 4% + 4% = 8%."),
                ("Why does CAPM say company-specific risk earns no reward?", "Because it can be diversified away for free by holding many stocks, so investors do not need to be paid for bearing it. Only systematic, market-wide risk is rewarded."),
                ("Why do portfolio optimisers often produce extreme, odd portfolios?", "Expected returns are very hard to estimate, and optimisers pile into whatever looks best, so small errors in the inputs become large, concentrated bets."),
                ("True or false: diversification works best in a market crash.", "False. Correlations between risky assets tend to rise in crises, so many holdings fall together just when diversification is most needed."),
            ],
            "calc": None,
            "links": [
                ("Kenneth French data library", "https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html"),
            ],
        },
        {
            "id": "risk-metrics",
            "title": "Measuring risk",
            "level": "Advanced",
            "minutes": 11,
            "summary": "Volatility, annualising with the square root of time, drawdowns, Sharpe, Sortino, beta, value at risk and expected shortfall.",
            "body": """
"Risk" means different things to different people: wild swings, a deep loss, or losing more than the market. Each metric below captures one of these, and none captures all of them.

### Volatility and the square root of time

**Volatility** is the standard deviation of returns: how widely returns spread around their average. If returns are roughly independent from one period to the next, variance grows in line with time, so volatility grows with the **square root of time**:

`Annual volatility = periodic volatility x sqrt(periods per year)`

Use 12 for monthly data and about 252 trading days for daily data. A 1% daily volatility is about 1% x 15.87 = 15.9% a year. Returns themselves scale with time, not its square root: a 0.8% average monthly return is roughly 9.6% a year.

### Drawdown

**Maximum drawdown** is the biggest fall from a peak to a later low. It is what investors feel. Losses need bigger gains to recover: a 50% fall needs a 100% gain to get back.

### Return per unit of risk

- **Sharpe ratio**: excess return over the risk-free rate, divided by volatility.

`Sharpe = (return - risk-free rate) / volatility`

- **Sortino ratio**: the same, but divided by **downside deviation**, which counts only returns below a target. It does not punish upside swings.

Both should use the same time unit for every input. A Sharpe ratio calculated from monthly figures can be annualised by multiplying by sqrt(12).

### Beta

**Beta** measures sensitivity to the market: the covariance of the asset with the market, divided by the market's variance. A beta of 1.3 means the asset has tended to move about 1.3% for each 1% market move. Beta says nothing about company-specific risk.

### Value at risk and expected shortfall

**Value at risk (VaR)** answers: "On a normal bad day, how much could we lose?" A one-day 95% VaR of 16,000 means losses should exceed 16,000 on only about 1 day in 20. It says nothing about *how much* worse those days are. **Expected shortfall** (also called CVaR) fills the gap: the average loss on the days beyond VaR. Regulators and risk managers increasingly prefer it.

> Common mistake: trusting VaR from a normal distribution. Real returns have fat tails, so extreme losses are more common than the model says.
""",
            "example": {"title": "Worked example: a fund's risk report", "body": """
A fictional fund, Harbour Balanced, has an average monthly return of **0.8%** and monthly volatility of **4%**. The risk-free rate is **3%** a year.

1. Annual return (simple): 0.8% x 12 = **9.6%**
2. Annual volatility: 4% x sqrt(12) = 4% x 3.464 = **13.86%**
3. Sharpe: (9.6% - 3%) / 13.86% = **0.48**
4. Sortino: annual downside deviation is **9%**, so (9.6% - 3%) / 9% = **0.73**
5. Drawdown: the fund peaked at 120,000 and fell to 84,000: (84,000 - 120,000) / 120,000 = **-30%**. To recover it needs 120,000 / 84,000 - 1 = **+42.9%**
6. One-day VaR on 1,000,000 with 1% daily volatility, assuming normal returns: 1.645 x 1% x 1,000,000 = **16,450** at 95%
7. Expected shortfall at 95% under the same assumption: about 2.06 x 1% x 1,000,000 = **20,600**
"""},
            "terms": [
                ("Volatility", "The standard deviation of returns, a measure of how widely they swing around their average."),
                ("Maximum drawdown", "The largest percentage fall from a peak to a subsequent low."),
                ("Sharpe ratio", "Excess return over the risk-free rate divided by volatility."),
                ("Sortino ratio", "Excess return over a target divided by downside deviation, so only harmful swings count as risk."),
                ("Beta", "An asset's sensitivity to market moves: its covariance with the market divided by the market's variance."),
                ("Value at risk (VaR)", "A loss level that should be exceeded only with a given small probability over a given period."),
                ("Expected shortfall", "The average loss in the cases worse than the VaR level."),
            ],
            "cards": [
                ("Monthly volatility is 5%. What is the annual volatility, assuming independent months?", "5% x sqrt(12) = 5% x 3.464 = about 17.3%. Volatility scales with the square root of time."),
                ("Daily volatility is 1.2%. What is the approximate annual volatility?", "1.2% x sqrt(252) = 1.2% x 15.87 = about 19%."),
                ("A fund returns 10% a year with 16% volatility; the risk-free rate is 2%. What is its Sharpe ratio?", "(10% - 2%) / 16% = 0.5."),
                ("How does the Sortino ratio differ from the Sharpe ratio?", "Sortino divides excess return by downside deviation, which counts only returns below a target, so upside volatility is not treated as risk."),
                ("A portfolio falls from 200,000 to 150,000. What is the drawdown and what gain is needed to recover?", "Drawdown = -25%. Recovery needs 200,000 / 150,000 - 1 = 33.3%."),
                ("A stock has a beta of 1.5. The market falls 8%. What move does beta suggest?", "About -12% (1.5 x -8%), on average. Company-specific news can make the actual move very different."),
                ("A one-day 99% VaR is 50,000. What does that mean, and what does it not tell you?", "Losses should exceed 50,000 on only about 1 day in 100. It does not say how large the losses are on those worst days; expected shortfall answers that."),
                ("Why can VaR built on a normal distribution understate risk?", "Real returns have fat tails: extreme days happen more often than a normal curve predicts, so actual large losses are more frequent than the model suggests."),
                ("True or false: returns, like volatility, scale with the square root of time.", "False. Average returns scale roughly in line with time (monthly x 12), while volatility scales with the square root of time (monthly x sqrt(12))."),
            ],
            "calc": "sharpe",
            "links": [],
        },
        {
            "id": "position-sizing",
            "title": "Position sizing",
            "level": "Advanced",
            "minutes": 10,
            "summary": "Equal weight, fixed fractional risk, volatility targeting and the Kelly criterion, and why most professionals bet half Kelly or less.",
            "body": """
Picking investments is half the job. Deciding **how much** to put in each is the other half. Good ideas sized badly can still ruin an account; average ideas sized well can survive long enough to work.

### Equal weight

The simplest rule: split the money evenly. With 20 holdings, each gets 5%. It needs no forecasts and avoids accidental concentration, but ignores that some holdings are far riskier than others.

### Fixed fractional

Risk a fixed small fraction of the account on each trade, often 0.5% to 2%. You decide where you would exit (the stop) and size the position so that hitting the stop costs that fraction:

`Shares = (account x risk %) / (entry price - stop price)`

Losses shrink as the account shrinks, which makes ruin very unlikely. Price gaps can jump past a stop, so the real loss can be larger.

### Volatility targeting

Size each holding so it contributes a similar amount of risk, or scale the whole portfolio to a chosen volatility:

`Weight = target volatility / asset volatility`

An asset with 25% volatility at a 10% target gets a 40% weight. When markets become wilder, positions shrink automatically.

### The Kelly criterion

For repeated bets, the **Kelly criterion** gives the fraction of capital that maximises long-run growth. For a bet that wins b times the stake with probability p and loses the stake otherwise:

`Kelly fraction = p - (1 - p) / b`

A coin that wins 60% of the time at even money (b = 1) gives 0.6 - 0.4 = 20% of capital per bet. If the fraction is zero or negative, there is no edge and Kelly says do not bet.

### Why half Kelly

Full Kelly maximises growth only if your inputs are exactly right, and in markets they never are. It also produces stomach-churning swings. Betting **more** than Kelly is worse than betting less: at about twice Kelly, expected long-run growth falls to roughly zero or below. Half Kelly gives up only about a quarter of the growth rate while roughly halving the volatility, so many professionals treat Kelly as a ceiling and use half or less.

> Common mistake: plugging an optimistic win rate into Kelly. Overestimating your edge pushes you into overbetting, the side that destroys capital.
""",
            "example": {"title": "Worked example: three sizing rules", "body": """
**Fixed fractional.** Account 50,000, risk 1% per trade = 500. Entry 40, stop 36, so risk per share is 4.
- Shares = 500 / 4 = **125**, a position worth 125 x 40 = **5,000** (10% of the account)

**Volatility targeting.** Target 10% portfolio volatility, asset volatility 25%.
- Weight = 10% / 25% = **40%** of the portfolio

**Kelly.** A strategy wins 60% of the time and wins or loses the same amount (b = 1).
- Kelly = 0.6 - 0.4 / 1 = **20%**
- Average log growth per bet: 0.6 x ln(1.2) + 0.4 x ln(0.8) = 0.1094 - 0.0893 = **2.01%**
- At half Kelly (10%): 0.6 x ln(1.1) + 0.4 x ln(0.9) = 0.0572 - 0.0421 = **1.50%**, about 75% of full Kelly's growth
- At double Kelly (40%): 0.6 x ln(1.4) + 0.4 x ln(0.6) = 0.2019 - 0.2043 = **-0.25%**: shrinking despite a real edge
"""},
            "terms": [
                ("Position sizing", "Deciding how much capital to put into each holding or trade."),
                ("Fixed fractional sizing", "Sizing each trade so that hitting the stop loses a fixed small fraction of the account."),
                ("Volatility targeting", "Scaling positions so each, or the whole portfolio, carries a chosen level of volatility."),
                ("Kelly criterion", "The bet fraction that maximises long-run compound growth given the win probability and payoff."),
                ("Half Kelly", "Betting half the Kelly fraction to cut volatility and the damage from overestimated edges."),
            ],
            "cards": [
                ("Account 80,000, risk 1% per trade, entry 25, stop 23. How many shares?", "Risk = 800. Risk per share = 2. Shares = 800 / 2 = 400, a 10,000 position."),
                ("What is the Kelly fraction for a 55% win rate at even money (b = 1)?", "0.55 - 0.45 / 1 = 0.10, so 10% of capital per bet."),
                ("Win rate 40%, wins pay 2 times the stake, losses lose the stake. What is the Kelly fraction?", "0.4 - 0.6 / 2 = 0.4 - 0.3 = 0.10, or 10%. A low win rate can still have an edge if wins are big enough."),
                ("Kelly gives a negative fraction. What does that mean?", "The bet has no positive edge, so Kelly says not to bet at all."),
                ("Why do professionals often bet half Kelly?", "Inputs are uncertain and full Kelly swings wildly. Half Kelly keeps about three quarters of the growth rate with roughly half the volatility, and protects against an overestimated edge."),
                ("Why is overbetting worse than underbetting relative to Kelly?", "Growth falls off faster above Kelly than below it. At about twice Kelly, expected long-run growth drops to roughly zero or below, even with a real edge."),
                ("Target volatility 12%, asset volatility 30%. What weight does volatility targeting give?", "12% / 30% = 40% of the portfolio."),
                ("True or false: a stop-loss guarantees your loss is capped at your planned risk.", "False. Prices can gap past a stop, for example overnight or on news, so the actual loss can be larger than planned."),
            ],
            "calc": "kelly",
            "links": [],
        },
        {
            "id": "rebalancing-and-taxes",
            "title": "Rebalancing, costs and taxes",
            "level": "Intermediate",
            "minutes": 9,
            "summary": "Keeping your mix on target by calendar, bands or new money, and why fees, tax-loss harvesting and asset location matter.",
            "body": """
Once you choose an allocation, markets immediately start pulling you away from it. If stocks boom, a 60/40 portfolio drifts to 70/30 and quietly becomes riskier than you planned. **Rebalancing** brings it back.

### Two ways to rebalance

- **Calendar rebalancing**: check and reset on a fixed schedule, such as once a year. Simple and easy to stick to.
- **Threshold (band) rebalancing**: act only when a holding drifts outside a band, for example more than 5 percentage points from target. Trades less often but needs regular checking.

Both work; studies broadly find no single best rule. Rebalancing too often adds costs; rarely, and risk drifts. Many people combine them: check yearly, act only if outside the band.

### Rebalance with new money first

If you are still adding money, send each new contribution to whatever is below target. You can often rebalance without selling anything, which avoids trading costs and taxable gains. Withdrawals can do the same in reverse.

### Costs compound too

Fees come out every year, so they compound against you:

`Ending value = start x (1 + return - fee)^years`

A 1% yearly fee sounds small but can take a large slice of the final pot over decades.

### Taxes: general principles

Tax rules differ by country, so check your own. Some ideas apply widely:

- **Tax-loss harvesting**: selling an investment below its cost to realise a loss that can offset taxable gains, then staying invested in something similar. It usually defers tax rather than removing it, because your new holding has a lower cost base.
- **Wash-sale-type rules**: several countries (including the US, UK and Canada) have rules that deny or delay the loss if you buy back the same or a substantially identical investment within a set period. The details differ.
- **Asset location**: holding the investments that are taxed most heavily (often interest-paying bonds) inside tax-advantaged accounts such as a 401(k) or IRA, an ISA, or a TFSA or RRSP, and more tax-efficient ones outside, where local rules allow.

> Common mistake: rebalancing in a taxable account by selling winners every few months. The tax bill can cost more than the drift ever would.
""",
            "example": {"title": "Worked example: drift, rebalancing and fees", "body": """
**Drift.** A 100,000 portfolio at 60/40. Stocks rise 25%, bonds are flat.
- Stocks 75,000, bonds 40,000, total 115,000. Stocks are now 75,000 / 115,000 = **65.2%**, outside a 5-point band.

**Rebalance by selling.** Target stocks = 60% x 115,000 = 69,000. Sell **6,000** of stocks and buy 6,000 of bonds.

**Rebalance with new money.** Instead, add 10,000 to bonds. Total 125,000: stocks 75,000 = **60%**, bonds 50,000 = **40%**. Back on target with no sales.

**Fees over 30 years.** 100,000 earning 6% before fees:
- No fee: 100,000 x 1.06^30 = **574,349**
- 1% fee: 100,000 x 1.05^30 = **432,194**
- The fee cost **142,155**, about a quarter of the no-fee result.
"""},
            "terms": [
                ("Rebalancing", "Trading or directing cash flows to bring a portfolio back to its target allocation."),
                ("Threshold rebalancing", "Rebalancing only when a holding drifts outside a set band around its target."),
                ("Tax-loss harvesting", "Selling an investment at a loss to offset taxable gains while staying invested in something similar."),
                ("Wash-sale rule", "A tax rule that denies or delays a loss if you buy back the same or a substantially identical investment too soon."),
                ("Asset location", "Placing investments in the account types where they are taxed least, given local rules."),
            ],
            "cards": [
                ("A 60/40 portfolio grows to stocks 84,000 and bonds 36,000. What are the weights now, and what trade restores 60/40?", "Total 120,000: stocks 70%, bonds 30%. Target stocks = 72,000, so sell 12,000 of stocks and buy 12,000 of bonds."),
                ("What is the difference between calendar and threshold rebalancing?", "Calendar rebalancing resets on a fixed schedule, such as yearly. Threshold rebalancing acts only when a holding drifts outside a set band, such as 5 points from target."),
                ("How can you rebalance without selling anything?", "Direct new contributions to whatever is below target (or take withdrawals from what is above). This avoids trading costs and realising taxable gains."),
                ("Why does a 1% annual fee matter so much over 30 years?", "It compounds: on 6% returns, 100,000 grows to about 574,000 without the fee but about 432,000 with it, a gap of roughly a quarter."),
                ("Does tax-loss harvesting eliminate tax?", "Usually not: it defers it. The replacement holding has a lower cost base, so more gain is taxed when it is eventually sold, though deferral itself has value."),
                ("What do wash-sale-type rules do?", "In several countries, they deny or delay a tax loss if you buy back the same or a substantially identical investment within a set period. The exact rules differ by country."),
                ("What is asset location?", "Putting heavily taxed holdings, often interest-paying bonds, in tax-advantaged accounts and more tax-efficient ones in taxable accounts, where local rules allow."),
                ("True or false: rebalancing more often is always better.", "False. Very frequent rebalancing adds trading costs and, in taxable accounts, tax bills, often without meaningfully reducing risk."),
            ],
            "calc": "compound",
            "links": [
                ("Investor.gov: mutual funds and their fees", "https://www.investor.gov/introduction-investing/investing-basics/investment-products/mutual-funds-and-exchange-traded-1"),
            ],
        },
        {
            "id": "behaviour",
            "title": "Your brain on markets",
            "level": "Intermediate",
            "minutes": 9,
            "summary": "The mental shortcuts that cost investors money, and practical process fixes: rules, checklists, pre-mortems and a written policy.",
            "body": """
Most investing mistakes are not about missing information. They come from predictable quirks in how people think about money and risk. Knowing the names helps a little; building a process that works around them helps a lot.

### The usual suspects

- **Loss aversion**: losses hurt more than equal gains feel good; experiments often find roughly twice as much. It makes people sell in panic or refuse to cut a bad position.
- **Overconfidence**: most people rate their skill above average. It leads to trading too much and holding too few stocks.
- **Recency bias**: giving recent events too much weight, such as assuming last year's winners will keep winning.
- **Anchoring**: fixing on an irrelevant number, often the price you paid. The market does not know or care what you paid.
- **Confirmation bias**: seeking out evidence that supports what you already believe and dismissing the rest.
- **Herding**: following the crowd because it feels safer, which feeds bubbles and panics.
- **Disposition effect**: selling winners too early and holding losers too long, partly to avoid admitting a loss.

### Process fixes

You cannot switch biases off, but you can make decisions before emotions are involved.

1. **Rules in advance**: decide your allocation, rebalancing bands and exit conditions while calm, and follow them when not.
2. **Checklists**: a short list of questions before every purchase (What is the thesis? What would prove it wrong? How big a position?) forces you to slow down.
3. **Pre-mortems**: imagine it is a year later and the investment has failed badly. Write down why. This surfaces risks that optimism hides.
4. **Decision journal**: record why you bought or sold and what you expected. Later, judge the reasoning, not just the outcome.
5. **Investment policy statement (IPS)**: a one-page document stating your goals, horizon, target allocation, rebalancing rules and what you will do in a crash.

### Ask the right question

For any holding, ask: "If I had cash today, would I buy this at this price?" If not, the price you paid is not a reason to keep it.

> Rule of thumb: automate whatever you can (regular contributions, rebalancing). Every decision you do not have to make is one your biases cannot spoil.
""",
            "example": {"title": "Worked example: the disposition effect in action", "body": """
You need to raise **10,000**. You hold two positions, each now worth 20,000:

- **Alder Foods**: bought for 15,385, up **30%**
- **Birch Robotics**: bought for 28,571, down **30%**

Most people sell Alder: it feels good to lock in a win, and selling Birch would mean admitting a loss. Run the checklist instead:

1. **Would I buy each today at this price?** Suppose your updated view is that Alder's outlook is still strong and Birch's thesis has broken.
2. **The anchor.** Birch must rise 28,571 / 20,000 - 1 = **42.9%** just to get back to what you paid. The market does not care about that number.
3. **Tax (where gains are taxed).** Selling Alder realises a gain of about 3,500 on the 10,000 sold (30/130 of the sale). Selling Birch realises a loss of about 4,300 on the 10,000 sold (30/70 of the sale), which may offset other gains.

On these assumptions, selling the loser is the better decision on both the thesis and the tax, even though it feels worse.
"""},
            "terms": [
                ("Loss aversion", "The tendency to feel losses more strongly than gains of the same size."),
                ("Disposition effect", "Selling winning investments too early and holding losing ones too long."),
                ("Anchoring", "Relying too heavily on a reference number, such as your purchase price, when making a decision."),
                ("Pre-mortem", "Imagining a decision has already failed and listing the reasons, to expose hidden risks before acting."),
                ("Investment policy statement (IPS)", "A short written plan setting out your goals, horizon, allocation, rebalancing rules and crisis behaviour."),
            ],
            "cards": [
                ("What is the disposition effect?", "Selling winners too early and holding losers too long, partly to avoid admitting a loss. It often leaves investors with their weakest holdings."),
                ("Why does your purchase price usually not matter for a sell decision?", "The market does not know what you paid. The only question is whether the investment is worth holding at today's price; using the purchase price is anchoring."),
                ("What is loss aversion and how does it hurt investors?", "Feeling losses more strongly than equal gains, often roughly twice as much in experiments. It drives panic selling and refusing to cut bad positions."),
                ("What is a pre-mortem?", "Before deciding, imagine the investment has failed badly a year from now and write down why. It brings out risks that optimism and confirmation bias hide."),
                ("What goes into an investment policy statement?", "Your goals, horizon, target allocation, rebalancing rules and what you will do in a crash, written while calm so you can follow it when markets are not."),
                ("Last year's best-performing fund is advertised everywhere. Which bias pulls you towards it?", "Recency bias, often with herding: giving recent results too much weight and following the crowd. Past top performance is a weak guide to future results."),
                ("Why judge decisions by your reasoning rather than the outcome?", "Good decisions can lose money and bad ones can win by luck. A decision journal lets you check whether your reasoning held up, which is what you can improve."),
                ("True or false: knowing about biases is enough to avoid them.", "False. Awareness helps a little, but biases act in the moment. Rules, checklists and automation set in advance work far better."),
            ],
            "calc": "crash",
            "links": [],
        },
    ],
}
