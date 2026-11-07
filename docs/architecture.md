# How the app works

## The idea in one line

Pull live official data on coffee import costs, the euro–dollar rate and shipping news, and turn it into a plain-English answer a café owner or their accountant can act on, always saying where each number came from and how fresh it is.

## Big picture

```
 Live sources                 Loaders (src/corkathon/sources)          App (not built yet)
 ─────────────                ───────────────────────────────          ───────────────────
 Eurostat Comext  ──fetch──▶  comext.py    ─┐
 CSO PxStat TSM06 ──fetch──▶  cso_trade.py ─┤  each returns a          plain-English
 ECB Data Portal  ──fetch──▶  ecb_fx.py    ─┼─ SourceResult ──────────▶ answer + source
 GDELT DOC 2.0    ──fetch──▶  gdelt.py     ─┘  (records + freshness)    and freshness line
                                  │
                       live fetch fails?
                                  ▼
                     data/snapshots/<source>/<date>.json
```

## Key pieces

| File | What it does |
|---|---|
| `src/corkathon/sources/base.py` | Shared `Loader` class, the `SourceResult` shape, HTTP helpers, snapshot read/write. **Temporary**: to be replaced by the Engineering Lead's "PR A", keeping the same field names. |
| `src/corkathon/sources/<source>.py` | One loader per data source. Each implements `fetch()` (get raw data) and `parse()` (turn it into records). |
| `src/corkathon/sources/registry.py` | The list of loaders by name (`comext`, `cso_trade`, `ecb_fx`, `gdelt`). |
| `src/corkathon/snapshot.py` | Command that fetches every source live and saves a dated copy. |
| `data/snapshots/` | Saved copies of real responses, one JSON file per source per day. |
| `tests/` | Offline tests using saved responses in `tests/fixtures/`. |

## The result every loader returns

Every loader returns the same shape (`SourceResult`), so the app can treat all sources alike:

| Field | Meaning |
|---|---|
| `source_id` | e.g. `comext` |
| `endpoint` | The exact URL or API call used |
| `licence` | Name, URL and the attribution line to show users |
| `status` | `ok` (live), `snapshot` (saved copy used), `unavailable` (nothing to show), `stale` (reserved, not used yet) |
| `reference_period` | The latest period the data covers, e.g. `2026-08` |
| `published_at` | When the publisher released it (can be empty, e.g. ECB, GDELT) |
| `retrieved_at` | When we fetched it |
| `reason` | Why a fallback happened, if it did |
| `records` | The data rows |

**Team rule:** every answer shown to a user must say where the data came from and how fresh it is. `licence.attribution`, `reference_period` and `retrieved_at` are there to make that easy.

## Never-fail design

Loaders never crash the app:

1. **Live mode (default):** try the live source. If anything goes wrong, use the newest saved snapshot and mark it `snapshot`, with the reason.
2. **No snapshot either:** return `unavailable` with the reason.
3. **Snapshot mode (`SNAPSHOT=1`):** never touch the network; read saved copies only. `SNAPSHOT_DATE=YYYY-MM-DD` picks a specific day.

Use snapshot mode for the live demo if the venue Wi-Fi is unreliable, and say so on screen: the status line will show it.

## Running it

Python 3.12, standard library only (no packages to install).

```bash
cp .env.example .env     # settings; never commit .env
make test                # offline test suite
make snapshot            # fetch all sources live, save today's snapshots
SNAPSHOT=1 make test     # example: force snapshot mode
```

Settings in `.env`: `SNAPSHOT`, `SNAPSHOT_DATE`, `SOURCE_TIMEOUT_S` (default 20 s), and `LLM_ENABLED` / `LLM_API_KEY` (off by default, only if an AI model is later used to word answers).

## Adding a new data source

1. Create `src/corkathon/sources/<name>.py` with a class inheriting `Loader`. Set `source_id`, `endpoint` and `licence`; implement `fetch()` and `parse()`. `parse()` returns `(records, reference_period, published_at)`.
2. Register it in `registry.py`.
3. Save a real response to `tests/fixtures/` and add `tests/test_<name>.py`.
4. Add a row to `docs/sources.md` (licence, attribution, role) and a section to `docs/data-sources-guide.md`.
5. Run `make snapshot` and commit the new snapshot.
6. Open a small PR (see `docs/contributing.md`).

## Not built yet

- The part that combines sources into an answer (e.g. "coffee import cost per kg went up X% while the dollar rose Y%").
- The user-facing screen where someone asks a question.
- Accessibility checks (team rule: WCAG 2.2 AA minimum).

## Known gaps in the code

- `stale` status exists but nothing sets it yet; there's no rule for when data counts as too old.
- `base.py` is a stand-in until PR A lands.
- Some loader PRs were merged into other feature branches rather than `main`; check `main` actually has all four loaders.
