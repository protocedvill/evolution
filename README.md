# evolution

`evolution` is a self-modifying sandbox repository. Instead of being built by hand,
it grows through a recurring, unattended automation run: each run picks the next
unchecked item off the backlog in [`TODO.md`](TODO.md), implements it as a small,
focused change, checks it off, and commits the result. Over time the repository's
history is a record of small, autonomous, incremental improvements.

## Purpose

This repo exists to explore what a codebase looks like when it is iterated on by
an autonomous agent over many short, independent sessions rather than a single
human-driven effort. Each iteration is intentionally scoped to one backlog item
so that changes stay small, reviewable, and easy to reason about in isolation.

## How it works

1. [`TODO.md`](TODO.md) holds a checklist of pending improvements ("Auto-iteration
   backlog").
2. On each scheduled run, an agent selects one unchecked (`- [ ]`) item, implements
   it, and marks it done (`- [x]`) in place.
3. The change is committed (and pushed, when configured) by the automation
   pipeline — the agent itself does not manage git state beyond editing files.

## Setup / usage

There is no build step or runtime dependency yet — the repository currently
contains only documentation and its own backlog. To work with it locally:

```bash
git clone git@github.com-evolution:protocedvill/evolution.git
cd evolution
```

To add a new task to the backlog, append a `- [ ]` line to `TODO.md`. The next
automated run will pick it up.

## Project docs

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — how to propose changes and how the
  automated TODO.md-driven workflow operates.
- [`LICENSE`](LICENSE) — the project's license.
- [`SECURITY.md`](SECURITY.md) — how to privately report a security issue.
