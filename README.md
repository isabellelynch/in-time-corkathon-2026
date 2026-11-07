# Corkathon 2026

Team entry for Corkathon 2026 (sponsor: FRAME, Cork): turning live Irish open data into timely, plain-language answers a busy accountant or SME owner can act on.

**Status:** concept selection. See [CLAUDE.md](CLAUDE.md) for the brief, judging criteria, team rules and commands.

## Getting started
```bash
cp .env.example .env
make test
```

## Limits

### What it does well
- **Live, official data.** Pulls coffee import values and volumes (Eurostat Comext), Irish import totals (CSO) and the euro–dollar rate (ECB) straight from the source.
- **Always says where a number came from and how fresh it is.** Every figure carries its source, licence, reference period and when we retrieved it.
- **Doesn't break in a demo.** If a live source is down, it falls back to the last saved snapshot and says so, rather than failing or showing nothing.
- **Tested.** Offline test suite against saved real responses; runs on every pull request.

### Where it breaks
- **Trade data lags.** Import figures arrive about 2–3 months late (latest available is August 2026). They show the trend, not today's price.
- **National average, not your price.** The cost per kg is the average across all Irish coffee imports. It mixes green and roasted, all origins and all grades, so a café's supplier price can differ a lot.
- **Correlation, not a forecast.** We show how the exchange rate and import costs have moved together; we don't predict what a supplier will charge.
- **Exchange-rate timing is approximate.** The ECB API gives the rate but not an exact publication time, so freshness is shown as the date only.
- **Coffee only.** Other café costs (milk, energy, wages, rent) aren't included.
- **Licence wording.** Eurostat Comext reuse terms are applied per the general Eurostat notice; the exact Comext wording is still to be confirmed.

### What more time would add
- More cost lines for a café: dairy, energy and wage data from the CSO.
- Futures prices for coffee, to give an earlier signal than the delayed import data.
- Sector context from the CRO company register (e.g. how many cafés in Cork are affected).
- Alerts when a new release changes the picture, instead of waiting to be asked.
- Testing with real café owners and accountants.
