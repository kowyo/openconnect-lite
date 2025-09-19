# Repository Guidelines

openconnect-sso wraps OpenConnect with Azure AD SSO support. Follow these guidelines to keep contributions consistent, reviewable, and safe for downstream users.

## Project Structure & Module Organization
The core package lives in `openconnect_sso/`: `cli.py` wires the command-line entry point, authentication flows sit in `authenticator.py` and `saml_authenticator.py`, and `browser/` holds the PyQt WebEngine controller plus the injected `user.js`. Shared configuration helpers reside in `config.py` and `profile.py`, while `version.py` exposes the packaged version string. Tests live in `tests/` alongside common fixtures in `conftest.py`. Repository metadata and automation are defined in `pyproject.toml`, `Makefile`, and the uv-managed virtual environment under `.venv/`.

## Build, Test, and Development Commands
- `uv sync --extra dev`: create or refresh the development environment with dev dependencies.
- `make dev`: bootstrap `.venv` and sync dependencies via uv.
- `uv run pytest` or `make test`: execute the test suite inside the managed virtualenv.
- `make check`: convenience alias for running the pytest suite in CI-equivalent mode.
- `make dist`: build distributable artifacts with uv and copy the changelog.

## Coding Style & Naming Conventions
Target Python 3.8+ and match the existing module style: four-space indentation, snake_case for modules, functions, and variables, PascalCase for classes, and ALL_CAPS for module-level constants. Keep imports explicit within the package and follow the current logging patterns built on `structlog`. When editing JavaScript in `browser/user.js`, preserve the compact arrow-function style already in use.

## Testing Guidelines
Add coverage in `tests/` using pytest; name files and functions `test_<feature>.py` and `test_<behavior>` so auto-discovery succeeds. Leverage fixtures from `conftest.py` when exercising the browser and profile helpers, and isolate network interactions with the bundled HTTP server utilities. Run `uv run pytest --cov=openconnect_sso` (or `make check`) before opening a PR and include regression tests for new failure paths.

## Commit & Pull Request Guidelines
Write commit messages in short, imperative sentences (`git commit -m "streamline docs"`) to match the existing history. Squash noisy work-in-progress commits locally and keep the scope focused. Pull requests should link related issues, summarise user-visible changes, note manual testing steps, and include screenshots when UI surfaces change. Confirm `make check` (or `make test`) passes before requesting review.

## Security & Configuration Tips
Never commit contents of `.venv/`, user profiles, or files under `~/.config/openconnect-sso/`. Treat credentials captured by the keyring as sensitive and mock them in tests. When debugging authentication flows, redact tokens and tenant identifiers from logs and issue templates.
