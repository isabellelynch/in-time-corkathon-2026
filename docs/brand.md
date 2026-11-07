# Brand

> Owner: Isabelle. **This records the look the app already has** (the "Night Harbour" theme in `web/styles.css`). It is not a redesign. The one change it proposes is the product name, pending Khoi's OK.

## Name

**In Time**

*Find out before your stock runs out.*

- Says the benefit, not the technology. An importer's real fear is finding out too late.
- Short, plain English, easy to say on stage.
- The question the product answers stays as the page heading: **"Will my imports be late or dearer?"**
- Currently the page header says "Imports check". Proposed: "In Time" in the header and `<title>`, with the question kept as the main heading.

## Voice

| Do | Don't |
|---|---|
| Plain English a busy owner reads in 10 seconds | Logistics or finance jargon ("transshipment exposure") |
| Say when we don't know: "We can't determine whether your shipment is affected." | Reassure without evidence: never "No action needed" |
| One next step, in the imperative: "Ask your forwarder for a current ETA." | Lists of options or vague advice |
| Name the source and date of every number | Unsourced figures or "real-time" claims |
| Separate rumour from fact: "reported" vs "confirmed" | Alarmist words: "crisis", "urgent", red-alert styling |
| Say what isn't ours: "This isn't your bank's rate." | Imply we see the user's own container or bank |

Example headline: *"Check your forwarder's ETA today: your stock runs out 14 days before a new order would arrive."*

## Colour

From the app's design tokens (`web/styles.css`, defined in OKLCH; hex values are close equivalents for slides and documents). Dark is the primary look; light follows the reader's system setting.

| Role | Token | Dark | Light | Used for |
|---|---|---|---|---|
| Background | `--bg` | `#040F1D` | `#FAF6EF` | Page |
| Surface | `--bg2` | `#081527` | — | Panels, map |
| Text | `--fg` | `#F2EEE6` | `#0A1B2F` | Body and headings |
| Muted text | `--muted` | `#A7B7C3` | `#3F5265` | Captions, "How sure" |
| Accent (amber) | `--accent` | `#F6BC5D` | `#7D460B` | Main button, highlights |
| Route | `--route` | `#72D6E3` | `#005574` | Route line, links |
| Warning | `--warn` | `#FFB95B` | `#8C4400` | Stock shortfall, confirmed event |
| Calm | `--calm` | `#76DFBC` | `#0E5E49` | "About the same", nothing to act on |
| Unknown | `--unk` | `#BDC1E5` | `#51507B` | "Nothing reported", can't tell |

Rules:
- **Amber means "act", not "danger".** There is no red status colour: the product warns, it doesn't alarm.
- **Colour never carries meaning alone.** Every status has a word and an icon ("⚠ 14 days short").
- **Contrast:** WCAG 2.2 AA in both themes (the team rule; the page passes automated checks with 0 violations).

The pitch deck uses a slightly lighter navy (`#13233A`), a warm off-white (`#F6F3EC`) and a deeper amber (`#E8913A`) so it projects well; same family, tuned for screens in bright rooms.

## Typography

| Use | App | Deck |
|---|---|---|
| Display and headlines | **Gloock** (serif, self-hosted, OFL) | Libre Baskerville |
| Body and interface | **Work Sans** (self-hosted, OFL) | Inter |

- Headlines in the serif, sentence case, no full stops on labels.
- Status words big and short: "14 days short", "Nothing reported", "About the same".
- Numbers always with units and dates: "ECB rate as of 6 Nov".

## Logo

Not required for judging; a wordmark is enough.

- **Wordmark:** "In Time" in Gloock, in `--fg`, with the amber arc already used in the page header placed before it, as a horizon or the edge of a clock.
- **Clear space:** the height of the capital "I" on every side.
- **Don't:** add ships, containers, globes or clocks with hands; recolour the wordmark amber on navy at small sizes (contrast drops).

## Where the brand appears

| Place | Status |
|---|---|
| Pitch deck (10 slides) | Uses "In Time" |
| README title | To change, with Khoi's OK |
| Page header and `<title>` (`web/index.html`) | To change, with Khoi's OK |
| `CLAUDE.md` | Optional pointer, so agents follow this file: *"For the product name, wording and colours, follow docs/brand.md."* Khoi's call |
