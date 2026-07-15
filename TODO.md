# Auto-iteration backlog
Do not implement todo entries which use any of the following forbidden paths.
forbidden_paths:
  - ".git/**"
  - ".env*"
  - "**/*.pem"
  - "**/id_rsa*"
  - ".github/workflows/**"
  - "**/secrets/**"
## The goal is to produce tools which would be useful to a user. Consider that when brainstorming new items in the todo list.
- [x] Flesh out README.md with a real project description, purpose, and setup/usage instructions (currently only contains the title "# evolution")
- [x] Add a .gitignore file covering common OS, editor, and language tooling artifacts (.DS_Store, node_modules/, __pycache__/, .env, etc.)
- [x] Add a LICENSE file since the project currently has none
- [x] Add a CONTRIBUTING.md explaining how to propose changes, including how the automated TODO.md-driven workflow operates
- [x] Add a CHANGELOG.md to track notable changes going forward
- [x] Add a GitHub pull request template (`.github/PULL_REQUEST_TEMPLATE.md`) that reminds contributors to scope changes to a single TODO.md item, per the guidelines in CONTRIBUTING.md
- [x] Add a GitHub issue template (`.github/ISSUE_TEMPLATE/backlog_item.md`) for proposing a new TODO.md backlog item, matching the format described in CONTRIBUTING.md
- [x] Add a `.editorconfig` file to enforce consistent indentation, line endings, and trailing whitespace rules across editors for future source files
- [x] Add a small shell script (e.g. `scripts/check_todo_format.sh`) that lints TODO.md to confirm every checklist line starts with `- [ ] ` or `- [x] `, and document it in CONTRIBUTING.md
- [x] Add a SECURITY.md describing how to privately report a security issue, since the repo has no such policy yet
- [x] Update the "Unreleased" section of CHANGELOG.md to include entries for the PR template, issue template, .editorconfig, TODO.md format-checking script, and SECURITY.md, which were added after the changelog was first created and are currently missing from it
- [x] Start adding some code.
- [x] Add some more code.
- [x] And some more code.
- [x] Add a "Project docs" section to README.md linking to CONTRIBUTING.md, LICENSE, and SECURITY.md, none of which are currently referenced anywhere in README.md
- [x] Update the "Unreleased" section of CHANGELOG.md to add entries for `scripts/todo_stats.py` and its test suite `tests/test_todo_stats.py`, which were added in prior commits but are currently undocumented in the changelog
- [x] Document `scripts/todo_stats.py` and its `--remaining`/`--percent` flags in the "Setup / usage" section of README.md, since the script currently isn't mentioned anywhere in the project docs
- [x] Add unit tests for the `main()` CLI entry point in `scripts/todo_stats.py` (covering default output, `--remaining`, and `--percent`), since currently only the helper functions it calls are tested
- [x] Add a `Makefile` (or `scripts/check.sh`) with a single `check`/`test` target that runs both `scripts/check_todo_format.sh` and the Python test suite, so contributors have one command to validate changes
- [x] Add graceful error handling in `scripts/todo_stats.py` for a missing/unreadable TODO.md path (catch the `FileNotFoundError` and print a clear message to stderr with exit code 1), instead of letting an unhandled traceback surface
- [x] Add automated tests for `scripts/check_todo_format.sh` (e.g. `tests/test_check_todo_format.py` invoking it via `subprocess` on a temp file), covering both a well-formed checklist (exit 0) and a malformed checklist line (non-zero exit plus the error message), since the script currently has no test coverage
- [x] Add `--help`/`-h` usage output to `scripts/todo_stats.py` (e.g. via `argparse`), since running it with `-h` today silently falls through to the default output instead of describing the `--remaining`/`--percent` flags
- [x] Update the example `scripts/todo_stats.py` output shown in README.md's "Setup / usage" section, since it shows stale counts (`16/19 tasks done`) that no longer match the current TODO.md checklist totals
- [x] Add type hints to the functions in `scripts/todo_stats.py` (`count_checklist_items`, `remaining_items`, `percent_complete`, `main`) to improve readability, since they currently rely solely on docstrings to describe argument and return types
- [x] Update the "Unreleased" section of CHANGELOG.md to add entries for `tests/test_check_todo_format.py`, the `--help`/`-h` flag in `scripts/todo_stats.py`, the README example-output fix, and the new type hints in `scripts/todo_stats.py`, which were added in prior commits but are currently missing from the changelog
- [x] Add an optional path argument to `scripts/check_todo_format.sh` (defaulting to `TODO.md` at the repo root, mirroring `scripts/todo_stats.py`'s `path` argument), so `tests/test_check_todo_format.py` can pass a temp file directly instead of copying the script into a temp `scripts/` directory to exercise its relative path resolution
- [x] Add a test in `tests/test_todo_stats.py` covering `main()`'s default path resolution (invoking it with no path argument from the repo root and asserting it reads the real `TODO.md`), since only the explicit-path case is currently covered
- [x] Add a `--version` flag to `scripts/todo_stats.py` that prints a version string, and document it alongside `--remaining`/`--percent` in README.md
- [x] Add a `make clean` target to the `Makefile` that removes `__pycache__/` and `.pytest_cache/` directories, since contributors currently have no single command to clear these local build artifacts
- [ ] Update the "Unreleased" section of CHANGELOG.md to add entries for the `--version` flag in `scripts/todo_stats.py`, the `make clean` Makefile target, the optional path argument to `scripts/check_todo_format.sh`, and the new default-path test in `tests/test_todo_stats.py`, all of which were added in prior commits but are currently missing from the changelog
- [ ] Fix `scripts/check_todo_format.sh` so it also checks the last line of the checklist file when that file doesn't end with a trailing newline (bash's `while read` loop currently skips an unterminated final line, silently letting a malformed last line pass), and add a regression test for this case
- [ ] Add a test in `tests/test_check_todo_format.py` covering `scripts/check_todo_format.sh`'s default path argument (invoking it with no argument from the repo root and asserting it reads the real `TODO.md`), mirroring the equivalent default-path test already added for `todo_stats.py`'s `main()`
- [ ] Add a return type hint (`-> argparse.ArgumentParser`) to `build_parser()` in `scripts/todo_stats.py`, since every other function in the module now has type hints except this one
- [ ] Add a `--count`/`--total` flag to `scripts/todo_stats.py` that prints just the total number of checklist items (done + pending), useful for scripting against the backlog size without parsing the default human-readable output

