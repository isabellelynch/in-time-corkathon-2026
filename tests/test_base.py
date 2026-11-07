import json
import unittest
from pathlib import Path
from unittest import mock

from corkathon.sources import base
from corkathon.sources.base import Licence, Loader, SourceResult

from .helpers import no_network, tmpdir


class Dummy(Loader):
    source_id = "dummy"
    endpoint = "https://example.invalid"
    licence = Licence("CC BY 4.0", "https://example.invalid/l", "Source: test")

    def fetch(self):
        return base.http_json(self.endpoint)

    def parse(self, payload):
        return [{"x": 1}], "2026-01", None


class BaseTests(unittest.TestCase):
    def test_bad_status_rejected(self):
        with self.assertRaises(ValueError):
            SourceResult("a", "e", Dummy.licence, "weird", "t")

    def test_network_failure_unavailable_without_snapshot(self):
        with tmpdir() as d, mock.patch.object(base, "SNAPSHOT_DIR", Path(d)), no_network():
            r = Dummy().load()
        self.assertEqual(r.status, "unavailable")
        self.assertIn("network", r.reason)

    def test_network_failure_falls_back_to_labelled_snapshot(self):
        with tmpdir() as d, mock.patch.object(base, "SNAPSHOT_DIR", Path(d)):
            snap = SourceResult("dummy", "e", Dummy.licence, "ok", "2026-11-01T00:00:00+00:00",
                                reference_period="2026-01", records=[{"x": 1}])
            base.write_snapshot(snap)
            with no_network():
                r = Dummy().load()
        self.assertEqual(r.status, "snapshot")
        self.assertIn("2026-11-01", r.reason)
        self.assertEqual(r.records, [{"x": 1}])

    def test_snapshot_mode_never_fetches(self):
        with tmpdir() as d, mock.patch.object(base, "SNAPSHOT_DIR", Path(d)), \
                mock.patch.dict("os.environ", {"SNAPSHOT": "1"}), \
                mock.patch.object(Dummy, "fetch", side_effect=AssertionError("fetched")):
            r = Dummy().load()
        self.assertEqual(r.status, "unavailable")

    def test_roundtrip(self):
        with tmpdir() as d, mock.patch.object(base, "SNAPSHOT_DIR", Path(d)):
            snap = SourceResult("dummy", "e", Dummy.licence, "ok", "2026-11-02T00:00:00+00:00")
            p = base.write_snapshot(snap)
            self.assertEqual(SourceResult.from_dict(json.loads(p.read_text())), snap)
