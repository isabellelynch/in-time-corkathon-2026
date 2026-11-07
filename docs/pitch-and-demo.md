# Pitch and demo plan

> **Draft.** Fill in the [brackets] once the team confirms the one-line idea and target user. Owner: Isabelle.

## One-line idea

**For café owners and their accountants, who get hit by coffee price rises with no warning, we combine live trade data, exchange rates and shipping news to explain what's happening to their coffee costs and why, in plain English, with every number sourced.**

## Who it's for

**Isabelle, runs a café in Cork city.** Buys roasted beans from a local roaster. Gets a letter saying prices go up 12% next month and has no idea if that's fair or what's next. Her accountant at FRAME wants to give her a straight answer quickly.

Impact number to find: how many cafés in Cork (CRO register, sector 5630, Cork Eircodes): **150**, and in Ireland: **3,500**.

## How it fits the judging (equal weight)

| Criterion | Our answer |
|---|---|
| Innovation | Joins sources nobody puts together for a café: EU trade data + ECB rates + live shipping news. Explains *why*, not just *what*. Not a dashboard. |
| Impact | around 150 cafés in Cork, around 3,500 nationally; accountants advising them. Earlier warning on a major cost. |
| Technical depth | Real live data, four official sources, freshness and licence on every figure, never-fail fallback, tested. |
| Presentation | Live question → answer with sources showing on screen. |

## Demo questions (to agree with the developer)

Pick three. Each should be answered live, with sources shown.

1. **"Why are my coffee costs going up?"** → cost per kg trend from Comext, dollar movement from ECB, recent shipping incidents from GDELT.
2. **"Is my supplier's 12% rise reasonable?"** → compare with the national import cost change over the same period, clearly labelled as an average.
3. **"Should I expect more rises?"** → shipping news and currency direction as early signals, with the honest caveat that this is not a forecast.
4. *(Accountant)* **"Which of my café clients should I warn this month?"** → only if client lists are in scope.

For each, write down the expected answer before the demo, so you know if something's wrong.

## Three-minute script

| Time | Who | What |
|---|---|---|
| 0:00–0:30 | Pitcher | The problem: Isabelle's supplier letter. "She has no way to know if it's fair or what's next." |
| 0:30–0:45 | Pitcher | The idea in one line. |
| 0:45–2:00 | Developer | Live demo: type question 1, show the answer and the source line. Then question 2. |
| 2:00–2:30 | Pitcher | Why it's different: the combination of sources; the freshness on every figure. |
| 2:30–2:50 | Pitcher | Honest limits (one sentence each, from the README). |
| 2:50–3:00 | Pitcher | Impact number and close. |

## Demo safety checklist

- [ ] Run `make snapshot` the morning of the demo so saved copies are fresh.
- [ ] Rehearse in snapshot mode (`SNAPSHOT=1`) in case the Wi-Fi fails.
- [ ] Record a backup screen video once the demo works.
- [ ] Laptop charged, screen zoomed so the back row can read it.
- [ ] Know the submission deadline and what has to be uploaded.
- [ ] Nothing public or sent outside the team without Tran's yes.

## Likely judge questions

- *"How is this different from just Googling coffee prices?"* → Irish import data, specific to what lands here, combined with currency and shipping news, with sources.
- *"How fresh is it?"* → Exchange rate: yesterday. News: hours. Trade data: about 2–3 months, which is why the news and currency signals matter.
- *"Would an accountant actually use it?"* → [answer after asking a FRAME mentor if possible].
- *"What would you do with more time?"* → See README Limits.
