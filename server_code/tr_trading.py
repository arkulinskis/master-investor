"""Track: Trading. Content for Master Investor (see tools/CONTENT_BRIEF.md)."""

TRACK = {
    "id": "trading",
    "title": "Trading",
    "level": "Advanced",
    "blurb": "How short-term trading really works: edge, costs, market plumbing, risk per trade, the main strategy "
             "families and the process professionals use to stay honest.",
    "lessons": [
        # ------------------------------------------------------------------
        {
            "id": "trading-vs-investing",
            "title": "Trading versus investing",
            "level": "Advanced",
            "minutes": 8,
            "summary": "What separates trading from investing, why you need a measurable edge, and why costs and base rates matter so much.",
            "body": """
An investor buys a share of a business and expects to be paid by its growth and dividends over years. A trader tries to profit from price moves over minutes, days or weeks, and usually does not care what the business does as long as the price moves the right way. Both can be valid, but they win in different ways.

### Investing is positive-sum, trading is close to zero-sum

Over long periods the whole stock market has risen because companies earn profits. A buy-and-hold investor collects that return just by owning the market. Short-term trading is different: for every trader who buys too early there is someone on the other side, so before costs the gains and losses of traders roughly cancel out. **After costs, short-term trading as a group is negative-sum.** To win you must be better than the people you trade against, many of whom are professionals with faster data and cheaper execution.

### Edge and expectancy

An **edge** is a repeatable reason why your trades should make money on average. Expectancy measures it: the average profit or loss per trade over many trades.

`Expectancy = (win rate x average win) - (loss rate x average loss)`

A strategy can win only 35% of the time and still have positive expectancy if the wins are much larger than the losses. A strategy that wins 80% of the time can still lose money if the rare losses are huge.

### Costs eat thin edges

Every trade pays commissions, the bid-ask spread, slippage (getting a worse price than expected) and, in many countries, tax on short-term gains at a higher rate than long-term gains. A small edge per trade multiplied by hundreds of trades can vanish completely once costs are counted. The more often you trade, the larger your edge per trade has to be.

### The base rates

Large studies of retail day traders in several countries have consistently found that most of them lose money, that only a small minority earn profits that persist from year to year, and that many quit after losses. Treat this as your starting assumption: you need evidence that you are an exception, not hope.

> Common mistake: judging a strategy by a few good weeks. A handful of trades says almost nothing about expectancy; you need many trades, recorded honestly, with all costs included.
""",
            "example": {"title": "Worked example: a thin edge meets real costs", "body": """
A trader with a 25,000 account makes **500 trades a year**, each about 10,000 in size.

**Gross edge:** on average each trade makes 0.15% before costs.

- 0.15% x 10,000 = **15** per trade
- 15 x 500 = **7,500** a year

**Costs per trade:**

- Commission: 2 to buy + 2 to sell = 4
- Half the spread on entry and exit together: 0.05% x 10,000 = 5
- Slippage: 0.03% x 10,000 = 3
- Total = **12** per trade, or 12 x 500 = **6,000** a year

**Net:** 7,500 - 6,000 = **1,500**, which is 6% on the 25,000 account before tax. The net expectancy per trade is only 15 - 12 = 3.

If slippage rises to 0.06% in fast markets (6 per trade), costs become 15 per trade and the net result is **zero**. The same strategy run as 50 larger, longer trades would pay far less in total costs.
"""},
            "terms": [
                ("Edge", "A repeatable reason why a trading approach should make money on average after costs."),
                ("Expectancy", "The average profit or loss per trade over many trades: win rate x average win minus loss rate x average loss."),
                ("Zero-sum game", "A contest where one side's gains equal the other side's losses before costs; after costs it becomes negative-sum."),
                ("Base rate", "How often an outcome happens in a large group, used as a starting assumption before looking at your own case."),
                ("Day trading", "Opening and closing positions within the same trading day, so nothing is held overnight."),
            ],
            "cards": [
                ("Why is short-term trading described as roughly zero-sum before costs?",
                 "Over short horizons, one trader's gain on a price move is another trader's loss, so gains and losses largely cancel. Investors share in company profits over time, which makes long-term ownership positive-sum."),
                ("What is the expectancy formula?",
                 "Expectancy = (win rate x average win) - (loss rate x average loss). It is the average result per trade over many trades, and it must be positive after costs for a strategy to be worth running."),
                ("A strategy wins 40% of trades, average win 300, average loss 150. What is its expectancy?",
                 "0.40 x 300 - 0.60 x 150 = 120 - 90 = 30 per trade. It loses more often than it wins but still makes money on average because wins are twice the size of losses."),
                ("True or false: a strategy that wins 80% of its trades must be profitable.",
                 "False. If the 20% of losing trades are large enough, expectancy is negative. Win rate alone says nothing without the sizes of the average win and the average loss."),
                ("What do large studies of retail day traders consistently find?",
                 "Most lose money, only a small minority earn profits that persist from year to year, and many give up after losses. The sensible starting assumption is that you will be in the majority unless your records prove otherwise."),
                ("Why does trading more often demand a bigger edge per trade?",
                 "Each trade pays commissions, spread and slippage. More trades means more total cost, so a thin edge per trade can be wiped out once it is multiplied across hundreds of trades."),
                ("Name four costs a trader pays besides commission.",
                 "The bid-ask spread, slippage, financing costs on borrowed money or short positions, and often higher tax on short-term gains. All of them come out of the gross edge."),
                ("You made money on 12 trades in three weeks. Do you have an edge?",
                 "You cannot tell yet. A dozen trades is far too few to separate skill from luck; you need many trades, all costs counted, and ideally results that hold in different market conditions."),
            ],
            "calc": None,
            "links": [],
        },
        # ------------------------------------------------------------------
        {
            "id": "technical-analysis",
            "title": "Technical analysis, honestly",
            "level": "Advanced",
            "minutes": 9,
            "summary": "Trend, support and resistance, moving averages, RSI and volume, and what the research actually supports.",
            "body": """
Technical analysis studies prices and volume to make trading decisions, instead of studying the business. Some of its tools have real evidence behind them; many popular ones do not. This lesson covers both.

### The core tools

- **Trend:** a series of higher highs and higher lows (uptrend) or lower highs and lower lows (downtrend).
- **Support and resistance:** price zones where buying or selling has stopped a move before. They often line up with round numbers and earlier highs and lows, partly because many traders watch the same levels.
- **Moving averages:** the average closing price over the last N days, for example 50 or 200. A price above a rising 200-day average is a common definition of an uptrend.
- **RSI (relative strength index):** compares the size of recent gains to recent losses on a 0 to 100 scale, usually over 14 periods. Readings above 70 are called overbought and below 30 oversold.
- **Volume:** how many shares trade. A breakout on heavy volume is usually treated as more meaningful than one on thin volume.

`RSI = 100 - 100 / (1 + RS), where RS = average gain / average loss`

### What the evidence supports

The strongest evidence is for **momentum**. Cross-sectional momentum (buying the stocks that rose most over the past 3 to 12 months and selling those that fell most) has been documented in many countries and decades. Time-series momentum, or trend following (going long assets whose own past return is positive and short those with a negative one), has worked across stocks, bonds, currencies and commodities over long histories. Both can suffer sharp losses, especially when trends reverse suddenly.

Some moving-average rules looked profitable in older studies, but later work found much of the effect weakened once costs and data snooping (testing many rules and keeping the best) were accounted for.

### What the evidence does not support well

Most named chart patterns (head and shoulders, flags, triangles) and fixed RSI thresholds have weak or mixed evidence, especially after costs. Patterns are easy to see after the fact and hard to define precisely in advance, so it is easy to fool yourself.

> Rule of thumb: if you cannot write a rule as code that a computer could test on past data, you cannot know whether it works.
""",
            "example": {"title": "Worked example: RSI and a moving average", "body": """
Over the last 14 days, Northwind Tools shares had an **average daily gain of 1.20** on up days and an **average daily loss of 0.80** on down days (both averaged over the 14 days).

1. RS = 1.20 / 0.80 = **1.5**
2. RSI = 100 - 100 / (1 + 1.5) = 100 - 40 = **60**

60 is neither overbought nor oversold.

**Five-day moving average** of closes 41, 42, 40, 43, 44:

- (41 + 42 + 40 + 43 + 44) / 5 = 210 / 5 = **42**

The last close of 44 is above the average, so a simple trend rule would read this as an uptrend. Before trading on either signal, you would test the exact rule, with costs, on many years and many stocks.
"""},
            "terms": [
                ("Support and resistance", "Price zones where falls (support) or rises (resistance) have stalled before and that many traders watch."),
                ("Moving average", "The average closing price over the last N periods, recalculated each day, used to smooth out noise and define trend."),
                ("RSI", "Relative strength index: a 0 to 100 measure comparing recent average gains with recent average losses."),
                ("Cross-sectional momentum", "Buying the assets that rose most relative to others over the past months and selling those that fell most."),
                ("Time-series momentum", "Trend following: going long an asset whose own past return is positive and short one whose past return is negative."),
            ],
            "cards": [
                ("How is RSI calculated?",
                 "RS = average gain / average loss over a period (usually 14), then RSI = 100 - 100 / (1 + RS). It runs from 0 to 100; above 70 is called overbought, below 30 oversold."),
                ("Average gain 1.20, average loss 0.80. What is the RSI?",
                 "RS = 1.20 / 0.80 = 1.5, so RSI = 100 - 100 / 2.5 = 100 - 40 = 60."),
                ("Which technical idea has the strongest research support?",
                 "Momentum: both cross-sectional momentum (recent winners beating recent losers) and time-series momentum (trend following) have been documented across many markets and decades, though both suffer sharp crashes at times."),
                ("What is the difference between cross-sectional and time-series momentum?",
                 "Cross-sectional ranks assets against each other and buys the relative winners. Time-series looks at each asset on its own and goes long if its own past return is positive, short if negative."),
                ("True or false: research strongly supports head-and-shoulders and triangle patterns.",
                 "False. The evidence for most named chart patterns is weak or mixed, especially after costs, partly because the patterns are hard to define precisely before the fact."),
                ("Why might support and resistance levels sometimes work?",
                 "Many traders watch the same round numbers and earlier highs and lows and place orders there, so buying or selling can cluster at those levels. That makes them self-reinforcing at times, not reliable."),
                ("What is data snooping in technical analysis?",
                 "Testing many rules or settings on the same history and keeping the best. The winner often looks good by chance and fails on new data."),
                ("Why is volume watched alongside price?",
                 "A move on heavy volume shows many participants acting, so traders treat it as more meaningful than the same move on thin volume, which can be pushed around by a few orders."),
            ],
            "calc": None,
            "links": [],
        },
        # ------------------------------------------------------------------
        {
            "id": "microstructure",
            "title": "Market microstructure",
            "level": "Advanced",
            "minutes": 9,
            "summary": "How orders meet: the order book, liquidity, spreads, slippage, market makers, fees and why big orders move prices.",
            "body": """
Market microstructure is the plumbing of trading: how buy and sell orders meet and what that costs you.

### The order book

Most exchanges run a **limit order book**. A limit order says "buy up to 500 shares at 20.00 or better". Unfilled buy orders sit on the **bid** side, sell orders on the **ask** side. The best bid is the highest price someone will pay now; the best ask is the lowest price someone will sell at. The gap between them is the **spread**, and the midpoint is the **mid price**.

A **market order** says "fill me now at whatever price is available". It takes liquidity from the book, starting at the best price and walking up (or down) through the levels until it is filled.

### Liquidity, depth and slippage

**Liquidity** is how easily you can trade size without moving the price. **Depth** is how many shares are waiting at each price level. In a deep, liquid stock a large market order barely moves the price; in a thin one it can sweep through several levels. **Slippage** is the gap between the price you expected (often the mid or the last trade) and your average fill.

`Relative spread = (ask - bid) / mid`

### Market makers and fees

**Market makers** post both bids and asks and earn the spread, taking the risk of holding inventory and of trading with someone better informed. Many venues pay a small rebate to orders that **make** liquidity (resting limit orders) and charge a fee to orders that **take** it (market orders and marketable limits). This is the maker-taker model.

Some brokers that charge no commission are paid by wholesale market makers to send them retail orders. This **payment for order flow** is allowed in some markets (such as the United States) and banned or restricted in others (such as the UK). Critics worry it creates conflicts over execution quality; supporters say retail orders often get prices slightly better than the public quote.

### Why large orders move prices

A large buy order uses up the cheap offers and must pay higher prices. Other traders also notice persistent buying and raise their offers, because a big buyer may know something. This is **market impact**, and it is why professionals split big orders into many small ones.

> Rule of thumb: in a thin market use limit orders, and check the depth before you trade, not after.
""",
            "example": {"title": "Worked example: a market order walks the book", "body": """
The order book for Bluefin Logistics:

- Asks: 300 at 20.02, 1,000 at 20.03, 2,000 at 20.05
- Bids: 500 at 20.00, 800 at 19.99

Mid price = (20.00 + 20.02) / 2 = **20.01**. Spread = 0.02, relative spread = 0.02 / 20.01 = about **0.10%**.

You send a **market order to buy 2,000 shares**:

1. 300 x 20.02 = 6,006
2. 1,000 x 20.03 = 20,030
3. 700 x 20.05 = 14,035
4. Total = **40,071**, average price = 40,071 / 2,000 = **20.0355**

Slippage against the mid: 20.0355 - 20.01 = 0.0255 per share, or 0.0255 / 20.01 = about **0.13%**, which is 2,000 x 0.0255 = **51** in total. A limit order at 20.03 would have filled 1,300 shares and left 700 waiting.
"""},
            "terms": [
                ("Limit order book", "The list of resting buy and sell limit orders at each price, which incoming orders trade against."),
                ("Bid-ask spread", "The gap between the best price buyers are offering (bid) and the best price sellers are asking (ask)."),
                ("Slippage", "The difference between the price you expected and the average price you actually got."),
                ("Market maker", "A firm that continuously quotes both buy and sell prices and earns the spread in return for holding inventory risk."),
                ("Maker-taker fees", "A pricing model where resting limit orders that add liquidity get a rebate and orders that remove liquidity pay a fee."),
                ("Payment for order flow", "Money a market maker pays a broker for sending it customers' orders to execute."),
            ],
            "cards": [
                ("What is the difference between a limit order and a market order?",
                 "A limit order sets the worst price you will accept and may not fill. A market order fills immediately at the best available prices, so it is certain to fill but not certain of its price."),
                ("Bid 20.00, ask 20.02. What are the mid price and the relative spread?",
                 "Mid = (20.00 + 20.02) / 2 = 20.01. Relative spread = 0.02 / 20.01 = about 0.10%."),
                ("Asks: 300 at 20.02, 1,000 at 20.03, 2,000 at 20.05. What is the average price for a 2,000-share market buy?",
                 "300 x 20.02 + 1,000 x 20.03 + 700 x 20.05 = 6,006 + 20,030 + 14,035 = 40,071, so the average is 40,071 / 2,000 = 20.0355."),
                ("What is market depth and why does it matter?",
                 "Depth is the number of shares resting at each price level. Shallow depth means a sizable order sweeps through several levels and pays more slippage."),
                ("How do market makers earn money, and what risks do they take?",
                 "They buy at the bid and sell at the ask, earning the spread. They risk holding inventory while prices move and trading against better-informed traders."),
                ("In the maker-taker model, who pays and who gets paid?",
                 "Orders that take liquidity (market orders and marketable limits) pay a fee; resting limit orders that make liquidity usually receive a small rebate."),
                ("What is payment for order flow, and what is the concern?",
                 "A market maker pays a broker to route customer orders to it. Critics fear brokers may pick routing by payment rather than best execution; it is allowed in some countries and banned or restricted in others."),
                ("Why does a large order push the price against you?",
                 "It uses up the cheapest offers and must climb to worse prices, and other traders who see persistent buying raise their offers because a large buyer may be informed. This is market impact."),
            ],
            "calc": None,
            "links": [],
        },
        # ------------------------------------------------------------------
        {
            "id": "risk-per-trade",
            "title": "Risk per trade",
            "level": "Advanced",
            "minutes": 9,
            "summary": "Stops, R multiples, expectancy in R, the 1 to 2% rule and how to size a position from your stop distance.",
            "body": """
Professional traders decide how much they are willing to lose before they decide how much to buy. That order is what keeps a run of losses survivable.

### Stops and R

A **stop** (stop-loss) is the price at which you admit the trade idea is wrong and exit. The distance from entry to stop, times the number of shares, is your **initial risk**, called **1R**. Results are then measured in R multiples: a trade that makes twice the initial risk is +2R; a full stop-out is -1R. Thinking in R lets you compare trades of different sizes and prices.

Expectancy can be written in R too:

`Expectancy (R) = win rate x average win (R) - loss rate x average loss (R)`

### The 1 to 2% rule and position size

A common professional habit is to risk no more than **1% to 2% of the account** on any single trade. Position size then follows from the stop distance:

`Shares = (account x risk %) / (entry - stop)`

A wide stop means fewer shares; a tight stop means more. The money at risk stays the same. Note that the position value can be much larger than the money at risk, and a stop is not guaranteed: prices can gap past it overnight or on news, so real losses can exceed 1R.

### Risk of ruin, intuitively

Losing streaks are normal. With a 40% win rate, ten losses in a row in a long run of trades is not rare. Compare what such a streak does at different risk levels:

- Risking 2% each time: 0.98^10 = 0.817, so the account is down about **18%**.
- Risking 10% each time: 0.90^10 = 0.349, so the account is down about **65%**.

Recovery is asymmetric: a 50% loss needs a 100% gain to get back to even. **Risk of ruin** is the chance of losing so much that you can no longer trade, and it rises steeply as risk per trade rises, even when expectancy is positive.

> Common mistake: moving a stop further away when the price approaches it. That quietly turns a -1R loss into a -3R loss and breaks every number in your plan.
""",
            "example": {"title": "Worked example: sizing a trade from the stop", "body": """
Account: **50,000**. Risk per trade: **1%**. You want to buy Harbour Mills at **40.00** with a stop at **37.50**.

1. Money at risk = 50,000 x 1% = **500**
2. Stop distance = 40.00 - 37.50 = **2.50** per share
3. Shares = 500 / 2.50 = **200 shares**
4. Position value = 200 x 40.00 = **8,000** (16% of the account), but only 500 is at risk

**R multiples:** your target is 45.00, a gain of 5.00 per share = 5.00 / 2.50 = **+2R**, or 1,000.

**Expectancy check:** if similar trades win 40% of the time at +2R and lose 60% at -1R:

- 0.40 x 2 - 0.60 x 1 = 0.80 - 0.60 = **+0.2R** per trade, or about 100 per trade at this size.

If the stock gaps down to 36.00 overnight, you exit at 36.00: a loss of 4.00 x 200 = 800, which is **-1.6R**.
"""},
            "terms": [
                ("Stop-loss", "A pre-set exit price at which you close a losing trade because the idea has been proven wrong."),
                ("R multiple", "A trade's profit or loss divided by its initial risk (1R), so +2R means it made twice what it risked."),
                ("Initial risk (1R)", "The money you would lose if the trade hits its stop: stop distance x number of shares."),
                ("Risk of ruin", "The probability of losing so much of an account that you can no longer keep trading."),
                ("Gap", "A jump in price between one trade and the next, often overnight or on news, that can skip past a stop."),
            ],
            "cards": [
                ("What is the position-size formula from a stop?",
                 "Shares = (account x risk %) / (entry - stop). The money at risk stays fixed; a wider stop means fewer shares and a tighter stop means more."),
                ("Account 50,000, risk 1%, entry 40.00, stop 37.50. How many shares?",
                 "Risk = 50,000 x 1% = 500. Stop distance = 2.50. Shares = 500 / 2.50 = 200, a position worth 8,000."),
                ("What does +2R mean?",
                 "The trade made twice its initial risk. If you risked 500 (the distance to your stop times your shares), a +2R trade made 1,000."),
                ("Win rate 40%, average win 2R, average loss 1R. What is the expectancy?",
                 "0.40 x 2 - 0.60 x 1 = 0.80 - 0.60 = +0.2R per trade. Over 100 trades that is about +20R."),
                ("What does ten losses in a row do at 2% risk versus 10% risk per trade?",
                 "At 2%: 0.98^10 = 0.817, a drawdown of about 18%. At 10%: 0.90^10 = 0.349, a drawdown of about 65%, which needs nearly a 190% gain to recover."),
                ("True or false: a stop-loss guarantees you never lose more than 1R.",
                 "False. A stop becomes a market order when hit, and prices can gap past it overnight or on news, so the fill can be worse and the loss larger than 1R."),
                ("Why is a 50% loss so damaging?",
                 "Recovery is asymmetric: from 50% of the starting value you need a 100% gain to get back to even. Keeping losses small matters more than chasing big gains."),
                ("Why is moving a stop further away a serious mistake?",
                 "It enlarges the loss beyond the planned 1R, so your position size, expectancy and risk-of-ruin numbers no longer hold. Losses that were meant to be small become large."),
            ],
            "calc": "position",
            "links": [],
        },
        # ------------------------------------------------------------------
        {
            "id": "strategies",
            "title": "The main strategy families",
            "level": "Advanced",
            "minutes": 9,
            "summary": "Trend following, mean reversion, breakout, carry, event-driven and market making: how each makes money and when it fails.",
            "body": """
Almost every trading strategy belongs to one of a few families. Each earns money in some market conditions and loses in others, so knowing the family tells you what pain to expect.

### Trend following and momentum

Buy what has been rising and sell what has been falling, and hold while the move continues. It makes money in long, persistent trends and in crises that unfold over months. It loses in choppy, sideways markets, through many small losses, and when trends reverse sharply. Win rates are often below 50%, with a few large winners paying for many small losers.

### Mean reversion

Bet that prices which moved far from a typical level will come back: buy sharp falls, sell sharp rises. It works in range-bound markets and over short horizons. It fails when a move is the start of a new trend, so the losers can be large. Many mean-reversion strategies win often but have occasional big losses.

### Breakout

Enter when price moves beyond a recent range or level, expecting the move to continue. It is a close cousin of trend following and suffers from **false breakouts** that reverse quickly.

### Carry

Earn the yield difference between two assets: for example, borrowing in a low-interest currency and holding a high-interest one, or holding futures whose prices roll towards spot in your favour. Carry earns small, steady gains in calm markets and can lose them suddenly when markets panic and investors rush back into the funding asset.

### Event-driven

Trade around known events: earnings, mergers, index changes, central-bank decisions. **Merger arbitrage**, for example, buys the target of an announced takeover below the offer price and earns the gap if the deal closes, but loses heavily if it collapses.

### Market making

Quote both sides, earn the spread, and manage inventory. It needs speed, low costs and tight risk control, and it loses when prices move sharply in one direction against the inventory, often because better-informed traders are on the other side.

`Carry return = yield earned - yield paid + price change`

> Rule of thumb: combining families that fail at different times (for example trend and carry) usually gives a smoother result than any one alone, but correlations can rise in a crisis.
""",
            "example": {"title": "Worked example: a currency carry trade", "body": """
Two fictional currencies: the **Lumen** pays 6% a year on deposits, the **Ferro** charges 1% a year to borrow.

You borrow the equivalent of 100,000 in Ferro and hold 100,000 in Lumen deposits for one year.

1. Interest earned: 100,000 x 6% = **6,000**
2. Interest paid: 100,000 x 1% = **1,000**
3. Carry = 6,000 - 1,000 = **5,000**, or 5%

**If the exchange rate does not move:** you keep about **+5%**.

**If the Lumen falls 8% against the Ferro:** your Lumen holding loses about 8,000 in Ferro terms, so the result is roughly 5,000 - 8,000 = **-3,000**, or about -3%.

This is the carry trade's shape: small, steady gains that can be erased by one sharp currency move, which tends to come in market panics.
"""},
            "terms": [
                ("Trend following", "A strategy that buys assets in rising trends and sells those in falling trends, holding while the trend lasts."),
                ("Mean reversion", "A strategy betting that prices far from a typical level will move back towards it."),
                ("Breakout", "Entering a trade when price moves beyond a recent range, expecting the move to continue."),
                ("Carry trade", "Earning the yield difference between a higher-yielding asset you hold and a lower-yielding one you fund it with."),
                ("Merger arbitrage", "Buying the shares of a takeover target below the offer price and earning the gap if the deal completes."),
            ],
            "cards": [
                ("When does trend following tend to lose money?",
                 "In choppy, sideways markets, where it collects many small losses from false signals, and when trends reverse sharply before it can exit."),
                ("What is the typical profile of a mean-reversion strategy?",
                 "It often wins frequently with small gains but suffers occasional large losses, when a big move turns out to be the start of a new trend rather than an overreaction."),
                ("Borrow at 1%, hold an asset yielding 6%, and the currency falls 8%. Roughly what is the result?",
                 "Carry of 6% - 1% = 5%, minus the 8% currency loss, gives roughly -3% for the year."),
                ("Why is the carry trade sometimes described as picking up coins in front of a steamroller?",
                 "It earns small, steady gains in calm markets but can lose them suddenly when markets panic and investors rush back into the low-yield funding currency or asset."),
                ("How does merger arbitrage make money, and what is its main risk?",
                 "It buys a takeover target below the agreed offer price and earns the gap when the deal closes. The main risk is the deal collapsing, which can send the target's price sharply lower."),
                ("What is a false breakout?",
                 "A move beyond a range or level that quickly reverses back inside it, stopping out traders who bought the breakout."),
                ("When does market making lose money?",
                 "When prices move sharply in one direction against the inventory it holds, often because better-informed traders are taking the other side of its quotes."),
                ("Why combine strategy families such as trend and carry?",
                 "They tend to make and lose money at different times, so combining them can smooth returns. The benefit can shrink in a crisis when many strategies fall together."),
            ],
            "calc": None,
            "links": [],
        },
        # ------------------------------------------------------------------
        {
            "id": "trading-process",
            "title": "Plan, journal, review",
            "level": "Advanced",
            "minutes": 8,
            "summary": "A trade plan template, what to record in a journal, the weekly review, the key metrics and how to avoid tilt.",
            "body": """
Most trading mistakes are not about analysis but about process: trades taken on impulse, rules bent after a loss, results never measured. A written plan, a journal and a regular review fix most of that.

### The trade plan

Write it before you trade, while you are calm. A useful template answers:

1. **Setup:** what conditions must be true to enter?
2. **Entry:** exact price or trigger.
3. **Stop:** where the idea is proven wrong.
4. **Target or exit rule:** where or how you take profit.
5. **Size:** from account, risk % and stop distance.
6. **What would make me skip it:** news events, low liquidity, already at the daily loss limit.

### The journal

Record every trade, including the ones you would rather forget: date, instrument, setup name, entry, stop, exit, size, result in money and in R, fees, screenshot of the chart, your reason for the trade and how you felt. The emotional notes are often where the useful patterns hide.

### The weekly review

Once a week, group trades by setup and calculate:

- **Win rate:** winning trades / all trades.
- **Average win and average loss**, and their ratio.
- **Expectancy** per trade, in money and in R.
- **Profit factor:**

`Profit factor = gross profit / gross loss`

A profit factor above 1 means the winners made more than the losers lost. Also check **rule breaks**: how much did trades that broke the plan cost compared with those that followed it? Keep setups that show positive expectancy over a meaningful number of trades, and drop or fix the rest.

### Avoiding tilt

**Tilt** is trading emotionally after losses (or big wins), usually by sizing up or taking setups not in the plan to win the money back. Defences that professionals use:

- A **daily loss limit**, for example 3R, after which you stop for the day.
- A cooling-off rule after a set number of losses in a row.
- Never changing the plan during market hours; changes happen in the weekly review.

> Common mistake: reviewing only the losing trades. Winners taken by luck, or by breaking rules, teach bad habits if you never look at them.
""",
            "example": {"title": "Worked example: a weekly review of 20 trades", "body": """
Your journal for the month shows **20 trades**: **8 winners** averaging **300**, **12 losers** averaging **150**.

1. Win rate = 8 / 20 = **40%**
2. Gross profit = 8 x 300 = **2,400**; gross loss = 12 x 150 = **1,800**
3. Profit factor = 2,400 / 1,800 = **1.33**
4. Net result = 2,400 - 1,800 = **600**; expectancy = 600 / 20 = **30 per trade**
5. Check with the formula: 0.40 x 300 - 0.60 x 150 = 120 - 90 = **30**

**Rule breaks:** 4 of the 12 losers were trades outside the plan, losing 250 each (1,000 in total). Without them, 16 trades would have netted 2,400 - 800 = **1,600**, a profit factor of **3.0**. The lesson from this review is about discipline, not the strategy.
"""},
            "terms": [
                ("Trade plan", "A written set of rules for a trade or setup: entry, stop, exit, size and when to skip, made before trading."),
                ("Trading journal", "A record of every trade with prices, size, result, reasons and emotions, used for later review."),
                ("Profit factor", "Gross profit divided by gross loss; above 1 means winners made more than losers lost."),
                ("Win rate", "The share of trades that made money: winning trades divided by all trades."),
                ("Tilt", "Trading emotionally after losses or big wins, usually by sizing up or breaking the plan."),
                ("Daily loss limit", "A pre-set loss, often in R, after which a trader stops trading for the day."),
            ],
            "cards": [
                ("What should a trade plan include?",
                 "The setup conditions, exact entry, stop, target or exit rule, position size, and the conditions under which you would skip the trade. It is written before trading, while calm."),
                ("8 winners averaging 300 and 12 losers averaging 150. What is the profit factor?",
                 "Gross profit 8 x 300 = 2,400; gross loss 12 x 150 = 1,800. Profit factor = 2,400 / 1,800 = 1.33."),
                ("What does a profit factor below 1 tell you?",
                 "Over the period the losing trades lost more money than the winning trades made, so the setup or the way it was traded lost money overall."),
                ("Name five fields every journal entry should have.",
                 "For example: date and instrument, setup name, entry, stop and exit prices, size, result in money and in R, fees, the reason for the trade and how you felt."),
                ("What is tilt, and name two defences against it.",
                 "Tilt is emotional trading after losses or big wins, such as sizing up to win money back. Defences: a daily loss limit (for example 3R) and a cooling-off rule after several losses in a row."),
                ("Why should the trading plan only be changed during the weekly review?",
                 "Changes made during market hours are usually driven by the last few trades and emotions. The review looks at many trades calmly and grouped by setup."),
                ("Why review winning trades as well as losers?",
                 "A winner that broke the rules or worked by luck reinforces bad habits. Reviewing it shows whether the process was right, not just the result."),
                ("How do you measure what rule breaks cost you?",
                 "Tag each journal entry as on-plan or off-plan, then compare the results of the two groups. The difference shows the cost of indiscipline separately from the strategy itself."),
            ],
            "calc": None,
            "links": [],
        },
    ],
}
