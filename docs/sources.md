# Data sources

| source_id | Endpoint | Licence | Attribution | Role |
|---|---|---|---|---|
| cso_trade | CSO PxStat TSM06 (imports by SITC group, monthly, EUR thousand) | CC BY 4.0 — https://www.cso.ie/en/aboutus/whoweare/copyrightpolicy/ | Source: Central Statistics Office, Ireland | Context only |

# Dependency vetting
No third-party packages: stdlib `urllib`/`json`/`unittest` only. Nothing to pin or scan yet;
osv-scanner in CI still runs and exits 128 (no lockfiles), which the workflow accepts.
