SHELL := /bin/sh
.DEFAULT_GOAL := help

ARGS ?=

.PHONY: help install dev test lint format check build clean run lock

help:
	@printf "Targets:\n"
	@printf "  dev     Install project with dev tooling\n"
	@printf "  install Sync project dependencies\n"
	@printf "  test    Run the pytest suite\n"
	@printf "  lint    Run static analysis\n"
	@printf "  format  Apply formatting fixes\n"
	@printf "  check   Run lint and tests\n"
	@printf "  build   Build distributable artifacts\n"
	@printf "  run     Execute openconnect-sso (pass ARGS=...)\n"
	@printf "  lock    Refresh uv.lock\n"
	@printf "  clean   Remove build caches\n"

install:
	uv sync

dev:
	uv sync --group dev --group lint

test:
	uv run pytest $(ARGS)

lint:
	uv run ruff check . $(ARGS)

format:
	uv run ruff format . $(ARGS)

check: lint test

build:
	uv build

run:
	uv run openconnect-sso $(ARGS)

lock:
	uv lock

clean:
	rm -rf build dist htmlcov .pytest_cache .ruff_cache .coverage coverage.xml
	find openconnect_sso tests -name "__pycache__" -type d -prune -exec rm -rf {} +
