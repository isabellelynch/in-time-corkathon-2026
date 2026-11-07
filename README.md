# Corkathon 2026

Team entry for Corkathon 2026 (sponsor: FRAME, Cork): turning live Irish open data into timely, plain-language answers a busy accountant or SME owner can act on.

**Imports check:** a small Irish importer enters one shipment route, their invoice currency and how long their stock lasts, and gets a plain-English answer to *"Will my imports be late or dearer this month?"*, with one next step and every source dated.

**Status:** prototype in progress. See [docs/](docs/README.md) for the plan, architecture, data sources and pitch, and [CLAUDE.md](CLAUDE.md) for the brief, judging criteria and team rules.

## Getting started
```bash
cp .env.example .env
make test
PYTHONPATH=src python3 -m corkathon.server   # then open http://localhost:8000
```
On Windows PowerShell, see [docs/contributing.md](docs/contributing.md#on-windows-powershell).

## Limits

### What it does well
- **Checks your route, not the whole world.** Only news naming a port on the route you entered, inside your dates, is shown. We never guess your route.
- **Separates rumour from confirmation.** A news story is shown as "reported". It only counts as "confirmed" when a carrier or port authority's own notice names the event and a place on your route.
- **Says when it doesn't know.** It never says "No action needed". When it can't tell, it says so, still flags a stock shortfall, and links to the official notices of the ports it can't check.
- **Ties it to your business.** Compares your stock with your order lead time, and works out the exchange-rate effect on the part of your invoice you haven't fixed.
- **Says where every number came from and how fresh it is.** Every figure carries its source, period and when we checked it.
- **Keeps your information private.** What you type is never saved, cached or logged.
- **Doesn't break in a demo.** If a live source is down, it uses the last saved copy and says so.
- **Tested.** 77 offline tests run on every pull request.

### Where it breaks
- **We can't see your shipment.** A confirmed port problem on your route may or may not affect your container; we tell you to check with your forwarder.
- **News is a signal, not proof.** Matching is by keywords, so irrelevant stories can match a port name, and quiet delays may never be reported.
- **No live alerts yet.** Confirmation is switched off until the reuse terms of carrier and port advisories are recorded, so today every event is "reported" and the app never raises an alert.
- **Few confirming sources.** Even when switched on, "confirmed" relies on a fixed list of major carriers and ports; smaller ones can only ever show as "reported".
- **Not your bank's rate.** Currency figures use ECB reference rates, published once a working day, with no exact release time.
- **Five foreign currencies only:** US dollar, sterling, yuan, yen and Swiss franc (plus euro).
- **No ship tracking.** Vessel position data was left out because its display rights aren't confirmed.
- **Trade statistics lag** about 2–3 months, so they're shown as background only.

### What more time would add
- Ship-tracking and port-call data, once licensing is clear.
- More official confirming sources: more ports, carriers and canal authorities.
- Alerts when something changes on your route, instead of waiting to be asked.
- Several routes and shipments at once, e.g. for an accountant with many importing clients.
- Testing with real importers and accountants.
