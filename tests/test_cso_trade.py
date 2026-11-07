import unittest

from corkathon.sources import base
from corkathon.sources.cso_trade import CsoTradeLoader

from .helpers import env, fixture, no_network


class CsoTradeTests(unittest.TestCase):
    def test_parse_fixture(self):
        recs, ref, pub = CsoTradeLoader().parse(fixture("cso_tsm06.json"))
        self.assertEqual(len(recs), 13)
        self.assertRegex(ref, r"^\d{4}-\d{2}$")
        self.assertTrue(pub)
        r = recs[-1]
        for k in ("reference_period", "published_at", "retrieved_at", "imports_value", "unit"):
            self.assertIn(k, r)
        self.assertEqual(r["unit"], "Euro Thousand")

    def test_committed_snapshot_loads_offline(self):
        with env(SNAPSHOT="1"), no_network():
            r = CsoTradeLoader().load()
        self.assertEqual(r.status, "snapshot")
        self.assertTrue(r.records)
        self.assertIn("CC BY 4.0", r.licence.name)

    def test_live_failure_never_raises(self):
        with no_network():
            r = CsoTradeLoader().load_live()
        self.assertEqual(r.status, "unavailable")
