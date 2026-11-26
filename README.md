# HookInvariant

Validate idempotency and state transitions from webhook processing evidence.

**Status** Local proof of concept. See the [roadmap](ROADMAP.md) for product acceptance criteria and release status.

## Overview

Event-driven application teams need to prove that duplicate deliveries do not repeat side effects and invalid transitions do not mutate state.

## Quickstart

Requires Python 3.11 or later. Use a system Python installation. The core uses only its standard library and reads local files.


```sh
git clone https://github.com/Parsa-Emami/hook-invariant.git
cd hook-invariant
python3 check.py examples/pass.json
python3 check.py examples/finding.json
python3 -m unittest discover -s tests -v
```

The second command deliberately exits with status 1 and reports `duplicate_applied`.

- [CLI contract and examples](docs/cli.md)
- [Architecture](docs/architecture.md) and [threat model](docs/threat-model.md)
- [Project rules](RULES.md), [roadmap](ROADMAP.md), and [contributing](CONTRIBUTING.md)
- [Security reporting](SECURITY.md) and [license](LICENSE)
- [Published documentation](https://parsa-emami.github.io/hook-invariant/)
