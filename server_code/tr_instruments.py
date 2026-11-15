"""Track: Markets and instruments. Content for Master Investor (see tools/CONTENT_BRIEF.md)."""

TRACK = {
    "id": "instruments",
    "title": "Markets and instruments",
    "level": "Intermediate",
    "blurb": "How the main instruments really work: stocks and indices, bonds, options, futures and leverage, and "
             "the assets beyond stocks and bonds.",
    "lessons": [
        # ------------------------------------------------------------------ stocks-in-depth
        {
            "id": "stocks-in-depth",
            "title": "Stocks in depth",
            "level": "Intermediate",
            "minutes": 9,
            "summary": "Share classes, dividends and buybacks, splits, IPOs, and how cap-weighted, equal-weighted and "
                       "price-weighted indices are built.",
            "body": """
A share is a small slice of ownership in a company. It gives you a claim on profits after everyone else
(staff, suppliers, lenders, tax) has been paid, and usually a vote on big decisions.

### Share classes

Some companies issue more than one class. Often one class carries extra votes (for example 10 votes per share)
and is held by the founders, while the public class has one vote or none. The economic claim may be the same,
but control is not. **Preferred shares** usually pay a fixed dividend that must be paid before ordinary
dividends, and rank ahead of ordinary shares if the company is wound up, but rarely have votes.

### Dividends, buybacks and splits

A company can return cash in two main ways:

- **Dividends**: cash paid per share. To receive one you must own the share before the **ex-dividend date**;
  on that date the price typically drops by roughly the dividend.
- **Buybacks**: the company buys its own shares, so each remaining share owns a bigger slice. Earnings per
  share rise even if total profit does not. A buyback helps remaining owners only if the shares are bought for
  less than they are worth.

A **stock split** (say 4-for-1) gives you four shares for each one, each worth a quarter of the price. Nothing
real changes: the company is worth the same and your stake is the same.

### IPOs

An **initial public offering (IPO)** is when a private company first sells shares to the public, usually with
banks setting the price and allocating shares. The sellers (founders, early investors) choose when to sell
and know the business best, so be careful about assuming IPOs are bargains. Several academic studies have
found that IPOs, as a group, have tended to lag comparable shares over the following years.

### How indices are built

An index tracks a basket of shares. The weighting method matters:

- **Cap-weighted** (most big indices, such as the S&P 500): each company is weighted by its market value, so the
  largest companies dominate.
- **Equal-weighted**: every company has the same weight, which tilts towards smaller companies and needs
  regular rebalancing.
- **Price-weighted** (the Dow Jones Industrial Average, the Nikkei 225): weighted by share price, so a high-priced
  share counts more regardless of company size.

`Market cap = Share price x Shares outstanding`

> Common mistake: thinking a split makes a stock cheaper. A 400 share split into four 100 shares is exactly the
> same value; only the price per piece changed.
""",
            "example": {
                "title": "Worked example: one index, three weightings",
                "body": """
Three fictional companies:

- Alder Mining: price **100**, 10m shares, market cap **1,000m**
- Birch Telecom: price **20**, 100m shares, market cap **2,000m**
- Cedar Retail: price **50**, 20m shares, market cap **1,000m**

**Weights:**

- Cap-weighted: total 4,000m, so Alder 25%, Birch 50%, Cedar 25%.
- Equal-weighted: 33.3% each.
- Price-weighted: total of prices 170, so Alder 100 / 170 = 58.8%, Birch 20 / 170 = 11.8%, Cedar 50 / 170 = 29.4%.

**Alder rises 10%, the others do not move:**

- Cap-weighted index: 25% x 10% = **+2.5%**
- Equal-weighted index: 33.3% x 10% = **+3.3%**
- Price-weighted index: the price total goes from 170 to 180, so **+5.9%**

**A buyback:** Birch earns 500m on 100m shares, EPS 5.00. It buys back 10m shares. EPS becomes 500 / 90 = **5.56**
(ignoring the interest it gave up on the cash), an 11% rise with no extra profit.
""",
            },
            "terms": [
                ("Share class", "A type of share with its own rights; classes can differ in votes or dividends."),
                ("Ex-dividend date", "The first day a share trades without the right to the next dividend."),
                ("Share buyback", "A company buying its own shares, reducing the number outstanding."),
                ("Stock split", "Dividing each share into several, lowering the price per share without changing total value."),
                ("Initial public offering (IPO)", "The first sale of a company's shares to the public on a stock exchange."),
                ("Cap-weighted index", "An index in which each company's weight is proportional to its market value."),
            ],
            "cards": [
                ("A company with 10m shares at 30 does a 3-for-1 split. What happens?", "There are now 30m shares at about 10 each. Market cap stays 300m and each holder's stake is unchanged."),
                ("Why do earnings per share rise after a buyback even if profit stays flat?", "The same profit is divided over fewer shares. With 500m profit, cutting shares from 100m to 90m lifts EPS from 5.00 to about 5.56."),
                ("When does a buyback actually help the remaining shareholders?", "When the company buys shares for less than they are worth. Buying back overvalued shares transfers value to the sellers."),
                ("What must you do to receive a declared dividend?", "Own the share before the ex-dividend date. On that date the share typically falls by roughly the dividend amount."),
                ("In a price-weighted index, which company has the most influence?", "The one with the highest share price, regardless of how big the company is. The Dow Jones Industrial Average and the Nikkei 225 work this way."),
                ("How does an equal-weighted index differ from a cap-weighted one?", "Each member has the same weight rather than a weight based on market value, so it tilts towards smaller companies and must be rebalanced regularly."),
                ("Why be cautious about assuming IPOs are bargains?", "The sellers know the business best and choose the timing and price. Several studies find IPOs as a group have tended to lag comparable shares in the following years."),
                ("What do dual-class shares usually separate?", "Economic ownership from control: one class, often held by founders, carries extra votes, while public shareholders get fewer or no votes."),
            ],
            "calc": None,
            "links": [
                ("Investor.gov: stocks", "https://www.investor.gov/introduction-investing/investing-basics/investment-products/stocks"),
            ],
        },
        # ------------------------------------------------------------------ bonds
        {
            "id": "bonds",
            "title": "Bonds: price, yield and duration",
            "level": "Intermediate",
            "minutes": 10,
            "summary": "How a bond's price is set, why it moves opposite to yields, how duration measures rate risk, and "
                       "what ratings and spreads say.",
            "body": """
A **bond** is a loan you make to a government or company. In return you usually get a fixed yearly interest
payment, the **coupon**, and your money back (the **face value**, often 1,000) at **maturity**.

### Price is the present value of the payments

A bond's price is every future payment discounted at the yield the market currently demands:

`Price = C / (1 + y) + C / (1 + y)^2 + ... + (C + Face) / (1 + y)^n`

The discount rate y that makes this equation true at the market price is the **yield to maturity (YTM)**: the
yearly return you earn if you buy now, receive every payment and hold to maturity (assuming you can reinvest
the coupons at the same yield).

### Why prices and yields move in opposite directions

The coupon is fixed. If new bonds start paying more, nobody will pay full price for an old bond with a lower
coupon, so its price falls until its yield matches the market. If market yields fall, old bonds with higher
coupons become worth more. A bond priced above face value is at a **premium** (its coupon is above the market
yield); below face value it is at a **discount**.

### Duration and convexity

**Duration** measures how sensitive a bond's price is to yield changes. Modified duration gives a handy
approximation:

`% price change = - Modified duration x Change in yield`

A bond with modified duration 7 loses about 7% if yields rise by 1 percentage point. Longer maturities and
lower coupons mean higher duration. **Convexity** is the curve in the relationship: for ordinary bonds, prices
rise a little more when yields fall than they drop when yields rise, so duration alone slightly overstates
losses and understates gains for large moves.

### Credit ratings and spreads

Rating agencies grade borrowers from AAA down. Bonds rated BBB- or above (Baa3 at Moody's) are called
**investment grade**; below that, **high yield** or junk. Riskier borrowers must pay more: the **credit spread**
is the extra yield over a government bond of similar maturity. Spreads widen when investors fear defaults,
which pushes corporate bond prices down even if government yields stay put.

> Common mistake: thinking a government bond fund cannot lose money. It has no default risk, but a long-duration
> fund can fall sharply when yields rise.
""",
            "example": {
                "title": "Worked example: a 5-year bond from Saltmarsh Utilities",
                "body": """
Face value **1,000**, coupon **5%** paid once a year (50 a year), **5 years** to maturity. The market now demands
a yield of **6%**.

1. Present value of the coupons: 50 x (1 - 1.06^-5) / 0.06 = 50 x 4.2124 = **210.62**.
2. Present value of the face value: 1,000 / 1.06^5 = 1,000 / 1.3382 = **747.26**.
3. Price = 210.62 + 747.26 = **957.88**. It trades at a discount because its 5% coupon is below the 6% market yield.

**Duration:** this bond's Macaulay duration is about 4.53 years; modified duration = 4.53 / 1.06 = **4.28**.

- If yields rise to 7%: duration predicts about -4.28%, or roughly 916.9. The actual price is **918.00** (-4.16%).
- If yields fall to 5%: duration predicts about +4.28%. The actual price is **1,000.00** (+4.40%), because the
  coupon now equals the yield.

The gain is bigger than the loss for the same 1-point move: that is convexity.

**Spread:** if a 5-year government bond yields 4.5%, the spread is 6% - 4.5% = 1.5 percentage points, or **150
basis points**.
""",
            },
            "terms": [
                ("Coupon", "The fixed interest a bond pays each year, stated as a percentage of face value."),
                ("Yield to maturity", "The yearly return from buying a bond at today's price and holding it to maturity, with coupons reinvested at the same yield."),
                ("Duration", "A measure of a bond's price sensitivity to changes in yield; modified duration gives the approximate % price change per 1-point yield move."),
                ("Convexity", "The curvature of the price-yield relationship, which makes price gains from falling yields larger than losses from rising yields of the same size."),
                ("Credit spread", "The extra yield a bond pays over a government bond of similar maturity, as compensation for default risk."),
                ("Investment grade", "Bonds rated BBB- (S&P, Fitch) or Baa3 (Moody's) or higher."),
            ],
            "cards": [
                ("Why do bond prices fall when market yields rise?", "The coupon is fixed, so an old bond paying less than new bonds is only attractive at a lower price. Its price falls until its yield matches the market."),
                ("A bond has modified duration 6. Yields rise by 0.5 percentage points. Roughly how much does the price change?", "About -6 x 0.5% = -3%. Convexity makes the actual loss slightly smaller."),
                ("A bond's coupon is 4% and market yields for similar bonds are 5%. Does it trade above or below face value?", "Below face value, at a discount, because its coupon is less than what the market now demands."),
                ("What is yield to maturity?", "The single discount rate that makes the present value of a bond's coupons and face value equal its price: the yearly return if you hold to maturity and reinvest coupons at that rate."),
                ("Which has higher duration: a 30-year zero-coupon bond or a 5-year bond with a 6% coupon?", "The 30-year zero. Longer maturity and lower coupons both raise duration; a zero's duration equals its maturity."),
                ("A corporate bond yields 6.2% and a government bond of similar maturity yields 4.0%. What is the credit spread?", "2.2 percentage points, or 220 basis points."),
                ("What happens to corporate bond prices when credit spreads widen?", "They fall, because investors demand a higher yield for default risk, even if government bond yields stay the same."),
                ("Where is the line between investment grade and high yield?", "BBB- at S&P and Fitch, Baa3 at Moody's. Bonds rated below that are called high yield or junk."),
                ("True or false: a government bond fund cannot lose money.", "False. It has little default risk, but when yields rise its price falls, and long-duration funds can drop sharply."),
            ],
            "calc": "bond",
            "links": [
                ("FRED: 10-year US Treasury yield", "https://fred.stlouisfed.org/series/DGS10"),
                ("FRED: US corporate bond spread (ICE BofA OAS)", "https://fred.stlouisfed.org/series/BAMLC0A0CM"),
            ],
        },
        # ------------------------------------------------------------------ options
        {
            "id": "options",
            "title": "Options from zero",
            "level": "Intermediate",
            "minutes": 12,
            "summary": "Calls and puts, payoffs at expiry, intrinsic and time value, the Greeks in plain words, and why "
                       "time decay works against most buyers.",
            "body": """
An **option** is a contract that gives the buyer the right, but not the obligation, to buy or sell something at
a fixed price (the **strike**) until or on a set date (the **expiry**). The buyer pays a price called the
**premium** to the seller (the writer). On most stock exchanges one contract covers 100 shares.

### Calls and puts

- A **call** is the right to buy at the strike. It gains when the price rises.
- A **put** is the right to sell at the strike. It gains when the price falls.

At expiry, per share:

`Call payoff = max(Price - Strike, 0)`

`Put payoff = max(Strike - Price, 0)`

Profit is payoff minus the premium paid. A buyer can lose at most the premium; a seller of an uncovered call
has no limit on losses.

### Intrinsic value, time value and moneyness

An option's premium has two parts. **Intrinsic value** is what it would pay if exercised now. **Time value** is
everything above that: the chance the option becomes more valuable before expiry. A call is **in the money**
when the price is above the strike, **at the money** when it is near the strike, and **out of the money** when
below. For puts it is the reverse. Out-of-the-money options are pure time value.

### The Greeks in plain words

- **Delta**: how much the option price moves for a 1 move in the underlying. Calls run 0 to 1, puts 0 to -1.
- **Gamma**: how fast delta changes as the price moves.
- **Theta**: how much value the option loses each day from the passing of time, all else equal.
- **Vega**: how much the option price changes when expected volatility changes by 1 point.
- **Rho**: sensitivity to interest rates, usually the smallest effect.

### Two common strategies

- **Covered call**: own the shares and sell a call. You collect premium but give up gains above the strike.
- **Protective put**: own the shares and buy a put. Like insurance, it caps your loss at a cost.

### Why most option buyers lose to time decay

Time value melts to zero by expiry, and the melting speeds up in the final weeks. A buyer needs the price to
move far enough, and soon enough, to beat the premium. Being right about direction but too slow still loses.

> Rule of thumb: before buying an option, work out the break-even price at expiry (strike plus premium for a
> call, strike minus premium for a put) and ask how likely that move is in the time left.
""",
            "example": {
                "title": "Worked example: options on Quillfeather Media",
                "body": """
Quillfeather shares trade at **103**. A call with strike **100** costs **4**; a put with strike **95** costs **2**.

**The call now:** intrinsic value = 103 - 100 = **3**, time value = 4 - 3 = **1**. It is in the money.
Break-even at expiry = 100 + 4 = **104**.

**Call at expiry:**

- Price 110: payoff 10, profit 10 - 4 = **6** per share, 600 per contract of 100 shares.
- Price 102: payoff 2, profit **-2**.
- Price 95: payoff 0, loss of the full premium, **-4**.

**The put now:** out of the money (103 is above 95), so its 2 is all time value. At expiry price 88: payoff
95 - 88 = 7, profit 7 - 2 = **5**.

**Covered call:** own shares bought at 100 and sell a 110 call for 3. Best case at expiry: (110 - 100) + 3 =
**13** per share. If the shares fall, the premium cushions the first 3.

**Protective put:** own shares bought at 100 and buy a 90 put for 2. Worst case at expiry: (100 - 90) + 2 =
**12** per share, however far the shares fall.
""",
            },
            "terms": [
                ("Call option", "The right to buy an asset at the strike price until or on the expiry date."),
                ("Put option", "The right to sell an asset at the strike price until or on the expiry date."),
                ("Strike price", "The fixed price at which an option lets its holder buy or sell."),
                ("Time value", "The part of an option's premium above its intrinsic value, reflecting the chance of further gains before expiry."),
                ("Delta", "How much an option's price changes for a 1-unit move in the underlying asset."),
                ("Theta", "The value an option loses per day from the passing of time, all else equal."),
            ],
            "cards": [
                ("You buy a call with strike 50 for 3. At expiry the stock is at 58. What is your profit per share?", "Payoff = 58 - 50 = 8, profit = 8 - 3 = 5 per share (500 per contract of 100 shares)."),
                ("What is the break-even price at expiry for a put with strike 40 bought for 2?", "40 - 2 = 38. The stock must finish below 38 for the put buyer to make a profit."),
                ("A stock is at 72 and a call with strike 70 costs 5. Split the premium into intrinsic and time value.", "Intrinsic value = 72 - 70 = 2; time value = 5 - 2 = 3."),
                ("What is the most an option buyer can lose? And an uncovered call seller?", "A buyer can lose only the premium paid. A seller of an uncovered call faces unlimited losses, because the stock price has no upper limit."),
                ("What does theta measure, and why does it hurt option buyers?", "Theta is the value lost each day as time passes. Time value falls to zero by expiry, faster near the end, so a buyer needs a big enough move soon enough to overcome it."),
                ("What does a call delta of 0.6 mean?", "The option price moves by about 0.60 for each 1 move in the stock, roughly like holding 60 shares per 100-share contract."),
                ("What do you give up with a covered call?", "Gains above the strike. In exchange for the premium you receive, your shares will effectively be sold at the strike if the price rises past it."),
                ("Why might an investor buy a protective put?", "As insurance: it sets a floor under losses on shares they own, at the cost of the premium."),
                ("True or false: if you are right about the direction of a stock, buying a call will make money.", "False. The stock must rise past the strike plus the premium before expiry. A move that is too small or too slow still loses to time decay."),
            ],
            "calc": "options",
            "links": [],
        },
        # ------------------------------------------------------------------ futures-and-leverage
        {
            "id": "futures-and-leverage",
            "title": "Futures and leverage",
            "level": "Advanced",
            "minutes": 11,
            "summary": "Margin and daily settlement, contango and backwardation, roll yield, the maths of leverage and "
                       "why leveraged ETFs decay in choppy markets.",
            "body": """
A **futures contract** is an agreement to buy or sell a set quantity of something (oil, wheat, a stock index,
a currency) at a price fixed today, for delivery on a future date. Contracts are standardised and traded on an
exchange, and a clearing house stands between buyer and seller. Most traders close or roll positions before
delivery.

### Margin and mark to market

You do not pay the full value up front. You post **initial margin**, often around 5 to 15% of the contract's
value, set by the exchange. Every day the contract is **marked to market**: gains are credited and losses
debited from your account in cash. If the balance falls below the **maintenance margin**, you get a margin call
and must add money, usually back to the initial level, or the position is closed.

### Contango, backwardation and roll yield

Futures prices for different delivery months form a curve.

- **Contango**: later contracts cost more than the spot price, common when storage and financing are costly.
- **Backwardation**: later contracts cost less than spot, common when the commodity is scarce now.

A futures price converges towards the spot price as delivery approaches. An investor who keeps a long position
by selling the expiring contract and buying the next one earns a **roll yield**: negative in contango (you keep
buying higher and watching it drift down) and positive in backwardation. This is why commodity funds can lag the
spot price badly for years.

### Leverage maths

`Leverage = Position size / Your capital`

With leverage L, a market move of m changes your capital by about L x m. At 10x, a 10% fall wipes you out.
Losses also need bigger gains to recover: after a 50% loss you need +100% to get back to where you started.

### Why leveraged ETFs decay

A 2x or 3x leveraged ETF resets its leverage every day, so it delivers the multiple of each **daily** return, not
of the return over months. In a market that swings up and down without going anywhere, the losses compound
more than the gains, and the fund falls even if the index ends flat. In steady trends it can beat the simple
multiple. This **volatility decay** is why these funds are designed for short holding periods.

> Common mistake: judging leverage only by the expected gain. Always ask what move would force you out, because
> a forced exit locks in the loss even if the price later recovers.
""",
            "example": {
                "title": "Worked example: crude oil futures and a 2x fund",
                "body": """
**Futures on oil:** one contract covers **1,000 barrels** at **80**, so the position is worth **80,000**. Initial
margin is **8,000**; maintenance margin **6,000**.

- Leverage = 80,000 / 8,000 = **10x**.
- Oil rises 5% to 84: gain 4 x 1,000 = **4,000**, or +50% on the margin.
- Oil falls 5% to 76: loss **4,000**. The account drops to 4,000, below maintenance, so a margin call asks for
  4,000 more to restore 8,000.
- A 10% fall (to 72) would lose 8,000, the entire initial margin.

**Roll yield in contango:** spot is 80 and the next month's contract is 82. If spot stays at 80, the contract
drifts down to 80 by expiry, a loss of 2 / 82 = about **2.4%** for the month while spot did not move.

**2x daily leveraged fund:** an index goes from 100 to 110 (+10%) and back to 99 (-10%), down **1%** overall.

- 2x fund: +20% takes 100 to 120, then -20% takes 120 to **96**, down **4%**, not 2%.
- 3x fund: +30% to 130, then -30% to **91**, down **9%**.
""",
            },
            "terms": [
                ("Futures contract", "A standardised exchange-traded agreement to buy or sell a set amount of an asset at a fixed price on a future date."),
                ("Initial margin", "The deposit required to open a futures position, a fraction of the contract's value."),
                ("Mark to market", "Daily settlement of gains and losses on a futures position in cash."),
                ("Contango", "When futures prices for later delivery are higher than the spot price."),
                ("Backwardation", "When futures prices for later delivery are lower than the spot price."),
                ("Roll yield", "The gain or loss from replacing an expiring futures contract with a later one as prices converge to spot."),
                ("Volatility decay", "The loss a daily-reset leveraged fund suffers in markets that swing up and down without trending."),
            ],
            "cards": [
                ("A futures position is worth 50,000 and you posted 5,000 margin. What is your leverage, and what fall wipes you out?", "50,000 / 5,000 = 10x. A 10% fall in the futures price loses 5,000, the whole margin."),
                ("What does mark to market mean for a futures trader?", "Gains and losses are settled in cash every day. If losses push the account below the maintenance margin, the trader must add money or the position is closed."),
                ("What is contango, and why does it hurt a long-only commodity fund?", "Later futures cost more than spot. As each contract converges down towards spot and the fund rolls into the next dearer one, it loses money even if spot stays flat: negative roll yield."),
                ("In backwardation, what roll yield does a long futures holder earn?", "A positive one: later contracts are cheaper than spot, and as they converge up towards spot the holder gains even if spot does not move."),
                ("An index goes +10% then -10%. What does a 2x daily leveraged fund do?", "100 to 120 to 96, a loss of 4%, while the index lost only 1% (100 to 110 to 99)."),
                ("Why do leveraged ETFs decay in choppy markets?", "They reset leverage daily, so they multiply each day's return, and in up-and-down markets the compounded losses outweigh the gains. The fund can fall even if the index ends flat."),
                ("After a 50% loss, what gain do you need to break even?", "100%. Half the capital must double to return to the start, which is why leveraged losses are so hard to recover from."),
                ("True or false: a 3x leveraged ETF held for a year returns three times the index's yearly return.", "False. It targets three times each daily return. Over longer periods compounding makes the result differ, often worse in volatile markets and sometimes better in steady trends."),
            ],
            "calc": None,
            "links": [],
        },
        # ------------------------------------------------------------------ alternatives
        {
            "id": "alternatives",
            "title": "Beyond stocks and bonds",
            "level": "Intermediate",
            "minutes": 10,
            "summary": "Currencies, commodities, real estate, crypto and private markets: what drives each, how people "
                       "get exposure, and the specific risks.",
            "body": """
Most long-term portfolios are built from stocks and bonds, but other assets behave differently and can add
diversification, or extra risk. For each, ask three things: what drives its return, how you would hold it, and
what can go wrong.

### Currencies

Exchange rates move with interest rate differences, inflation, trade flows and investor mood. Most investors
hold currencies indirectly: owning foreign shares or bonds means owning the currency too. Foreign returns in
your own money are:

`Home return = (1 + Local return) x (1 + Currency change) - 1`

Currency-hedged funds remove most of that effect for a small cost. Currencies themselves produce no cash flow
apart from interest, so over long periods they are not a source of growth.

### Commodities

Oil, metals and crops respond to supply shocks, weather, economic growth and the dollar. Exposure usually comes
through futures-based funds (with the roll yield effects from the previous lesson), physically backed funds
for gold and silver, or shares of producers, which add company risk. Commodities pay no income and their
long-run real return has historically been modest; their main argument is that they can rise when inflation
surprises.

### Real estate and REITs

Property returns come from rent and from changes in property values, which depend on interest rates,
occupancy and the local economy. Exposure: owning property directly (concentrated and illiquid, but often
financed with a mortgage) or **REITs**, listed companies that own property and pay out most of their income.
REITs trade daily and can fall sharply when interest rates rise.

### Crypto assets

Bitcoin and other crypto assets have no cash flows; prices depend on adoption, supply rules, regulation and
sentiment. They have been extremely volatile, with past falls of 70% or more. Specific risks include exchange
failures, hacks, lost keys and fraud. Exposure: buying on an exchange, holding coins yourself, or, where
allowed, exchange-traded funds.

### Private markets

Private equity, venture capital and private credit invest in unlisted companies and loans. They are usually
available only to large or accredited investors through funds that lock money up for 7 to 10 years and charge
high fees (a traditional model is 2% a year plus 20% of profits). Valuations are updated rarely, which makes
them look smoother than they are.

> Common mistake: mistaking smooth reported values for low risk. An asset that is valued quarterly by its
> manager will look calmer than a listed share, even if the underlying risk is the same or higher.
""",
            "example": {
                "title": "Worked example: a foreign fund and a currency move",
                "body": """
An investor whose home currency is the dollar buys **10,000** of a fund holding shares in another country. Over
a year the shares rise **8%** in their local currency.

**If the foreign currency falls 5% against the dollar:**

- Home return = 1.08 x 0.95 - 1 = 1.026 - 1 = **+2.6%**, so the holding is worth **10,260**.

**If the foreign currency rises 5%:**

- Home return = 1.08 x 1.05 - 1 = 1.134 - 1 = **+13.4%**, worth **11,340**.

**With a currency-hedged version** (assume hedging costs 0.5% a year): home return is about 8% - 0.5% = **7.5%**
in either case.

The same shares gave anything from 2.6% to 13.4% depending on the currency. Hedging narrows that range but
also removes the chance of a currency gain.
""",
            },
            "terms": [
                ("Currency hedging", "Using contracts such as forwards to remove most of the effect of exchange rate moves on foreign holdings."),
                ("Commodity", "A raw material such as oil, metals or crops, traded in standard grades."),
                ("REIT", "Real estate investment trust: a company that owns income-producing property and pays out most of its income to shareholders."),
                ("Private equity", "Investment in companies that are not listed on a stock exchange, usually through long lock-up funds."),
                ("Illiquidity", "Difficulty selling an asset quickly without a large price cut."),
            ],
            "cards": [
                ("Foreign shares rise 10% in local currency and the currency falls 10% against yours. What is your return?", "1.10 x 0.90 - 1 = -1%. The currency loss slightly outweighs the share gain."),
                ("What does a currency-hedged fund do?", "It uses contracts such as forwards to remove most of the effect of exchange rate moves, so your return is close to the local-currency return minus a hedging cost."),
                ("What are the main ways to get commodity exposure, and a drawback of each?", "Futures-based funds (roll yield can hurt in contango), physically backed funds for metals like gold (storage cost, no income), and producer shares (adds company-specific risk)."),
                ("Why can REITs fall when interest rates rise?", "Higher rates raise borrowing costs, make bond yields more competitive with REIT dividends, and push up the discount rates used to value property."),
                ("Name three risks specific to holding crypto assets.", "Extreme volatility (past falls of 70% or more), exchange failures or hacks, and losing the keys or being defrauded. Regulation can also change quickly."),
                ("What does '2 and 20' mean for a private fund?", "A management fee of 2% of assets a year plus 20% of the profits, a traditional fee model for private equity and hedge funds."),
                ("Why can private market investments look less risky than they are?", "Their values are estimated by the manager, often quarterly, so reported prices move smoothly, while the underlying risk can be the same as or higher than listed shares."),
                ("True or false: commodities produce a reliable long-term return like dividends from shares.", "False. Commodities pay no income and their long-run real returns have historically been modest; the main argument for them is protection when inflation surprises."),
            ],
            "calc": None,
            "links": [],
        },
    ],
}
