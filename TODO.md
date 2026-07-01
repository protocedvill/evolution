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
- [ ] Update the "Unreleased" section of CHANGELOG.md to add entries for `scripts/todo_stats.py` and its test suite `tests/test_todo_stats.py`, which were added in prior commits but are currently undocumented in the changelog
- [ ] Document `scripts/todo_stats.py` and its `--remaining`/`--percent` flags in the "Setup / usage" section of README.md, since the script currently isn't mentioned anywhere in the project docs
- [ ] Add unit tests for the `main()` CLI entry point in `scripts/todo_stats.py` (covering default output, `--remaining`, and `--percent`), since currently only the helper functions it calls are tested
- [ ] Add a `Makefile` (or `scripts/check.sh`) with a single `check`/`test` target that runs both `scripts/check_todo_format.sh` and the Python test suite, so contributors have one command to validate changes

