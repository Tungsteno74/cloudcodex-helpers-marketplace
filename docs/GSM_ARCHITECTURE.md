# GSM Architecture

**GSM — GPT Structured Marketplace** is the canonical repository organization used
for CloudCodeX plugin families.

## Structure

```text
Family public marketplace
    -> references public plugin repository A
    -> references public plugin repository B
    -> references public plugin repository C

Optional family private marketplace
    -> references private/unpublished plugin repositories

Each plugin repository
    -> owns source
    -> owns semantic versioning
    -> owns tests and CI
    -> owns release artifacts
    -> owns plugin-specific issues and history
```

## Principles

1. **Family is the discovery boundary.** A marketplace groups semantically related
   plugins and is not a monorepo for their implementations.
2. **Plugin is the lifecycle boundary.** Every plugin can be cloned, developed,
   versioned, validated, released, and retired independently.
3. **Visibility is a distribution state.** Public marketplaces list only plugins
   intentionally ready for public family distribution.
4. **Private staging is separate.** Private or experimental plugins use a private
   family marketplace rather than leaking into the public catalog.
5. **Promotion avoids duplication.** A plugin moves from private staging to the
   public family marketplace while keeping its canonical source repository.
6. **Catalogs reference sources.** Marketplace repositories contain metadata and
   documentation, not copied plugin implementations.

## Private marketplace lifecycle

Preferred lifecycle:

```text
ACTIVE -> ARCHIVE -> DELETE
```

Archive a private marketplace when it no longer has active private plugins. Delete
it only when its historical context and references are no longer useful.

## Current family

Public marketplace: `Tungsteno74/cloudcodex-helpers-marketplace`

Current plugin repositories:

- `Tungsteno74/cloudcodex-windows-bootstrap`

Proposed experimental plugin (catalog PR; do not merge until live capabilities
are reviewed for public family distribution):

- `Tungsteno74/cloudcodex-environment-discovery`
