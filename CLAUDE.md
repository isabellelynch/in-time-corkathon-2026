# CLAUDE.md — Corkathon 2026

Guidance for Claude Code and the team's bots working in this repo.

## Brief
Corkathon 2026, sponsored by FRAME (accounting firm, Cork).
**Challenge:** take data that exists today and turn it into something a busy person can act on.
- Timing matters: the same data means different things in January and June. A stale or late answer can be worse than none.
- Data is scattered across systems, spreadsheets and inboxes. Pulling it together and trusting it is the hard part.
- Users are non-technical domain experts (accountants, SME owners) and must manage it without help.

**What great looks like**
1. A clear one-sentence idea. A well-argued concept with a rough prototype beats an unexplained polished build.
2. Honest about limits: what it does well, where it breaks, what more time would add.
3. Usable by non-technical people: a plain-language question gets a usable answer. No query language, no training.

**Data:** live open Irish data (data.gov.ie, CSO, public calendars and registers) or a dataset we build ourselves.

## Judging (equal weight)
- **Innovation:** fresh use of data, unexpected combination of sources, new insight. A dashboard alone scores poorly.
- **Impact:** who benefits, how, and why. Bigger and more credible is better.
- **Technical depth:** sound engineering, real data, sensible transformations, explainable design.
- **Presentation/demo:** show the data driving the result live. Clarity beats polish.

## Team rules
- Every change is a small PR. CI (tests + osv-scanner) must be green; Engineering Lead reviews and merges.
- Nothing public, deployed, or sent outside the team without Tran's explicit yes.
- No secrets in the repo. Use `.env` (git-ignored); document keys in `.env.example`.
- Pin every dependency to an exact version and commit the lockfile. New packages need: pinned version, osv-scanner clean, install-script review, SWE sign-off.
- Every answer shown to a user must say where the data came from and how fresh it is.
- Open data only; respect each source's licence and record it next to the loader. No personal data.
- Accessibility: WCAG 2.2 AA minimum.
- Never commit API keys, tokens, or scraped personal data.

## Run / test
Stack not chosen yet (waiting on Tran's concept pick). Until then:
```bash
cp .env.example .env    # fill locally, never commit
make test               # placeholder; replaced when the stack lands
```
CI runs osv-scanner on every PR (`.github/workflows/ci.yml`).
Update this section in the same PR that introduces the stack.
