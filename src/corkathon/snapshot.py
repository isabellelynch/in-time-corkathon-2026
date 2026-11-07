"""Write a dated snapshot per source: python -m corkathon.snapshot [source_id ...]"""
from __future__ import annotations

import sys

from .sources.base import write_snapshot
from .sources.registry import LOADERS


def main(argv: list[str]) -> int:
    names = argv or list(LOADERS)
    for name in names:
        res = LOADERS[name]().load_live()
        if res.status != "ok":
            print(f"{name}: {res.status} ({res.reason}); snapshot not written")
            continue
        print(f"{name}: ok ref={res.reference_period} -> {write_snapshot(res)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
