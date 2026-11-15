"""Track: Macro and the economy. Content for Master Investor (see tools/CONTENT_BRIEF.md)."""

TRACK = {
    "id": "macro",
    "title": "Macro and the economy",
    "level": "Intermediate",
    "blurb": "How interest rates, inflation, the yield curve and the business cycle move markets, and how to read the "
             "economic news without overreacting to it.",
    "lessons": [
        {
            "id": "rates-and-central-banks",
            "title": "Interest rates and central banks",
            "level": "Intermediate",
            "minutes": 8,
            "summary": "How a central bank sets the price of money, how that reaches mortgages, bonds and share prices, and why markets hang on every word.",
            "body": """
A central bank (the Federal Reserve in the US, the ECB in the euro area, the Bank of England, the Bank of Canada) has one main lever: the **policy rate**, the interest rate it pays or charges banks on overnight money. It raises the rate to cool an economy that is running too hot and lowers it to support one that is weakening. Most central banks aim for low, stable inflation, often around 2% a year; some also aim for full employment.

### How the policy rate travels

The policy rate directly sets only the shortest borrowing costs. From there it spreads out:

- **Short-term loans and savings**: variable-rate mortgages, credit lines and savings accounts usually follow within weeks.
- **Bonds**: longer bond yields move on what investors *expect* the policy rate to average over the bond's life, plus extra pay for tying money up (more in the yield curve lesson).
- **Fixed-rate mortgages** are priced off those longer bond yields, so they can move before the central bank does anything.

### QE and QT

When the policy rate is already near zero, a central bank can buy large amounts of government bonds and other assets with newly created reserves. This is **quantitative easing (QE)**: it pushes bond prices up and long yields down. **Quantitative tightening (QT)** is the reverse: letting those bonds mature without replacing them, or selling them, which tends to push long yields up.

### Why every word matters

Markets price the *future* path of rates, not just today's rate. So a hint in a speech or in the meeting statement that cuts will come later than expected can move bond and stock prices more than the decision itself. This is called **forward guidance**.

### Rates and stock valuations

A share is worth the cash it will pay in future, discounted back to today. Higher rates mean a higher discount rate, so future cash is worth less now. A simple model shows the effect:

`Price = next year's dividend / (required return - growth)`

Companies whose cash flows sit far in the future (young growth companies) are hit hardest by rising rates, much like long-dated bonds.

> Common mistake: thinking a rate cut is always good news for stocks. If the bank cuts because a recession is arriving, falling profits can outweigh the lower discount rate.
""",
            "example": {"title": "Worked example: a 1-point rise in the required return", "body": """
Northwind Utilities is expected to pay a dividend of **4.00** next year, growing **4%** a year for ever. Investors want an **8%** return.

1. Price = 4.00 / (0.08 - 0.04) = 4.00 / 0.04 = **100**
2. Rates rise and investors now want **9%**: Price = 4.00 / (0.09 - 0.04) = 4.00 / 0.05 = **80**
3. Change: (80 - 100) / 100 = **-20%**

Nothing about the business changed: the same dividends are simply worth less today. A growth company with growth of 6% would fall further: 4.00 / 0.02 = 200 becomes 4.00 / 0.03 = 133.33, a **33%** drop. The closer the required return is to the growth rate, the more sensitive the price is to rates.
"""},
            "terms": [
                ("Policy rate", "The overnight interest rate a central bank sets to steer borrowing costs across the economy."),
                ("Quantitative easing (QE)", "Large-scale central bank purchases of bonds that push long-term yields down and add money to the banking system."),
                ("Quantitative tightening (QT)", "Shrinking a central bank's bond holdings, by letting them mature or selling them, which tends to push long-term yields up."),
                ("Forward guidance", "What a central bank says about the likely future path of rates, used to steer market expectations."),
                ("Discount rate", "The return investors require, used to turn future cash flows into a value today."),
            ],
            "cards": [
                ("What does a central bank's policy rate directly control?", "Only the shortest borrowing cost, the overnight rate banks pay or earn. Everything else, from savings rates to bond yields, follows indirectly through expectations and competition."),
                ("Why can fixed mortgage rates rise before the central bank raises its policy rate?", "Fixed mortgages are priced off longer bond yields, which move on the expected future path of the policy rate. If markets expect hikes, long yields and mortgage rates rise first."),
                ("What is quantitative easing, and what does it do to long-term yields?", "QE is a central bank buying large amounts of bonds with newly created reserves. Buying pushes bond prices up, so long-term yields fall."),
                ("Why can a speech move markets more than the rate decision itself?", "Markets price the expected future path of rates. A decision that was fully expected changes little, while a hint that cuts or hikes will come sooner or later changes that path."),
                ("A dividend of 3 growing 5% a year, required return 8%: what is the price? What if the required return becomes 9%?", "3 / (0.08 - 0.05) = 100. At 9%: 3 / (0.09 - 0.05) = 75, a 25% fall with no change in the business."),
                ("Why are growth companies usually more sensitive to rising rates than mature companies?", "More of their value comes from cash flows far in the future, and distant cash flows lose the most value when the discount rate rises, just as long bonds fall more than short ones."),
                ("True or false: a rate cut is always good for stocks.", "False. Lower rates raise the value of future cash, but if the cut is a response to a weakening economy, falling profits can outweigh that and stocks can still fall."),
                ("What is quantitative tightening?", "The reverse of QE: a central bank shrinks its bond holdings by letting bonds mature without replacing them or by selling them, which tends to push long yields up."),
            ],
            "calc": None,
            "links": [
                ("Federal Reserve: monetary policy", "https://www.federalreserve.gov/monetarypolicy.htm"),
                ("FRED: effective federal funds rate", "https://fred.stlouisfed.org/series/FEDFUNDS"),
            ],
        },
        {
            "id": "inflation",
            "title": "Inflation and your money",
            "level": "Intermediate",
            "minutes": 8,
            "summary": "What inflation measures, why only real returns count, and which assets have tended to hold up when prices rise.",
            "body": """
**Inflation** is the rate at which the general level of prices rises. At 3% a year, something costing 100 today costs about 103 next year. Your money buys less, so what matters is not how many units of currency you have but what they can buy.

### The main measures

- **CPI (consumer price index)**: the price of a basket of goods and services a typical household buys, published monthly by statistics agencies in most countries.
- **Core inflation**: CPI without food and energy, which jump around. Core is a better guide to the underlying trend, though food and energy still hit your wallet.
- **PCE price index**: a US measure from the national accounts with a broader basket and weights that shift as people change what they buy. The Federal Reserve's 2% target is set on PCE, which usually runs a little below CPI.

Headline numbers are usually quoted **year on year**. Monthly numbers are smaller and noisier.

### Real returns

The **real return** is your return after inflation:

`Real return = (1 + nominal return) / (1 + inflation) - 1`

For small numbers, nominal minus inflation is a fair shortcut. A savings account paying 2% when inflation is 4% is losing about 2% of buying power a year, even though the balance goes up.

### What holds up, and what does not

There is no perfect inflation hedge, and results depend on whether inflation was expected:

- **Cash** keeps pace only if interest rates rise with inflation, and often lags.
- **Conventional bonds** suffer most from unexpected inflation: their fixed payments buy less and rising rates cut their prices.
- **Shares** can hold up over long periods because companies can raise prices, but they have often struggled during sudden inflation spikes, especially businesses that cannot pass on costs.
- **Commodities** have tended to do well when inflation is driven by energy and raw materials, but they are volatile and pay no income.
- **Property** gives mixed results, depending on rents and mortgage rates.

### Inflation-linked bonds

**Inflation-linked bonds** (TIPS in the US, index-linked gilts in the UK, real return bonds in Canada) adjust their principal with an inflation index, so they pay a known *real* yield if held to maturity. Their prices still move when real yields change.

> Rule of thumb: compare the yield on a normal government bond with an inflation-linked bond of the same maturity. The gap, called breakeven inflation, is roughly the inflation the market expects.
""",
            "example": {"title": "Worked example: 10,000 over 20 years at 3% inflation", "body": """
**Buying power of cash under the mattress**

- Prices after 20 years: 1.03^20 = **1.806** times today's level
- Buying power of 10,000: 10,000 / 1.806 = **5,537** in today's money, a loss of about 45%

**A savings account paying 1%**

- Real return each year: 1.01 / 1.03 - 1 = **-1.94%**
- After 20 years the balance is 10,000 x 1.01^20 = 12,202, but in today's money that is 12,202 / 1.806 = **6,756**

**A fund returning 6%**

- Real return: 1.06 / 1.03 - 1 = **2.91%** a year (the shortcut 6 - 3 = 3% is close)
- Balance: 10,000 x 1.06^20 = 32,071, worth 32,071 / 1.806 = **17,757** in today's money
"""},
            "terms": [
                ("Consumer price index (CPI)", "The price of a fixed basket of household goods and services, tracked over time to measure inflation."),
                ("Core inflation", "Inflation excluding food and energy prices, used to see the underlying trend."),
                ("PCE price index", "A US inflation measure from the national accounts with a broader basket than CPI; the Federal Reserve targets it."),
                ("Real return", "The return after adjusting for inflation: the change in what your money can buy."),
                ("Inflation-linked bond", "A bond whose principal rises with an inflation index, so it pays a known real yield if held to maturity."),
                ("Breakeven inflation", "The yield gap between a normal government bond and an inflation-linked bond of the same maturity: roughly expected inflation."),
            ],
            "cards": [
                ("Nominal return 7%, inflation 3%: what is the real return?", "1.07 / 1.03 - 1 = 3.88%. The shortcut 7 - 3 = 4% is close but slightly overstates it."),
                ("What is core inflation and why do central banks watch it?", "Inflation excluding food and energy. Those prices swing a lot, so core gives a clearer view of the underlying trend that policy can influence."),
                ("How does PCE inflation differ from CPI in the US?", "PCE has a broader basket and weights that change as people switch what they buy, and it usually runs a little below CPI. The Federal Reserve's 2% target is set on PCE."),
                ("Why do conventional bonds suffer most from unexpected inflation?", "Their payments are fixed in currency, so they buy less, and rising inflation pushes interest rates up, which lowers the price of existing bonds."),
                ("True or false: shares always protect you from inflation.", "False. Over long periods companies can raise prices, but shares have often done badly during sudden inflation spikes, especially firms that cannot pass on higher costs."),
                ("What does an inflation-linked bond guarantee if held to maturity?", "A known real yield: its principal rises with an inflation index. Its market price can still fall before maturity if real yields rise."),
                ("A 10-year government bond yields 4.2% and the 10-year inflation-linked bond yields 1.9%. What is breakeven inflation?", "About 4.2 - 1.9 = 2.3% a year: roughly the average inflation the market expects over the next 10 years."),
                ("Your savings account pays 2% and inflation is 4%. Are you getting richer?", "No. Your balance grows, but its buying power falls by about 2% a year: 1.02 / 1.04 - 1 = -1.9%."),
            ],
            "calc": "compound",
            "links": [
                ("FRED: consumer price index (US)", "https://fred.stlouisfed.org/series/CPIAUCSL"),
                ("US Bureau of Labor Statistics: CPI", "https://www.bls.gov/cpi/"),
            ],
        },
        {
            "id": "yield-curve",
            "title": "Reading the yield curve",
            "level": "Intermediate",
            "minutes": 8,
            "summary": "What normal, flat and inverted yield curves say about rate expectations, and what the inversion-recession record does and does not prove.",
            "body": """
The **yield curve** is a line plotting the yields of government bonds against their maturities, from a few months to 30 years. Its shape tells you what the bond market expects from interest rates and the economy.

### Three shapes

- **Normal (upward sloping)**: long bonds yield more than short ones. Investors expect rates to stay steady or rise and want extra pay for locking money up.
- **Flat**: short and long yields are similar. Often seen when a central bank has been raising rates and markets think it is near the end.
- **Inverted**: short yields are above long yields. Markets expect the central bank to *cut* rates in future, usually because they expect the economy to weaken or inflation to fall.

Analysts often summarise the curve with a **spread**: the 10-year yield minus the 2-year yield, or the 10-year minus the 3-month. A negative spread means an inverted curve. Spreads are quoted in **basis points**: one basis point is 0.01 percentage point.

### Expectations plus term premium

A long yield is roughly the average short rate expected over its life, plus a **term premium**: extra return for the risk that rates or inflation turn out differently while your money is locked in.

`Long yield = average expected short rate + term premium`

The term premium cannot be observed directly; it is estimated with models and has varied a lot, sometimes close to zero or even negative. So a flat curve does not always mean markets expect cuts.

### The inversion-recession record

In the US, an inverted curve has come before most recessions of the last several decades, usually with a lag of many months to a couple of years. That record is why inversions make headlines. Keep its limits in mind:

- The **lag is long and variable**, so it is a poor timing tool, and stocks have sometimes risen strongly after an inversion.
- There have been **false signals**, and the sample of recessions is small.
- QE and changes in the term premium may have **changed what the curve means**.
- Recessions often begin *after* the curve has un-inverted and steepened again, as the central bank starts cutting.

> Rule of thumb: treat an inverted curve as a reason to check your risk, not as a signal to sell everything.
""",
            "example": {"title": "Worked example: spreads and what the market expects", "body": """
Fictional government yields: 3-month **5.0%**, 1-year **5.0%**, 2-year **4.5%**, 10-year **3.8%**.

1. 10-year minus 2-year spread: 3.8 - 4.5 = **-0.7 percentage points**, or **-70 basis points**. The curve is inverted.
2. What does the 2-year yield imply for next year's 1-year rate? Ignoring the term premium, investing for 2 years at 4.5% should match 1 year at 5.0% then 1 year at the unknown rate f:
   - 1.045^2 = 1.050 x (1 + f)
   - 1.092025 = 1.050 x (1 + f), so 1 + f = 1.0400
   - f = **4.0%**
3. Reading: the market expects 1-year rates to fall about a percentage point over the next year, which usually means it expects central bank cuts. If there is a positive term premium, the expected fall is even larger.
"""},
            "terms": [
                ("Yield curve", "A plot of government bond yields against their maturities at one point in time."),
                ("Inverted yield curve", "A curve where short-term yields are above long-term yields, usually because markets expect rate cuts."),
                ("Term premium", "The extra yield investors demand for holding a long bond instead of rolling short ones; estimated, not observed."),
                ("Basis point", "One hundredth of a percentage point: 0.01%."),
                ("Yield spread", "The difference between two yields, such as the 10-year minus the 2-year government yield."),
            ],
            "cards": [
                ("What does an inverted yield curve usually say about market expectations?", "That short-term rates are expected to fall, usually because markets expect the economy to weaken or inflation to drop, prompting central bank cuts."),
                ("The 10-year yields 4.1% and the 2-year 4.6%. What is the spread in basis points?", "4.1 - 4.6 = -0.5 percentage points, which is -50 basis points. The curve is inverted between those maturities."),
                ("What is the term premium?", "The extra yield investors want for locking money into a long bond instead of rolling short ones, to cover the risk that rates or inflation turn out differently. It is estimated by models, not observed."),
                ("Why is an inverted curve a poor tool for timing the stock market?", "The lag before a recession has been long and variable, often many months to a couple of years, there have been false signals, and stocks have sometimes risen strongly after an inversion."),
                ("True or false: a recession starts the moment the yield curve inverts.", "False. In past cycles recessions have often begun much later, frequently after the curve had steepened again as the central bank started cutting."),
                ("The 1-year rate is 4% and the 2-year rate is 4.5%. Ignoring the term premium, what 1-year rate does the market expect a year from now?", "1.045^2 / 1.04 - 1 = 1.092025 / 1.04 - 1 = 5.0%. The market expects short rates to rise."),
                ("Why might the yield curve's signal be weaker than it used to be?", "Central bank bond buying and shifts in the term premium can flatten or invert the curve for reasons that have little to do with recession expectations, and the historical sample of recessions is small."),
            ],
            "calc": "bond",
            "links": [
                ("FRED: 10-year minus 2-year Treasury spread", "https://fred.stlouisfed.org/series/T10Y2Y"),
                ("FRED: 10-year minus 3-month Treasury spread", "https://fred.stlouisfed.org/series/T10Y3M"),
            ],
        },
        {
            "id": "business-cycle",
            "title": "The business cycle and earnings",
            "level": "Intermediate",
            "minutes": 9,
            "summary": "The four phases of the economy, why some sectors swing harder than others, and which indicators and revisions investors watch.",
            "body": """
Economies do not grow in a straight line. They move through a rough **business cycle**: periods of growth broken by slowdowns and, every so often, recessions. The phases have no fixed length, and nobody rings a bell when one ends.

### Four phases

1. **Expansion**: output, jobs and profits grow. Confidence and borrowing rise.
2. **Slowdown**: growth fades, costs and interest rates are often high, and profit margins get squeezed.
3. **Recession**: output and employment fall for a sustained period. A common shortcut is two quarters of falling GDP, but official bodies such as the NBER in the US look at a wider set of data.
4. **Recovery**: activity bottoms out and starts to grow, often helped by lower interest rates.

### Cyclical and defensive sectors

**Cyclical** sectors sell things people can put off: cars, travel, building materials, industrial machinery, luxury goods. Their sales swing with the economy, and because many have high fixed costs, profits swing even more. This is **operating leverage**.

**Defensive** sectors sell things people buy anyway: food staples, utilities, basic health care. Their profits are steadier, so they usually hold up better in recessions and lag in strong recoveries.

### Leading indicators

Markets look forward, so investors watch data that tends to turn before the economy does:

- **PMIs (purchasing managers' indices)**: monthly surveys of company buyers. Above 50 means more firms report growth than decline; below 50 means contraction.
- **Initial jobless claims**: weekly counts of new unemployment claims. A sustained rise is an early warning.
- **Building permits, new orders and the yield curve** also tend to lead.

No single indicator is reliable on its own. Look for several pointing the same way.

### Earnings revisions

Share prices follow expected profits. **Earnings revisions** are changes analysts make to their forecasts. When forecasts are cut across many companies, prices often fall twice: once for lower earnings and again because investors pay a lower multiple for shrinking profits.

`Price = earnings per share x P/E multiple`

> Common mistake: buying cyclicals on low P/E ratios at the top of the cycle. Their earnings are at a peak, so the P/E looks cheap just before profits fall.
""",
            "example": {"title": "Worked example: operating leverage and a double hit", "body": """
**Operating leverage at Granite Machines (fictional)**

- Revenue 100 million, fixed costs 60 million, variable costs 30% of revenue (30 million)
- Profit = 100 - 60 - 30 = **10 million**
- Recession: revenue falls 10% to 90 million. Variable costs fall to 27 million, fixed costs stay at 60 million
- Profit = 90 - 60 - 27 = **3 million**, a **70%** fall from a 10% drop in sales

**The double hit on the share price**

- Before: expected EPS 5.00 x P/E 16 = **80**
- Analysts cut EPS to 4.00 and investors pay only 14 times: 4.00 x 14 = **56**
- Fall: (56 - 80) / 80 = **-30%**, from a 20% cut in earnings
"""},
            "terms": [
                ("Business cycle", "The recurring pattern of expansion, slowdown, recession and recovery in economic activity."),
                ("Cyclical sector", "An industry whose sales and profits rise and fall strongly with the economy, such as cars or travel."),
                ("Defensive sector", "An industry with steady demand in good and bad times, such as food staples or utilities."),
                ("Operating leverage", "The effect of fixed costs that makes profits swing by a larger percentage than sales."),
                ("Purchasing managers' index (PMI)", "A monthly business survey where readings above 50 signal expansion and below 50 contraction."),
                ("Earnings revisions", "Changes analysts make to their profit forecasts; widespread cuts often come before or during downturns."),
            ],
            "cards": [
                ("Name the four phases of the business cycle.", "Expansion, slowdown, recession and recovery. The phases have no fixed length and are usually only dated with hindsight."),
                ("Why do cyclical companies' profits fall faster than their sales?", "Operating leverage: many have high fixed costs that do not shrink with sales, so a small drop in revenue takes a large bite out of profit."),
                ("A PMI reading of 47 means what?", "More purchasing managers report decline than growth, so that part of the economy is contracting. 50 is the dividing line."),
                ("Why do investors watch weekly jobless claims?", "They are timely and tend to rise before the wider job market weakens, so a sustained increase is an early recession warning."),
                ("Expected EPS falls from 6 to 5 and the P/E falls from 15 to 13. What happens to a share price of 90?", "New price = 5 x 13 = 65, a fall of about 28%, much more than the 17% cut in earnings, because the multiple shrank too."),
                ("Why can a low P/E on a cyclical stock be a trap?", "At the top of the cycle earnings are at a peak, so the P/E looks cheap just before profits fall. Cyclicals often look most expensive on P/E near the bottom."),
                ("True or false: a recession is officially two quarters of falling GDP everywhere.", "False. Two falling quarters is a common shortcut, but bodies such as the NBER in the US date recessions using a broad set of data, including jobs, income and output."),
                ("Which sectors usually hold up better in a recession, and why?", "Defensive sectors such as food staples, utilities and basic health care, because people keep buying those goods and services even when money is tight."),
            ],
            "calc": None,
            "links": [
                ("NBER: business cycle dating", "https://www.nber.org/research/business-cycle-dating"),
                ("FRED: initial jobless claims", "https://fred.stlouisfed.org/series/ICSA"),
            ],
        },
        {
            "id": "economic-calendar",
            "title": "Reading economic releases",
            "level": "Intermediate",
            "minutes": 7,
            "summary": "The big monthly releases, why the market reacts to the surprise versus consensus rather than the number itself, and how to read one calmly.",
            "body": """
Every week brings scheduled economic data. A small number of releases move markets far more than the rest, because they change what investors expect central banks to do.

### The releases that matter most

- **CPI (inflation)**: monthly. Watch headline and core, month on month and year on year.
- **Payrolls and unemployment**: in the US, the monthly jobs report shows jobs added and the unemployment rate, plus wage growth. Other countries publish similar labour force surveys.
- **GDP**: quarterly. The broadest measure of output, but it arrives late and is revised.
- **PMIs**: monthly business surveys, early and forward-looking.
- **Central bank meetings**: the rate decision, the statement, any new projections and the press conference.

An **economic calendar** lists each release with its date, time, the previous value and the **consensus**: the median forecast of economists surveyed beforehand.

### Surprises move markets, not levels

By release time, the consensus is already in prices. What moves markets is the **surprise**:

`Surprise = actual - consensus`

Strong job growth that matches the forecast may barely move prices. Weaker growth that is still far better than feared can send markets up. A hot inflation surprise often pushes bond yields up and stocks down, because it makes rate cuts less likely or hikes more likely.

### Reading a release without getting fooled

1. **Check the details**, not just the headline. Revisions to earlier months, core versus headline, and wages can matter as much as the main figure.
2. **Know the noise.** Monthly numbers bounce around. One month is rarely a trend.
3. **Watch the first reaction fade or grow.** Algorithms trade the headline in milliseconds; the more lasting move often comes as people read the details.
4. **Annualise carefully.** A monthly inflation rate of 0.3% is about 3.7% at an annual pace, so small monthly changes matter.

`Annual pace = (1 + monthly rate)^12 - 1`

> Rule of thumb: as a long-term investor you do not need to trade releases. Read them to understand why prices moved, not to react in the next five minutes.
""",
            "example": {"title": "Worked example: a hot inflation print", "body": """
Fictional release: monthly core inflation. Previous **0.2%**, consensus **0.3%**, actual **0.5%**.

1. Surprise: 0.5 - 0.3 = **+0.2 percentage points**, a large miss for a monthly figure.
2. Annual pace implied by the consensus: 1.003^12 - 1 = **3.7%**
3. Annual pace implied by the actual: 1.005^12 - 1 = **6.2%**
4. Likely first reaction: short-term bond yields rise as traders push back expected rate cuts, the currency strengthens, and rate-sensitive shares such as long-duration growth stocks fall.

Now suppose the same release had come in at 0.5% with a consensus of 0.6%. The level is identical, but the surprise is **-0.1**, so markets might rally on relief. The level is the same; the reaction depends on what was expected.
"""},
            "terms": [
                ("Consensus forecast", "The median forecast of surveyed economists for a release, published before it comes out."),
                ("Economic surprise", "The difference between a released figure and its consensus forecast."),
                ("Economic calendar", "A schedule of upcoming data releases and central bank events with previous values and forecasts."),
                ("Data revision", "A later change to a previously published figure as more complete information arrives."),
            ],
            "cards": [
                ("Why do markets react to the surprise rather than the level of a data release?", "The consensus forecast is already reflected in prices before the release, so only the gap between actual and expected changes the outlook."),
                ("Payrolls consensus 180,000, actual 120,000, previous month revised down by 50,000. How would you read it?", "Weaker than expected twice over: a 60,000 miss on the month plus a downward revision, so the job market looks softer than markets thought."),
                ("A monthly inflation rate of 0.4%: what is the annual pace?", "1.004^12 - 1, about 4.9% a year. Small monthly differences add up to large annual ones."),
                ("A hot inflation surprise usually does what to bond yields, and why?", "Pushes them up, especially short-term yields, because it makes central bank rate cuts less likely or hikes more likely."),
                ("True or false: a strong jobs number always lifts the stock market.", "False. If it was expected, it may do nothing. If it is so strong that markets expect higher rates for longer, stocks can fall on good news."),
                ("Why should you be careful reading too much into one month of data?", "Monthly figures are noisy and often revised. A trend needs several months of data pointing the same way."),
                ("What is the consensus figure on an economic calendar?", "The median forecast of economists surveyed before the release, used as the benchmark for whether the actual number is a surprise."),
            ],
            "calc": None,
            "links": [
                ("FRED economic data", "https://fred.stlouisfed.org/"),
                ("Federal Reserve: FOMC meeting calendar", "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"),
            ],
        },
    ],
}
