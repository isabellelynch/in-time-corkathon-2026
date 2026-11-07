import json
import os
import tempfile
from pathlib import Path
from unittest import mock

FIX = Path(__file__).parent / "fixtures"


def fixture(name):
    return json.loads((FIX / name).read_text())


def no_network():
    """Patch urlopen so any accidental live call fails loudly-but-safely."""
    return mock.patch("urllib.request.urlopen", side_effect=OSError("network disabled in tests"))


def env(**kw):
    return mock.patch.dict(os.environ, kw)


def tmpdir():
    return tempfile.TemporaryDirectory()
