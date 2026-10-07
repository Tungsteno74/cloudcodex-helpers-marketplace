from __future__ import annotations

import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MARKETPLACE = ROOT / '.agents/plugins/marketplace.json'


def main() -> int:
    data = json.loads(MARKETPLACE.read_text(encoding='utf-8'))
    if data.get('name') != 'cloudcodex-helpers':
        raise ValueError('Unexpected marketplace identity.')
    if data.get('interface', {}).get('displayName') != 'CloudCodeX Helpers':
        raise ValueError('Unexpected marketplace display name.')

    plugins = data.get('plugins')
    if not isinstance(plugins, list) or not plugins:
        raise ValueError('Marketplace must contain at least one plugin.')

    names: set[str] = set()
    for entry in plugins:
        name = entry.get('name')
        if not isinstance(name, str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name):
            raise ValueError(f'Invalid plugin name: {name!r}')
        if name in names:
            raise ValueError(f'Duplicate plugin name: {name}')
        names.add(name)

        source = entry.get('source', {})
        source_kind = source.get('source')
        if source_kind not in {'url', 'git-subdir'}:
            raise ValueError(f'{name}: public GSM entries must use a Git-backed source.')
        url = source.get('url')
        if not isinstance(url, str) or not url.startswith('https://github.com/'):
            raise ValueError(f'{name}: source must be a github.com HTTPS URL.')
        if source_kind == 'git-subdir':
            path = source.get('path')
            if not isinstance(path, str) or not path.startswith('./'):
                raise ValueError(f'{name}: git-subdir path must start with ./')

        policy = entry.get('policy')
        if policy != {'installation': 'AVAILABLE', 'authentication': 'ON_INSTALL'}:
            raise ValueError(f'{name}: unexpected public installation policy.')
        if not entry.get('category'):
            raise ValueError(f'{name}: category is required.')

    if (ROOT / 'plugins').exists():
        raise ValueError('GSM marketplace repositories must not embed plugin implementations.')
    if list(ROOT.glob('plugin.json')) or list(ROOT.glob('.codex-plugin/plugin.json')):
        raise ValueError('Marketplace repository must not masquerade as a plugin package.')

    print(f'validated {len(plugins)} public plugin entry/entries')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
