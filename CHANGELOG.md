# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows the autonomous, TODO.md-driven workflow described in
[`CONTRIBUTING.md`](CONTRIBUTING.md) rather than a version-number release cycle,
so entries are grouped by date instead of by release.

## [Unreleased]

### Added

- `CHANGELOG.md` to track notable changes going forward.
- `CONTRIBUTING.md` explaining how to propose changes, including how the
  automated TODO.md-driven workflow operates.
- `LICENSE` file (MIT).
- `.gitignore` covering common OS, editor, and language tooling artifacts.
- Fleshed out `README.md` with a real project description, purpose, and
  setup/usage instructions.
- GitHub pull request template (`.github/PULL_REQUEST_TEMPLATE.md`) that
  reminds contributors to scope changes to a single `TODO.md` item.
- GitHub issue template (`.github/ISSUE_TEMPLATE/backlog_item.md`) for
  proposing a new `TODO.md` backlog item.
- `.editorconfig` to enforce consistent indentation, line endings, and
  trailing whitespace rules across editors.
- `scripts/check_todo_format.sh` to lint `TODO.md` and confirm every
  checklist line starts with `- [ ] ` or `- [x] `.
- `SECURITY.md` describing how to privately report a security issue.
- `scripts/todo_stats.py` to print `TODO.md` checklist completion stats,
  with `--remaining` and `--percent` flags.
- `tests/test_todo_stats.py` unit tests covering the helper functions in
  `scripts/todo_stats.py`.
- `Makefile` with a `check`/`test` target that runs
  `scripts/check_todo_format.sh` and the Python test suite in one command.

### Fixed

- `scripts/todo_stats.py` now catches a missing/unreadable `TODO.md` path
  and prints a clear message to stderr with exit code 1, instead of letting
  an unhandled traceback surface.
