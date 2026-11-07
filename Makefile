.PHONY: test snapshot
PY ?= python3

test:
	PYTHONPATH=src $(PY) -m unittest discover -s tests -t . -v

snapshot:
	PYTHONPATH=src $(PY) -m corkathon.snapshot
