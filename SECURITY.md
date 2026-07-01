# Security Policy

## Reporting a vulnerability

If you believe you've found a security vulnerability in this repository,
please report it privately rather than opening a public issue or pull
request.

The preferred way to report a vulnerability is through
[GitHub's private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability):

1. Go to the repository's **Security** tab.
2. Select **Report a vulnerability**.
3. Fill in as much detail as you can, including steps to reproduce and the
   potential impact.

This opens a private conversation with the maintainer that isn't visible to
the public until it's resolved.

## What to expect

This project is maintained as an unattended, automated sandbox (see
[`README.md`](README.md)), so response times aren't guaranteed. Reports will
still be reviewed and, where applicable, addressed via a normal backlog item
in [`TODO.md`](TODO.md) once triaged.

## Scope

Given the nature of this repository (a self-modifying documentation/backlog
sandbox with no runtime dependencies at this time), most reports will
concern the repository's tooling (e.g. `scripts/`) or its GitHub
configuration rather than application code. Please still report anything
that looks like a genuine security issue.
