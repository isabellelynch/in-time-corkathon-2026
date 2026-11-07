# Data sources guide

Plain-English notes on each source: what it measures, how late it is, and the catches. The licence table lives in [`sources.md`](sources.md); keep both in step.

Figures below are from the snapshots saved on 7 Nov 2026.

## At a glance

| Source | What it tells us | How often | Latest data (7 Nov) | Lag | Role |
|---|---|---|---|---|---|
| Eurostat Comext | Value and weight of coffee imported into Ireland from outside the EU | Monthly | Aug 2026 | ~2–3 months | Core cost signal |
| CSO TSM06 | Irish imports by product group (coffee/tea/cocoa/spices; all food) | Monthly | Aug 2026 | ~2–3 months | Context |
| ECB reference rate | US dollars per euro | Every working day | 6 Nov 2026 | ~1 day | Currency pressure |
| GDELT | News about port strikes and shipping disruption | Continuous | Last 14 days | Minutes–hours | Early warning, noisy |

## Eurostat Comext (`comext`)

- **What:** Ireland's monthly imports of **HS 0901 (coffee)** from countries outside the EU, in euros and in units of 100 kg. Dividing one by the other gives an average **cost per kg** (about €9.20/kg in August 2026).
- **Dataset:** DS-045409. Loader fetches from June 2025 onward.
- **Catches:**
  - HS 0901 covers green and roasted, decaf and regular, every origin and grade. The per-kg figure is a national average, not any café's supplier price.
  - Coffee imported via another EU country (e.g. roasted in Germany) isn't in "extra-EU" figures.
  - Recent months can be revised.
- **Licence:** Eurostat free reuse (CC BY 4.0 per the general notice; exact Comext wording still to confirm). Say "Source: Eurostat" and state any changes we make to the figures.

## CSO TSM06 (`cso_trade`)

- **What:** Value of Irish imports in € thousand for two groups: **coffee, tea, cocoa, spices** (code 001008) and **total food and live animals** (code 001). Last 13 months.
- **Published:** the August figures came out 16 Oct 2026.
- **Catches:**
  - It's a broad group, so tea and cocoa move it too.
  - Value only, no weight, so it can't give a price per kg on its own. Use it for the trend and to cross-check Comext.
- **Licence:** CC BY 4.0. Attribution: "Source: Central Statistics Office, Ireland (table TSM06)."

## ECB euro reference rate (`ecb_fx`)

- **What:** Daily official US dollars per euro, last 30 working days. It moved from 1.1378 (28 Sep) to 1.1165 (6 Nov 2026).
- **Why it matters:** coffee is traded internationally in dollars, so a weaker euro tends to make imports dearer. That's a tendency, not a rule; suppliers hedge and contracts lag.
- **Catches:**
  - The API gives no exact release time, so `published_at` is empty. ECB publishes around 16:00 CET each working day.
  - No rates at weekends or on TARGET holidays.
- **Licence:** ESCB free reuse policy. **We must not modify the statistics**, and must quote the source: "Source: ECB statistics." Derived figures (e.g. % change) should be clearly labelled as our calculation.

## GDELT news (`gdelt`)

- **What:** News articles from the last 14 days matching port strikes, shipping disruption, Red Sea shipping or port congestion. Near-duplicate stories are grouped into "incidents", with counts per query.
- **Why it matters:** it can explain *why* costs might move, months before trade data shows it.
- **Catches:**
  - **Signal, not proof.** Matching is by keywords, so irrelevant or exaggerated stories get in.
  - The grouping of duplicates is approximate.
  - Not filtered to coffee routes yet.
  - GDELT allows at most 1 request every 5 seconds; the loader waits 6 seconds between queries.
- **Licence:** free with citation (terms to confirm). Attribution: "Source: The GDELT Project."

## Candidate source: CRO company register (not built)

- Free daily file of every Irish company, CC BY 4.0, from [opendata.cro.ie](https://opendata.cro.ie).
- Has `nace_v2_code` (sector; 5630 = beverage serving, i.e. cafés and bars), `eircode` (first three characters give the area, e.g. T12 = Cork) and `nard` (next annual return date).
- Useful for the **impact** number: how many cafés in Cork or Ireland this affects. Check how often the sector code is blank before relying on it.
- Contains company names and addresses (business data, not personal data), but follow the team's no-personal-data rule: use counts, not lists of named sole traders.

## Freshness: what to tell the user

Every answer should show something like:

If a loader returned `snapshot`, say "saved copy from <date>" instead of implying it's live.
