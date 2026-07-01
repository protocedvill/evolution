# Contributing

`evolution` grows through a recurring, unattended automation run rather than
regular pull-request review, so contributing here mostly means shaping the
backlog it works from. See [`README.md`](README.md) for the full picture of
how the project works.

## Proposing a change

The primary way to propose a change is to add an item to the backlog in
[`TODO.md`](TODO.md):

1. Append a new line in the form `- [ ] <description of the change>`.
2. Keep the description small, focused, and self-contained — something a
   single automated run could implement end to end without further
   clarification.
3. Open a pull request with just that addition (or, if you have push access,
   commit it directly).

If you'd rather implement the change yourself, regular pull requests are
also welcome. Keep each PR scoped to one improvement, matching the size and
focus of the automated iterations already in the project's history.

## How the automated TODO.md-driven workflow operates

On each scheduled run, an agent:

1. Reads `TODO.md` and selects one unchecked (`- [ ]`) item.
2. Implements that item as a small, focused change, consistent with the
   existing style of the repository.
3. Marks the corresponding line done by changing `- [ ]` to `- [x]`, without
   editing any other line in `TODO.md`.
4. Leaves committing and pushing to the automation pipeline — the agent
   itself does not run `git commit` or `git push`.

Because each run only touches one backlog item, the commit history is a
record of small, independent, reviewable changes. If a queued item turns out
to be unclear, unsafe, or too large for a single run, the agent leaves
`TODO.md` untouched and explains why instead of guessing — so if you add an
item, keep it small and unambiguous enough to survive that check.

## Guidelines for changes

- Keep changes small and scoped to a single backlog item or issue.
- Match the existing style and conventions of the surrounding files.
- Don't modify CI/workflow files, secrets, `.env` files, or credentials as
  part of a backlog item unless the item explicitly calls for it.
- Update or add tests when the project has a test suite covering the area
  you're changing.

## Checking TODO.md formatting

Run [`scripts/check_todo_format.sh`](scripts/check_todo_format.sh) to confirm
every checklist line in `TODO.md` starts with `- [ ] ` or `- [x] `:

```bash
./scripts/check_todo_format.sh
```

It exits non-zero and prints the offending line(s) if any checklist entry is
malformed.
