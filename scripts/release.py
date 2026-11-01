#!/usr/bin/env python3
"""Build and independently verify the deterministic v0.2.0 distribution ZIP.

Build from a clean committed checkout. No third-party Python packages required.
"""

import argparse
import hashlib
import json
import os
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME = 'super-mega-brainstorm-chatgpt-plugin-v0.2.0.zip'
REQUIRED = {
    'plugin.json', '.codex-plugin/plugin.json', 'README.md', 'docs/INSTALLATION.md',
    'LICENSES/README.md', 'LICENSES/ARTWORK-NOTICE.md',
    'LICENSES/MPL-2.0.txt', 'LICENSES/CC-BY-SA-4.0.txt',
    'skills/super-mega-brainstorm-skill/SKILL.md',
    'skills/super-mega-brainstorm-skill/tests/run_tests.sh',
    'scripts/release.py',
}
FORBIDDEN_PARTS = {'.git', '__pycache__', '.pytest_cache', '.mypy_cache', 'dist', 'tmp'}
FORBIDDEN_NAMES = {'.DS_Store', '.env', 'credentials.json'}


def tracked_files():
    result = subprocess.check_output(['git', '-C', str(ROOT), 'ls-files', '-z'])
    return sorted(p.decode() for p in result.split(b'\0') if p)


def safe_name(name):
    p = Path(name)
    return (not p.is_absolute() and '..' not in p.parts and
            not any(x in FORBIDDEN_PARTS for x in p.parts) and
            not any(x in FORBIDDEN_NAMES or x.startswith('.env.') for x in p.parts) and
            not name.endswith(('.pyc', '.pyo', '~')))


def build(destination):
    status = subprocess.check_output(['git', '-C', str(ROOT), 'status', '--porcelain']).decode()
    if status:
        raise SystemExit('Refusing to package an uncommitted checkout:\n' + status)
    files = tracked_files()
    if not REQUIRED <= set(files):
        raise SystemExit('Missing tracked release files: ' + repr(sorted(REQUIRED - set(files))))
    if not all(safe_name(name) for name in files):
        raise SystemExit('Tracked files include forbidden archive paths')
    destination = Path(destination).resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as out:
        for name in files:
            source = ROOT / name
            if not source.is_file() or source.is_symlink():
                raise SystemExit('Missing, non-file, or symlink: ' + name)
            info = zipfile.ZipInfo(name, (2020, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = ((0o755 if os.access(source, os.X_OK) else 0o644) << 16)
            out.writestr(info, source.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)
    print(destination)
    print('SHA-256', hashlib.sha256(destination.read_bytes()).hexdigest())


def verify(archive):
    archive = Path(archive).resolve()
    with zipfile.ZipFile(archive) as z:
        names = z.namelist()
        if len(names) != len(set(names)) or not REQUIRED <= set(names):
            raise SystemExit('Duplicate or missing required archive entries')
        if not all(safe_name(name) for name in names):
            raise SystemExit('Unsafe or unexpected development archive entry')
        if z.testzip() is not None:
            raise SystemExit('ZIP integrity failure')
        # The committed file inventory is the release allowlist.
        if set(names) != set(tracked_files()):
            raise SystemExit('Archive inventory differs from committed source')
        for name in names:
            if z.read(name) != (ROOT / name).read_bytes():
                raise SystemExit('Archive content differs from committed source: ' + name)
        with tempfile.TemporaryDirectory(prefix='smb-release-') as temp:
            z.extractall(temp)
            root = Path(temp)
            portable = json.loads((root / 'plugin.json').read_text())
            codex = json.loads((root / '.codex-plugin/plugin.json').read_text())
            assert portable['name'] == codex['name'] == 'super-mega-brainstorm'
            assert portable['version'] == codex['version'] == '0.2.0'
            assert (root / codex['skills']).is_dir()
            for key in ('composerIcon', 'logo'):
                assert (root / codex['interface'][key]).is_file()
            for size in (64, 128, 256, 512):
                name = f'assets/icons/super-mega-brainstorm-icon-{size}.png'
                data = (root / name).read_bytes()
                assert data[:8] == b'\x89PNG\r\n\x1a\n'
                assert int.from_bytes(data[16:20], 'big') == size
                assert int.from_bytes(data[20:24], 'big') == size
            skill = root / 'skills/super-mega-brainstorm-skill'
            subprocess.run(['python3', 'scripts/validate_package.py', '.', '--distribution'], cwd=skill, check=True)
            subprocess.run(['bash', 'tests/run_tests.sh'], cwd=skill, check=True)
    print('PASS extracted archive inventory, manifests, assets, and skill tests')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('build', 'verify'))
    parser.add_argument('archive', nargs='?', default=NAME)
    args = parser.parse_args()
    if args.command == 'build':
        build(args.archive)
    else:
        verify(args.archive)
