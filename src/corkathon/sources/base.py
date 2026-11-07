"""Minimal shared loader base.

TEMPORARY: to be replaced by Engineering Lead's PR A (shared result shape,
base loader, snapshot mode). Field names follow that plan so loaders port
over unchanged. Stdlib only.

Result fields: source_id, endpoint, licence, reference_period, published_at,
retrieved_at, status (ok | stale | unavailable | snapshot), reason, records.

Modes:
- live (default): fetch; on any failure fall back to the newest committed
  snapshot, labelled status="snapshot". No snapshot -> status="unavailable".
- SNAPSHOT=1: never touch the network; read the newest snapshot (or the one
  dated SNAPSHOT_DATE=YYYY-MM-DD) from data/snapshots/<source_id>/.
"""
from __future__ import annotations

import json
import os
import urllib.error
import urllib.request
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

STATUSES = ("ok", "stale", "unavailable", "snapshot")
REPO_ROOT = Path(__file__).resolve().parents[3]
SNAPSHOT_DIR = Path(os.environ.get("SNAPSHOT_DIR", REPO_ROOT / "data" / "snapshots"))
USER_AGENT = "corkathon-2026/0.1 (+https://github.com/khoivd-dot/Corkathon-2026)"
TIMEOUT_S = float(os.environ.get("SOURCE_TIMEOUT_S", "20"))


@dataclass
class Licence:
    name: str
    url: str
    attribution: str


@dataclass
class SourceResult:
    source_id: str
    endpoint: str
    licence: Licence
    status: str
    retrieved_at: str
    reference_period: str | None = None  # the data's own latest period
    published_at: str | None = None  # when the publisher released/updated it
    reason: str | None = None
    records: list[dict[str, Any]] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.status not in STATUSES:
            raise ValueError(f"bad status {self.status!r}")

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "SourceResult":
        d = dict(d)
        d["licence"] = Licence(**d["licence"])
        return cls(**d)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


class FetchError(Exception):
    """Raised inside fetch/parse; always caught by Loader.load()."""


def http_get(url: str, data: bytes | None = None, timeout: float = TIMEOUT_S) -> bytes:
    req = urllib.request.Request(url, data=data, headers={"User-Agent": USER_AGENT})
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read()
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        raise FetchError(f"network: {e}") from e


def http_json(url: str, data: bytes | None = None) -> Any:
    raw = http_get(url, data)
    try:
        return json.loads(raw)
    except ValueError as e:
        raise FetchError(f"not JSON: {raw[:120]!r}") from e


class Loader:
    source_id: str = ""
    endpoint: str = ""
    licence: Licence

    def fetch(self) -> Any:
        """Return raw payload from the network. May raise anything."""
        raise NotImplementedError

    def parse(self, payload: Any) -> tuple[list[dict], str | None, str | None]:
        """Return (records, reference_period, published_at). May raise."""
        raise NotImplementedError

    def _result(self, status: str, **kw: Any) -> SourceResult:
        return SourceResult(source_id=self.source_id, endpoint=self.endpoint,
                            licence=self.licence, status=status,
                            retrieved_at=kw.pop("retrieved_at", now_iso()), **kw)

    def load_live(self) -> SourceResult:
        try:
            records, ref, pub = self.parse(self.fetch())
        except Exception as e:  # noqa: BLE001 - loaders never raise
            return self._result("unavailable", reason=f"{type(e).__name__}: {e}"[:300])
        return self._result("ok", records=records, reference_period=ref, published_at=pub)

    def load_snapshot(self, reason: str | None = None) -> SourceResult:
        path = latest_snapshot(self.source_id, os.environ.get("SNAPSHOT_DATE"))
        if path is None:
            return self._result("unavailable", reason=(reason or "") + " | no snapshot")
        res = SourceResult.from_dict(json.loads(path.read_text()))
        res.status = "snapshot"
        res.reason = f"snapshot {path.stem}" + (f" (live failed: {reason})" if reason else "")
        return res

    def load(self) -> SourceResult:
        if os.environ.get("SNAPSHOT") == "1":
            return self.load_snapshot()
        res = self.load_live()
        if res.status == "unavailable":
            return self.load_snapshot(res.reason)
        return res


def latest_snapshot(source_id: str, date: str | None = None) -> Path | None:
    d = SNAPSHOT_DIR / source_id
    if date:
        p = d / f"{date}.json"
        return p if p.exists() else None
    files = sorted(d.glob("*.json")) if d.exists() else []
    return files[-1] if files else None


def write_snapshot(res: SourceResult) -> Path:
    day = res.retrieved_at[:10]
    p = SNAPSHOT_DIR / res.source_id / f"{day}.json"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(res.to_dict(), indent=1, ensure_ascii=False) + "\n")
    return p
