# Project plan

## Goal

By the demo, show a working prototype where a café owner or accountant asks a plain-English question about coffee costs and gets a sourced, dated answer built from live data.

## Key times

| What | When |
|---|---|
| Hacking started | Sat 7 Nov, ~09:50 |
| Concept chosen | ~10:45 (coffee import costs) |
| Code freeze | Sat 7 Nov, ~17:00 |
| Submission deadline | Sat 7 Nov, 19:00 |
| Demo / judging | Sat 7 Nov, 19:45 |

## Roles

| Person | Role | Owns |
|---|---|---|
| Khoi (khoivd-dot) | Engineering Lead | Architecture, code review, shared base ("PR A") |
| SWE bot (Grok) + Claude Code | Builders | Data loaders, tests |
| Isabelle | Product, data and pitch | Docs, demo questions, impact number, Limits, pitch, submission |

## Milestones

| # | Milestone | Done when | Status |
|---|---|---|---|
| M0 | Repo set up | CLAUDE.md, CI, rules in place | 10:06 |
| M1 | Concept chosen | One-line idea agreed by Tran |  |
| M2 | Data loaders | Comext, CSO, ECB, GDELT on `main`, tests green | built; some merged to feature branches, not `main` |
| M3 | Shared base (PR A) | Temporary `base.py` replaced |  |
| M4 | Insight engine | Combines sources into a few computed facts (cost/kg change, FX change, incident count) with freshness |  |
| M5 | Plain-English answers | 3 agreed demo questions return correct, sourced answers |  |
| M6 | User screen | Simple, accessible page to ask and see answers |  |
| M7 | Demo ready | Snapshots fresh, rehearsed twice, backup video recorded |  |
| M8 | Submitted | Repo, README, Limits, video and form in |  |

## Work breakdown

### Engineering
- [ ] Merge `feat/loader-ecb-fx` (contains Comext and ECB) and the GDELT loader into `main`
- [ ] PR A: shared base, replacing `base.py`
- [ ] Define when data counts as `stale` per source (e.g. FX > 3 days, trade > 4 months)
- [ ] Insight functions: cost per kg month-on-month and year-on-year; FX % change over 30 days; shipping incidents in last 14 days
- [ ] Answer templates for the 3 demo questions, each ending with a source and freshness line
- [ ] Decide whether an AI model words the answers (`LLM_ENABLED`); if so, it may only rephrase computed facts, never add numbers
- [ ] Simple web page: question box, answer, sources; keyboard-usable, readable contrast (WCAG 2.2 AA)
- [ ] Tests for insights and answers

### Product, data and pitch (Isabelle)
- [x] Limits section in README
- [x] Docs: architecture, data sources guide, contributing, pitch and demo, this plan
- [ ] Confirm one-line idea and target user
- [ ] Agree 3 demo questions with the developer, with expected answers
- [ ] Impact number from CRO register (sector 5630, Cork Eircodes)
- [ ] If possible, ask a FRAME mentor: "Would you use this with café clients?"
- [ ] Slides (3–4 max) and 3-minute script
- [ ] Rehearse twice, record backup video
- [ ] Submission form and links

## Suggested timeline

Adjust to the real deadline.

| Block | Engineering | Product / pitch |
|---|---|---|
| Now → +1 h | Merge loaders to `main`; PR A | Confirm idea; demo questions; impact number |
| +1 h → +3 h | Insight functions + tests | Pitch script; slides; mentor feedback |
| +3 h → +5 h | Answer templates; simple screen | Update Limits and docs to match the build |
| +5 h → freeze | Polish, accessibility pass, fresh snapshots | Rehearse; backup video |
| Freeze → deadline | Bug fixes only | Submit |

## Decisions log

| When | Decision | By |
|---|---|---|
| 10:06 | Every change via small PR; merges need Tran's OK | Team |
| ~10:45 | Concept: coffee import costs for cafés | Tran |
| ~10:45 | Python 3.12, standard library only | Engineering |
| ~10:45 | Loaders never fail; fall back to saved snapshots | Engineering |
| | [AI model for wording: yes / no] | |
| | [Target user: café owner / accountant / both] | |

## Risks

| Risk | Likelihood | Impact | Plan |
|---|---|---|---|
| Wi-Fi fails during demo | Medium | High | Snapshot mode; backup video |
| Trade data looks too old to judges | High | Medium | Lead with news and FX as early signals; say so in Limits |
| News matches irrelevant stories | High | Medium | Show as "signals", link the articles, keep it out of headline numbers |
| Scope creep (too many features) | Medium | High | Three demo questions only; anything else goes in "with more time" |
| Code merged to wrong branch | Happened | Medium | Check PR base is `main`; see contributing guide |
| Answer states a number without source | Low | High (team rule) | Every template ends with the source line; test for it |
| Licence terms unconfirmed (Comext, GDELT) | Medium | Low | Confirm before submission; note in sources.md |

## Definition of done (for the demo)

- Three questions answered live from real data
- Every answer shows source and freshness
- Works with Wi-Fi off (snapshot mode)
- README explains the idea, how to run it, and its limits
- CI green on `main`
