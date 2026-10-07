# CloudCodeX Helpers Marketplace

Public family marketplace for CloudCodeX helper plugins.

This repository follows the **GSM (GPT Structured Marketplace)** architecture:
the marketplace is the discovery boundary for one plugin family, while each plugin
has its own repository, versioning, CI, release process, and issue history.

## Plugins

- **CloudCodeX Windows Bootstrap** — Windows-only validation for Codex Cloud through
  GitHub Actions. Source: https://github.com/Tungsteno74/cloudcodex-windows-bootstrap

## Add the marketplace

```sh
codex plugin marketplace add Tungsteno74/cloudcodex-helpers-marketplace
```

Workspace administrators can import the repository URL directly and leave **Path**
empty. New entries are intentionally added only when a plugin is ready for public
family distribution.

## GSM boundary

This repository contains **catalog metadata only**. Plugin implementations are never
copied here. A marketplace entry points to the canonical Git repository for that
plugin.

Unpublished or private plugins belong in a separate private family marketplace.
When all private plugins in that staging catalog are promoted or abandoned, the
private marketplace can be archived and later removed if it has no remaining value.

See [GSM architecture](docs/GSM_ARCHITECTURE.md) for the canonical structure.

Licensed under [MIT](LICENSE).
