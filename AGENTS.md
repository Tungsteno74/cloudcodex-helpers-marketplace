# Contributor instructions

This repository is a GSM family marketplace and must remain catalog-only.
Do not copy plugin implementations, build artifacts, credentials, or account-specific
plugin IDs into this repository.

Each public marketplace entry must point to the canonical GitHub repository for one
plugin. Public entries are added only when the referenced plugin is intentionally
ready for public family distribution.

Private or experimental plugins belong in a separate private family marketplace;
do not expose them here merely for convenience.

Keep marketplace changes minimal and reviewable. Preserve existing plugin entries
unless a source is intentionally renamed, retired, or promoted according to the GSM
lifecycle. Run `python -X utf8 tools/validate.py` before committing.
