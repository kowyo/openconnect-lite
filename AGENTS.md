# Project Instructions

openconnect-sso wraps OpenConnect with Azure AD SSO support. Follow these guidelines to keep contributions consistent, reviewable, and safe for downstream users.

## Dev environment tips

- Use `make dev` to install development dependencies.
- Run `uv add <package_name>` if you need to add a Python package to the workspace so the virtual environment can see it.

## Testing instructions

- Use `uv run <file_name>` to run a Python script in the virtual environment.
- Use `make test` to run the test suite.

## Coding guidelines

- Always use context7 when I need code generation, setup or configuration steps, or library/API documentation. This means you should automatically use the Context7 MCP tools to resolve library id and get library docs without me having to explicitly ask.

