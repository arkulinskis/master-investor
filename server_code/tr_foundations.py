"""Track: Foundations. Content for Master Investor (see tools/CONTENT_BRIEF.md)."""

TRACK = {
    "id": "foundations",
    "title": "Foundations",
    "level": "Beginner",
    "blurb": "What investing is, how compounding, risk and fees shape your results, how a trade actually happens, "
             "and how to put together a simple first plan.",
    "lessons": [
        # ------------------------------------------------------------------
        {
            "id": "what-investing-is",
            "title": "What investing actually is",
            "level": "Beginner",
            "minutes": 6,
            "summary": "Owning versus lending, where investment returns really come from, and why only real returns count.",
            "body": """
Investing means putting money into something today because you expect it to give you more money later. Almost every investment is one of two things: you **own** part of something, or you **lend** money to someone.

### Owning and lending

- **Owning (equity):** a share is a small slice of a company. You get a share of its profits, paid as dividends or kept and reinvested, and your slice is worth more if the business grows. There is no promise: profits can shrink and the share price can fall a long way.
- **Lending (debt):** a bond or a savings deposit is a loan. The borrower promises to pay interest and give your money back on a set date. Your upside is capped at the agreed interest, but you are paid before owners if things go wrong.

### Where returns come from

Over the long run, returns come from real economic sources:

- **Dividends:** cash a company pays its owners out of profits.
- **Earnings growth:** if profits grow, the business is worth more, and the share price tends to follow over time.
- **Interest:** what borrowers pay lenders for the use of their money.

On top of these sits a fourth, less reliable source: a change in what people are willing to pay for each unit of profit. That can add to or subtract from returns for years, but it does not compound forever.

### Saving, investing and speculating

**Saving** keeps money safe and available, usually in a bank account, and accepts a low return. **Investing** accepts ups and downs in exchange for a share of dividends, earnings growth or interest over years. **Speculating** is betting on a price move, often short term, where the return depends mainly on someone else paying more later rather than on what the asset produces.

### Real versus nominal

A **nominal** return is the number you see on your statement. A **real** return is what is left after inflation, and it is what decides what your money can buy.

`real return = (1 + nominal return) / (1 + inflation) - 1`

> Rule of thumb: real return is roughly nominal return minus inflation. A 2% savings rate with 3% inflation is a loss of buying power, even though the balance goes up.
""",
            "example": {
                "title": "Worked example: one year owning versus lending 2,000",
                "body": """
**Owning.** You buy 100 shares of Harbour Bakeries (a fictional company) at 20 each, so 2,000 in total.

- The company pays a dividend of 0.60 per share: 100 x 0.60 = **60**.
- Profits grow 5% and the share price rises from 20 to 21: 100 x 1 = **100** gain.
- Total return: (60 + 100) / 2,000 = **8%** nominal.

**Lending.** Instead, you buy a 2,000 bond paying 4% interest: **80** a year, plus your 2,000 back at the end.

**After inflation.** Inflation is 3% that year.

- Shares: 1.08 / 1.03 - 1 = 0.0485, so about **4.9%** real.
- Bond: 1.04 / 1.03 - 1 = 0.0097, so about **1.0%** real.

The shares did better this year, but the 100 price gain was not promised. In a bad year the price could have fallen to 16, wiping out far more than the dividend. The bond's 80 was promised, provided the borrower stays able to pay.
""",
            },
            "terms": [
                ("Equity", "Ownership in a company, usually held as shares, which entitles you to a slice of its profits and its value."),
                ("Bond", "A loan to a government or company that pays agreed interest and returns the amount lent on a set date."),
                ("Dividend", "A cash payment a company makes to its shareholders out of its profits."),
                ("Nominal return", "The return before adjusting for inflation: the change you see in your account balance."),
                ("Real return", "The return after inflation, which measures the change in what your money can buy."),
                ("Speculation", "Buying something mainly to profit from a price move, rather than from what the asset produces."),
            ],
            "cards": [
                ("What is the basic difference between owning a share and owning a bond?",
                 "A share makes you a part owner with an uncapped but unpromised claim on profits. A bond makes you a lender with a promised, capped return of interest plus your money back, and you are paid before owners if the borrower struggles."),
                ("Name the three main economic sources of investment returns.",
                 "Dividends paid out of profits, growth in company earnings (which tends to lift share prices over time), and interest paid by borrowers."),
                ("Your savings account pays 2% and inflation is 3%. Are you getting richer?",
                 "No. Your balance grows, but your real return is about (1.02 / 1.03) - 1 = minus 1% a year, so your money buys a little less each year."),
                ("What separates investing from speculating?",
                 "Investing relies on what an asset produces over time (dividends, earnings growth, interest). Speculating relies mainly on someone paying a higher price later, often over a short period."),
                ("A stock pays a 0.50 dividend and rises from 25 to 26 in a year. What is the total return?",
                 "(0.50 + 1.00) / 25 = 6%. Total return counts both the income and the price change."),
                ("True or false: a rising price-to-earnings ratio is a reliable long-term source of returns.",
                 "False. Changes in what people pay per unit of profit can add to or cut returns for years, but they swing both ways and cannot compound forever. Dividends and earnings growth are the durable sources."),
                ("Why are lenders paid before owners when a company fails?",
                 "Debt is a legal promise to pay; equity is a claim on whatever is left after all debts are paid. That priority is why bonds are usually less risky than shares, and also why their return is capped."),
            ],
            "calc": None,
            "links": [
                ("Investor.gov: Introduction to investing", "https://www.investor.gov/introduction-investing"),
            ],
        },
        # ------------------------------------------------------------------
        {
            "id": "compounding",
            "title": "Compounding and the time value of money",
            "level": "Beginner",
            "minutes": 7,
            "summary": "Why money now is worth more than money later, and how growth on growth builds wealth over decades.",
            "body": """
Compounding means earning returns on your past returns. In year one you earn on what you put in; in year two you earn on that plus last year's gain. Over long periods the growth on growth becomes larger than the growth on your original money.

### Future value and present value

The **future value** of a sum is what it grows to at a yearly return r after n years:

`FV = PV x (1 + r)^n`

Turn the formula round and you get the **present value**: what a future sum is worth today.

`PV = FV / (1 + r)^n`

This is the **time value of money**: 1,000 today is worth more than 1,000 in five years, because today's 1,000 could be invested and grow in the meantime. Present value is the foundation of bond pricing and company valuation later in the course.

### The rule of 72

A quick way to estimate doubling time: divide 72 by the yearly return in percent.

`years to double = 72 / return in %`

At 6% money doubles in about 12 years, at 9% in about 8. The rule is a close approximation for returns between roughly 4% and 12%.

### Regular contributions

Most people invest a bit at a time. If you add the same amount P at the end of every year, the total grows to:

`FV = P x ((1 + r)^n - 1) / r`

Add this to the growth of any starting sum to get the full picture. Time matters more than almost anything else: money added in your twenties has decades longer to compound than money added in your fifties.

### Inflation works the same way

Inflation compounds too, but against you. At 3% a year, prices roughly double in 24 years (72 / 3). That is why long-term plans should be judged in real terms: grow the money with the real return, or deflate the future total by the inflation factor.

> Common mistake: assuming returns arrive smoothly. These formulas use an average yearly return; real markets jump around, and a bad decade near the end of a plan matters more than one at the start.
""",
            "example": {
                "title": "Worked example: 10,000 plus 2,400 a year for 30 years at 7%",
                "body": """
**Starting sum.** 10,000 invested at 7% a year for 30 years.

- Growth factor: 1.07^30 = 7.612
- FV = 10,000 x 7.612 = **76,123**

**Contributions.** 2,400 added at the end of every year (200 a month, simplified to yearly).

- ((1.07^30) - 1) / 0.07 = (7.612 - 1) / 0.07 = 94.46
- FV = 2,400 x 94.46 = **226,706**

**Total:** 76,123 + 226,706 = **302,829**. You paid in 10,000 + 30 x 2,400 = 82,000; the other 220,829 is compounded growth.

**Rule of 72 check.** 72 / 7 = 10.3 years to double. The exact answer is 10.2 years, so 30 years is close to three doublings: 2^3 = 8, near the 7.6 factor above.

**In today's money.** With 3% inflation, prices grow by 1.03^30 = 2.4273. So 302,829 / 2.4273 = about **124,760** in today's buying power.
""",
            },
            "terms": [
                ("Compounding", "Earning returns on earlier returns as well as on the money you originally invested."),
                ("Future value", "What a sum of money grows to at a given yearly return after a given number of years."),
                ("Present value", "What a future sum of money is worth today, found by discounting it at a chosen rate."),
                ("Time value of money", "The idea that money today is worth more than the same amount later, because it can be invested meanwhile."),
                ("Rule of 72", "A shortcut for doubling time: 72 divided by the yearly return in percent gives roughly the years needed."),
            ],
            "cards": [
                ("What does the rule of 72 tell you?",
                 "Roughly how many years money takes to double: 72 divided by the yearly return in percent. At 8% a year, about 9 years."),
                ("Write the future value formula for a single sum.",
                 "FV = PV x (1 + r)^n, where PV is the amount today, r the yearly return as a decimal and n the number of years."),
                ("What is 5,000 worth after 10 years at 7% a year?",
                 "5,000 x 1.07^10 = 5,000 x 1.967 = about 9,836. That is close to a doubling, as the rule of 72 predicts (72 / 7 = about 10 years)."),
                ("You will receive 50,000 in 10 years. At a 7% discount rate, what is it worth today?",
                 "PV = 50,000 / 1.07^10 = 50,000 / 1.967 = about 25,417."),
                ("Why is 1,000 today worth more than 1,000 in five years?",
                 "Because today's 1,000 can be invested and grow over the five years, and inflation will usually cut what 1,000 buys by then. That is the time value of money."),
                ("Who ends up with more at 65: someone who invests 2,000 a year from 25 to 35 and then stops, or someone who invests 2,000 a year from 35 to 65?",
                 "At typical stock-market returns of around 7%, the early starter often ends up with a similar or larger sum despite paying in a third as much, because their money compounds for ten extra years. Time in the market is the most powerful input."),
                ("At 3% inflation, roughly how long until prices double?",
                 "About 24 years, using the rule of 72: 72 / 3 = 24."),
                ("True or false: the compound formulas assume returns arrive smoothly every year.",
                 "True. They use a constant average return. Real returns vary a lot from year to year, so actual outcomes spread widely around the formula's answer."),
            ],
            "calc": "compound",
            "links": [
                ("Investor.gov compound interest calculator", "https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator"),
            ],
        },
        # ------------------------------------------------------------------
        {
            "id": "risk-and-return",
            "title": "Risk, return and diversification",
            "level": "Beginner",
            "minutes": 8,
            "summary": "What investment risk really means, why spreading your money works, and which risks markets pay you to take.",
            "body": """
Higher expected returns usually come with more risk. Understanding which risk, and how much, is the core of investing.

### Volatility and drawdowns

**Volatility** measures how much returns swing around their average, usually as the standard deviation of yearly returns. Broad stock markets have often had yearly volatility of roughly 15% to 20%; high-quality government bonds much less.

A **drawdown** is the fall from a previous peak to a low. Drawdowns are what investors actually feel, and the maths is unkind: losses need bigger gains to recover.

`gain needed to recover = 1 / (1 - loss) - 1`

A 20% loss needs a 25% gain to get back to even; a 50% loss needs 100%.

### Why diversification works

When you hold many investments that do not move in lockstep, their ups and downs partly cancel. The portfolio's volatility is lower than the average volatility of its parts, while its expected return is still the average of their returns. That is why diversification is often called the only free lunch in finance.

How well it works depends on **correlation**, a number from minus 1 to plus 1 that measures how closely two investments move together. The lower the correlation, the bigger the benefit. In a market crash, correlations between shares tend to rise, so diversification within shares helps less exactly when you want it most.

### Company risk and market risk

- **Company-specific risk:** a product flop, a fraud, a lawsuit. It hits one firm, and owning many firms dilutes it towards zero.
- **Market risk:** recessions, interest rate shocks, panics. It hits nearly everything at once and cannot be diversified away within the stock market.

### The risk you are paid for

Because anyone can remove company-specific risk cheaply by diversifying, markets do not reliably reward you for bearing it. The extra expected return of shares over safe assets is compensation for market risk that cannot be avoided. Holding a few stocks adds risk with no extra expected reward.

> Rule of thumb: judge a risk by asking whether it can be diversified away. If it can, you are probably not being paid to carry it.
""",
            "example": {
                "title": "Worked example: two funds, one portfolio",
                "body": """
Two fictional funds each expect a 7% return with 20% volatility. Their correlation is 0.3. You put half your money in each.

**Expected return:** 0.5 x 7% + 0.5 x 7% = **7%**. Mixing does not cost you return.

**Volatility:** for two assets with weights w1 and w2, volatilities s1 and s2 and correlation c:

`variance = w1^2 x s1^2 + w2^2 x s2^2 + 2 x w1 x w2 x c x s1 x s2`

- 0.25 x 0.04 + 0.25 x 0.04 + 2 x 0.5 x 0.5 x 0.3 x 0.2 x 0.2
- = 0.010 + 0.010 + 0.006 = 0.026
- Volatility = square root of 0.026 = **16.1%**

Same expected return, a quarter less volatility. With correlation 1 the answer would stay 20%; with correlation 0 it would be 14.1%.

**Drawdown check.** A 100,000 portfolio falls to 65,000: a 35% drawdown. To recover: 1 / 0.65 - 1 = **53.8%** gain needed.
""",
            },
            "terms": [
                ("Volatility", "How widely returns swing around their average, usually measured as the standard deviation of returns."),
                ("Drawdown", "The percentage fall from a portfolio's or asset's previous peak to its later low."),
                ("Correlation", "A number from minus 1 to plus 1 measuring how closely two investments move together."),
                ("Diversification", "Spreading money across many investments so that their individual ups and downs partly cancel out."),
                ("Market risk", "Risk that affects almost all investments at once, such as recessions, and cannot be diversified away within a market."),
                ("Company-specific risk", "Risk that affects a single company, such as a failed product or fraud, which diversification can largely remove."),
            ],
            "cards": [
                ("Your portfolio falls 50%. What gain do you need to get back to where you were?",
                 "100%. Using 1 / (1 - 0.5) - 1 = 1. Losses need proportionally bigger gains to recover, which is why limiting drawdowns matters."),
                ("Why does diversification lower risk without lowering expected return?",
                 "The expected return of a mix is the weighted average of its parts, but its volatility is lower than the average because investments that do not move in lockstep partly cancel each other's swings."),
                ("What is the difference between company-specific risk and market risk?",
                 "Company-specific risk hits one firm (a fraud, a failed product) and fades as you own more companies. Market risk hits nearly everything at once (a recession) and cannot be diversified away within the market."),
                ("Why are investors not reliably paid for holding company-specific risk?",
                 "Because anyone can remove it cheaply by diversifying, so the market has no reason to offer extra expected return for carrying it. The equity premium compensates for market risk."),
                ("True or false: diversification works just as well in a crash as in normal times.",
                 "False. In crashes, correlations between shares tend to rise, so holding many shares helps less exactly when it is most wanted. Assets such as high-quality government bonds have often behaved differently in those periods, but not always."),
                ("What does a correlation of 0.3 between two funds mean?",
                 "They tend to move in the same direction but only loosely. A low positive correlation like this still gives a large diversification benefit."),
                ("Two funds each have 20% volatility and a correlation of 1. What is the volatility of a 50/50 mix?",
                 "20%. With perfect correlation the funds move in lockstep, so mixing them gives no diversification benefit."),
                ("What is a drawdown?",
                 "The fall from a previous peak to a later low, in percent. A portfolio that drops from 100,000 to 70,000 has a 30% drawdown."),
            ],
            "calc": None,
            "links": [
                ("Investor.gov: Asset allocation", "https://www.investor.gov/introduction-investing/getting-started/asset-allocation"),
            ],
        },
        # ------------------------------------------------------------------
        {
            "id": "funds-and-fees",
            "title": "Index funds, ETFs and the cost of fees",
            "level": "Beginner",
            "minutes": 8,
            "summary": "How funds pool money, why small yearly fees grow into large sums, and what the evidence says about active versus passive.",
            "body": """
A **fund** pools money from many investors and buys a basket of investments. One purchase gives you a slice of hundreds or thousands of companies, which is the cheapest way to diversify.

### Index funds and ETFs

An **index fund** simply holds the shares in a market index, such as a list of the largest companies in a country, in the same proportions. It does not try to pick winners, so it needs few staff and trades little. This is called **passive** investing.

An **ETF** (exchange-traded fund) is a fund whose units trade on a stock exchange during the day like a share. Many ETFs track indexes, but not all do. A traditional mutual fund, by contrast, is bought and sold once a day at a price set after the market closes.

### Fees compound too

Every fund charges an **expense ratio**: a yearly fee taken as a percentage of your money. Broad index funds often charge under 0.2% a year; many actively managed funds charge 0.5% to 1.5% or more.

The fee is taken every year from the whole balance, so it compounds against you. Roughly:

`your return = market return - fees - trading costs`

A 1% fee sounds small but, over 30 years, it can take around a quarter of your final wealth.

### Active versus passive: the evidence

An **active** fund manager tries to beat the index by choosing shares. Before costs, active managers as a group own the market, so they must earn the market return on average. After their higher fees, the average active dollar must trail the average passive dollar. Long-running studies, such as the S&P SPIVA scorecards, have repeatedly found that most active funds lag their benchmark over long periods, and that past winners rarely keep winning. Some managers do beat the market, but identifying them in advance has proved very hard.

### Tax-advantaged accounts

Many countries offer accounts where investments grow free of tax, or where contributions reduce your tax bill: for example the 401(k) and IRA in the United States, the ISA and SIPP in the United Kingdom, the TFSA and RRSP in Canada, and superannuation in Australia. Rules and limits differ and change, so check your own country's current rules.

> Rule of thumb: you cannot control market returns, but you can control costs. Compare expense ratios before anything else.
""",
            "example": {
                "title": "Worked example: a 0.05% fund versus a 1% fund over 30 years",
                "body": """
Assume the market returns 7% a year before fees. Fund A charges 0.05%, Fund B charges 1%.

**A single 10,000 investment:**

- Fund A: 10,000 x 1.0695^30 = **75,063**
- Fund B: 10,000 x 1.06^30 = **57,435**
- Gap: **17,628**, so Fund B leaves you about 23% less.

**Adding 6,000 at the end of every year:**

- Fund A: 6,000 x (1.0695^30 - 1) / 0.0695 = **561,692**
- Fund B: 6,000 x (1.06^30 - 1) / 0.06 = **474,349**
- Gap: **87,342** on the contributions alone.

The 0.95% fee gap looks tiny in any one year (95 on a 10,000 balance), but it is paid on a growing balance every year and loses the growth it would have earned. For Fund B to come out ahead, its manager would need to beat the market by more than 0.95% a year, every year, after trading costs.
""",
            },
            "terms": [
                ("Index fund", "A fund that holds the same investments as a market index, in the same proportions, instead of picking shares."),
                ("ETF", "Exchange-traded fund: a fund whose units are bought and sold on a stock exchange during the day, like a share."),
                ("Expense ratio", "The yearly fee a fund charges, expressed as a percentage of the money you have invested in it."),
                ("Active management", "Choosing investments in an attempt to beat a market index, usually at a higher fee than an index fund."),
                ("Tax-advantaged account", "An account where investments grow free of tax or contributions reduce tax, such as an ISA, TFSA or 401(k)."),
            ],
            "cards": [
                ("What is an expense ratio?",
                 "The yearly fee a fund takes as a percentage of your balance. A 0.2% expense ratio costs 20 a year for every 10,000 invested, taken from the fund's value."),
                ("Why must the average actively managed dollar trail the average passive dollar after costs?",
                 "Before costs, all investors together own the market and earn its return. Passive investors get that return minus small fees, so active investors as a group get it minus larger fees and trading costs."),
                ("10,000 grows at 7% for 30 years. Roughly how much does a 1% yearly fee cost by the end?",
                 "With no fee: 10,000 x 1.07^30 = about 76,100. With a 1% fee: 10,000 x 1.06^30 = about 57,400. The fee costs about 18,700, roughly a quarter of the outcome."),
                ("What is the difference between an ETF and a traditional mutual fund?",
                 "An ETF trades on an exchange throughout the day at market prices, like a share. A traditional mutual fund is bought or sold once a day at a price set after the market closes."),
                ("True or false: a fund that beat the market for the last five years will probably do so again.",
                 "False. Studies such as S&P's persistence scorecards find that past outperformance rarely continues; few top funds stay on top in later periods."),
                ("Name tax-advantaged accounts from three different countries.",
                 "For example: the 401(k) or IRA in the United States, the ISA or SIPP in the United Kingdom, the TFSA or RRSP in Canada, and superannuation in Australia."),
                ("Why is an index fund usually cheaper to run than an active fund?",
                 "It just copies an index, so it needs no team of analysts and trades only when the index changes. Less research and less trading mean lower costs."),
            ],
            "calc": "compound",
            "links": [
                ("S&P Dow Jones Indices: SPIVA research", "https://www.spglobal.com/spdji/en/research-insights/spiva/"),
            ],
        },
        # ------------------------------------------------------------------
        {
            "id": "how-a-trade-happens",
            "title": "How a trade happens",
            "level": "Beginner",
            "minutes": 7,
            "summary": "Exchanges, brokers, the bid and ask, the main order types, settlement and fractional shares.",
            "body": """
When you press Buy in an app, a chain of firms turns that click into shares you own.

### Exchanges and brokers

An **exchange** is a marketplace where buyers and sellers meet, such as the New York Stock Exchange, the London Stock Exchange or the Toronto Stock Exchange. Individuals do not trade on exchanges directly: you open an account with a **broker**, which sends your order to an exchange or another trading venue and holds the shares for you.

### Bid, ask and spread

At any moment a share has two prices:

- the **bid**: the highest price someone is currently willing to pay
- the **ask** (or offer): the lowest price someone is currently willing to sell at

The gap is the **spread**, a hidden cost of trading. Large, heavily traded shares often have spreads of a cent or two; small or thinly traded ones can have much wider spreads.

`spread % = (ask - bid) / midpoint x 100`

### Order types

- **Market order:** buy or sell now at the best available price. It almost always fills, but the price is not guaranteed, especially in fast markets or thin shares.
- **Limit order:** buy at or below, or sell at or above, a price you set. You control the price, but the order may never fill.
- **Stop order (stop-loss):** becomes a market order once the price touches your stop level. It is used to limit losses, but if a share opens far below your stop after bad news, you are sold at that lower price.
- **Stop-limit order:** becomes a limit order at the stop level, so it protects the price but may not fill at all.

### Settlement

The trade happens instantly, but the legal transfer of cash and shares, called **settlement**, takes a little longer. The United States and Canada moved to T+1 (one business day after the trade) in May 2024; many other markets use T+2, with moves to T+1 planned.

### Fractional shares

Many brokers let you buy part of a share, such as 0.25 of a share priced at 400 for 100. This makes it easy to invest small, regular amounts. Check whether your broker lets you transfer fractional holdings elsewhere, as many do not.

> Common mistake: placing market orders in thinly traded shares or just after the market opens, when spreads are wide. A limit order protects you from a bad fill.
""",
            "example": {
                "title": "Worked example: buying 200 shares of Northwind Tools",
                "body": """
Northwind Tools (fictional) shows a bid of 49.98 and an ask of 50.02.

**Spread:** 50.02 - 49.98 = 0.04. Midpoint = 50.00. Spread % = 0.04 / 50.00 = **0.08%**.

**Market order to buy 200 shares:** you pay the ask, 200 x 50.02 = **10,004**. If you sold straight away at the bid you would get 200 x 49.98 = 9,996, an instant cost of **8** from the spread alone.

**Limit order to buy at 49.99:** it waits until a seller accepts 49.99. If it fills you pay 9,998, but if the price moves up and away it may never fill.

**Stop order at 45:** a month later bad news comes out overnight and the shares open at 41. Your stop triggers at the open and sells around **41**, not 45: 200 x (50.02 - 41) = **1,804** loss instead of the roughly 1,004 you planned for.

**Settlement:** you trade on a Monday. On T+1 the cash and shares change hands on Tuesday.
""",
            },
            "terms": [
                ("Broker", "A firm that holds your investment account and sends your orders to exchanges or other trading venues."),
                ("Bid-ask spread", "The gap between the highest price a buyer will pay and the lowest price a seller will accept."),
                ("Limit order", "An order to buy at or below, or sell at or above, a price you set; it may not fill."),
                ("Stop order", "An order that becomes a market order once the price reaches a set level, often used to limit losses."),
                ("Settlement", "The legal transfer of cash and securities after a trade, such as T+1, one business day later."),
                ("Fractional share", "A part of one share, letting you invest a fixed amount of money rather than a whole number of shares."),
            ],
            "cards": [
                ("A share has a bid of 19.90 and an ask of 20.10. What is the spread in percent?",
                 "0.20 spread over a 20.00 midpoint = 1%. Buying and then selling straight away would cost you about 1% before any commission."),
                ("What is the difference between a market order and a limit order?",
                 "A market order fills now at the best available price, which is not guaranteed. A limit order fills only at your price or better, which protects the price but may never fill."),
                ("Why might a stop-loss order at 45 sell your shares at 41?",
                 "A stop order becomes a market order once triggered. If the shares open at 41 after overnight news, the stop triggers there and sells at the next available price, around 41."),
                ("What does T+1 settlement mean?",
                 "The cash and shares legally change hands one business day after the trade date. The United States and Canada moved to T+1 in May 2024."),
                ("When you buy with a market order, do you usually pay the bid or the ask?",
                 "The ask, the lowest price a seller is offering. When you sell with a market order you usually receive the bid."),
                ("What job does a broker do?",
                 "It holds your account and your investments, and routes your orders to an exchange or another trading venue for execution."),
                ("True or false: a stop-limit order always gets you out of a falling share.",
                 "False. Once triggered it becomes a limit order, so if the price falls straight through your limit it will not fill and you keep the shares."),
                ("What is a fractional share, and why is it useful?",
                 "Part of a single share, such as 0.25 of a 400 share for 100. It lets small, regular amounts be fully invested, even in high-priced shares."),
            ],
            "calc": None,
            "links": [
                ("Investor.gov: Types of orders", "https://www.investor.gov/introduction-investing/investing-basics/how-stock-markets-work/types-orders"),
            ],
        },
        # ------------------------------------------------------------------
        {
            "id": "first-plan",
            "title": "Your first investing plan",
            "level": "Beginner",
            "minutes": 8,
            "summary": "An emergency fund, clear goals, an asset mix that fits your time horizon, regular automatic investing and the classic mistakes.",
            "body": """
A simple written plan beats a clever one you abandon. It answers four questions: what is the money for, when is it needed, how much risk fits, and how will you keep going.

### First, the foundations

- **Emergency fund:** keep a cash buffer, often suggested as three to six months of essential spending, in an easy-access account. Without it, a job loss or repair can force you to sell investments at a bad time.
- **Expensive debt:** paying off a card charging 20% a year is a guaranteed 20% return. Few investments can promise that.

### Goals and time horizon

Give each goal a purpose, an amount and a date: a home deposit in four years, retirement in thirty. The **time horizon**, how long until you need the money, decides how much short-term loss you can live with.

### Asset mix by horizon

Your **asset mix** (or asset allocation) is the split between shares, bonds and cash. Rough guide lines many planners use:

- **Under about 3 years:** mostly cash or short-term bonds; shares can fall a long way and stay down for years.
- **About 3 to 10 years:** a balanced mix of shares and bonds.
- **Over about 10 years:** mostly shares, if you can sit through drawdowns of 30% to 50% without selling.

The right mix is the one you will actually hold in a crash. A diversified index fund or a ready-made multi-asset fund can do most of the work.

### Invest regularly and automate

**Dollar-cost averaging** means investing a fixed amount on a schedule, such as every payday. You buy more units when prices are low and fewer when they are high. Studies of past markets find that investing a lump sum at once has usually beaten spreading it out, because markets rise more often than they fall, but regular investing is how most people invest from their wages anyway, and it reduces the risk of regret. Set up automatic transfers so investing happens before you can spend the money.

### Beginner mistakes

- Selling after a fall and buying after a rise
- Chasing last year's best fund or a hot tip
- Holding a few stocks instead of a diversified fund
- Ignoring fees and taxes
- Checking the portfolio daily

> Rule of thumb: rebalance back to your target mix once a year, not when headlines scare you.
""",
            "example": {
                "title": "Worked example: 300 a month into a fund for four months",
                "body": """
You invest 300 on the first of each month into a fictional index fund.

- Month 1: price 10, units bought 300 / 10 = **30**
- Month 2: price 12, units bought 300 / 12 = **25**
- Month 3: price 8, units bought 300 / 8 = **37.5**
- Month 4: price 10, units bought 300 / 10 = **30**

**Total:** 1,200 invested for 122.5 units.

**Your average cost:** 1,200 / 122.5 = **9.80** per unit.
**Average price over the four months:** (10 + 12 + 8 + 10) / 4 = **10.00**.

Your average cost is below the average price because the fixed 300 bought more units when the price was low. At the month 4 price of 10, your holding is worth 122.5 x 10 = **1,225**, a gain of 25, even though the price ended where it started.

**Plan check.** With a 4-year goal, this money would mostly sit in bonds or cash. With a 30-year goal, a mainly shares fund would fit, as long as an emergency fund is already in place.
""",
            },
            "terms": [
                ("Emergency fund", "Cash set aside for unexpected costs, often three to six months of essential spending, kept easy to reach."),
                ("Time horizon", "How long until you need the money you are investing, which shapes how much risk you can take."),
                ("Asset allocation", "How your money is split between asset types such as shares, bonds and cash."),
                ("Dollar-cost averaging", "Investing a fixed amount at regular intervals, regardless of the price at the time."),
                ("Rebalancing", "Selling some of what has grown and buying what has lagged to bring your mix back to its target."),
            ],
            "cards": [
                ("Why build an emergency fund before investing?",
                 "So an unexpected cost or job loss does not force you to sell investments, possibly at a loss during a downturn. It is often suggested as three to six months of essential spending in easy-access cash."),
                ("You invest 200 a month. The price is 20, then 25, then 16. What is your average cost per unit?",
                 "Units: 10 + 8 + 12.5 = 30.5 for 600 invested. Average cost = 600 / 30.5 = about 19.67, below the average price of 20.33."),
                ("Why should money needed in two years mostly not be in shares?",
                 "Shares can fall 30% or more and take years to recover. With a short time horizon there may be no time to wait for a recovery."),
                ("True or false: dollar-cost averaging has usually beaten investing a lump sum all at once.",
                 "False. In past market data, lump sum has more often come out ahead because markets rise more often than they fall. Regular investing mainly suits money earned over time and reduces regret."),
                ("Paying off a credit card at 20% interest is like earning what return?",
                 "A guaranteed 20% a year, since every unit repaid stops costing 20%. Few investments can match that without risk."),
                ("What does rebalancing do?",
                 "It sells some of what has grown and buys what has lagged, bringing the portfolio back to its target mix and keeping risk where you planned it."),
                ("Name three common beginner investing mistakes.",
                 "For example: selling after a fall and buying after a rise, chasing last year's best performer or hot tips, holding only a few stocks, ignoring fees, and checking the portfolio too often."),
                ("What should decide your asset mix?",
                 "Mainly your time horizon and how much loss you could sit through without selling. The right mix is the one you will actually hold in a crash."),
            ],
            "calc": "compound",
            "links": [
                ("Investor.gov: Save and invest", "https://www.investor.gov/introduction-investing/investing-basics/save-and-invest"),
            ],
        },
        # ------------------------------------------------------------------
        {
            "id": "spotting-hype",
            "title": "Spotting hype and too-good-to-be-true offers",
            "level": "Beginner",
            "minutes": 7,
            "summary": "The red flags in investing posts and pitches: guaranteed returns, urgency, unregistered sellers, paid promotion and pump and dump schemes.",
            "body": """
Social media is full of people selling investing ideas. Some are honest and some are useful, but surveys by investor protection bodies keep finding the same pattern: people who lean on online influencers tend to rate their own knowledge highly, score lower on basic quizzes and report more brushes with fraud. The defence is not to memorise every scam. It is to recognise a handful of red flags that almost every scam shares.

### The six red flags

- **Guaranteed returns.** Every real investment can lose money. "Guaranteed", "no risk" or "can't lose" next to a high return is the single clearest warning sign.
- **Returns that are too high or too smooth.** A steady 2% to 5% a week, every week, does not exist in real markets. Stock markets have averaged roughly 10% a year over the long run, with painful falls along the way.
- **Urgency and scarcity.** "Only 12 spots left", "price doubles at midnight", "DM me now". Pressure is there to stop you checking.
- **Unregistered sellers.** People who sell investments or give paid advice usually have to be registered with a regulator. A real firm can be looked up in a public register; a scammer often has only a nickname and a messaging app.
- **Paid promotion you can't see.** Influencers are often paid to push a coin, a stock or a trading course. Many countries require a clear disclosure, but plenty of posts skip it.
- **Cherry-picked proof.** A screenshot of one winning trade, a rented sports car, a profit chart with no dates or no losses. You see the wins they chose to show, never the full record.

### Pump and dump

A classic scheme: promoters quietly buy a tiny, thinly traded stock or token, hype it to their followers, then sell into the buying rush. The price collapses and the last buyers are left holding the loss. Signs include a company or coin you have never heard of, huge claims with no filings behind them, and a push to buy right now.

### A 30-second check

1. Can it lose money? If they say no, walk away.
2. Who is selling, and are they registered? Look them up yourself, not through a link they send.
3. Are they paid to promote it?
4. What would you see if you asked for the full record, losses included?

> Rule of thumb: the more a post makes you feel you'll miss out, the slower you should go.
""",
            "example": {
                "title": "Worked example: what 3% a week really means",
                "body": """
A post promises "a safe 3% a week". Compounded over a year:

- 1.03^52 = about **4.65**, so 1,000 becomes about 4,650 in one year.
- After two years: 1.03^104 = about **21.6**, so 1,000 becomes about 21,600.
- After five years, 1,000 would grow to more than 2 million.

If anyone could really do this, they would be one of the richest people alive within a decade and would have no need to sell spots in a chat group. Compare that with the stock market's long-run average of roughly 10% a year, which turns 1,000 into about 1,100 after one year, with some years down 20% or more.

The maths alone tells you the promise is false. No chart, testimonial or screenshot can change that.
""",
            },
            "terms": [
                ("Pump and dump", "A scheme where promoters hype a small stock or token they already own, then sell to the buyers they attracted, leaving them with the losses."),
                ("Ponzi scheme", "A fraud that pays earlier investors with money from newer investors instead of from real profits, and collapses when new money dries up."),
                ("Finfluencer", "A social media personality who talks about money and investing, sometimes paid to promote products without saying so."),
                ("Paid promotion", "Content someone was paid to publish. Many countries require it to be clearly labelled as an advert or sponsorship."),
                ("Registration check", "Looking up a seller or adviser in a regulator's public register, such as FINRA BrokerCheck in the US, before trusting them with money."),
            ],
            "cards": [
                ("A post from \"@WealthWizardKai\": \"Guaranteed 3% a week with my trading signals. 12 spots left, DM me today!\" What are the red flags?",
                 "Guaranteed returns (no real investment is guaranteed), an impossible return (3% a week is about 365% a year), and urgency plus scarcity (12 spots, today). Also an unknown seller who wants you in private messages, away from public scrutiny."),
                ("\"@MoonshotMaya\": \"$GLEAMCOIN is about to explode, 100x incoming! I just loaded up, get in before the announcement tomorrow!\" Red flags?",
                 "A pump and dump pattern: a little-known token, a huge promised gain, the promoter already holding it and urgency tied to a vague announcement. If the hype works, early holders sell to the late buyers and the price falls."),
                ("A video shows a trader beside a sports car with a screenshot of a 48,000 profit. \"My course shows you how. Only 499 this week.\" What is wrong with this as proof?",
                 "Cherry-picked proof: one winning trade with no full record, no losses and no dates. The car may be rented. The real business may be selling the course, and a discount that ends this week is urgency."),
                ("\"Join our investment club. Members earn 20% a month, paid on time every time, and you get a bonus for each friend you bring.\" Red flags?",
                 "Returns that are far too high and far too smooth, plus rewards for recruiting. Paying old members with new members' money is how a Ponzi scheme works; it collapses when recruiting slows."),
                ("A finance influencer posts: \"Honest review: QuickGrow Pro is the only app I trust with my money.\" There is no ad label. What should you ask?",
                 "Whether it is paid promotion. Many countries require sponsored posts to be clearly labelled, but undisclosed deals are common. Look for an ad label or a disclosure, and treat glowing reviews with no downsides as marketing."),
                ("\"I'm a licensed broker with 20 years at a top bank. Send funds to my personal wallet and I'll manage them for you.\" How do you check?",
                 "Look the person up yourself in the regulator's public register, such as FINRA BrokerCheck in the US or the FCA register in the UK, not through a link they send. A real firm never asks you to send money to a personal account or wallet."),
                ("\"Tiny company Northwind Lithium is about to sign a deal with a huge carmaker. Buy before Monday!\" The stock trades a few thousand shares a day. Red flags?",
                 "A thinly traded tiny stock, an exciting rumour with no filing or official news behind it, and a deadline. That is the classic set up for a pump and dump. Check the company's official filings and press releases first."),
                ("A friend forwards: \"Bot trading AI, zero risk, you can withdraw any time, returns of 1% a day.\" Which words give it away?",
                 "\"Zero risk\" and \"1% a day\". No real investment has zero risk, and 1% a day compounds to about 37 times your money in a year. Fake trading platforms often show growing balances on screen but block or delay withdrawals."),
                ("A post says: \"Last year my picks returned 212%. Subscribe for this year's picks.\" What would you want to see before believing it?",
                 "The full record: every pick, with dates, entry and exit prices and the losers, ideally audited or at least public in advance. Big claimed returns with no complete, checkable history are cherry picking or simply made up."),
            ],
            "calc": None,
            "links": [
                ("FINRA: social media influenced investing", "https://www.finra.org/rules-guidance/key-topics/fintech/report/social-media-influenced-investing"),
                ("FINRA BrokerCheck: look up a broker", "https://brokercheck.finra.org/"),
                ("Investor.gov: protect your investments", "https://www.investor.gov/"),
            ],
        },
    ],
}
