"""Verify and join the archive parts using Python 3 (standard library only)."""
from pathlib import Path
import hashlib
import json
import os


def main():
    folder = Path(__file__).resolve().parent
    manifest = json.loads((folder / 'parts_manifest.json').read_text(encoding='utf-8'))
    name = manifest['archive']
    if Path(name).name != name:
        raise ValueError('Invalid archive filename')
    target = folder / name
    temporary = folder / (name + '.assembling')
    if target.exists() or temporary.exists():
        raise FileExistsError('Output or temporary file already exists; no files overwritten.')
    expected_names = [p['name'] for p in manifest['parts']]
    if len(set(expected_names)) != len(expected_names):
        raise ValueError('Duplicate part names')
    for part in manifest['parts']:
        if Path(part['name']).name != part['name']:
            raise ValueError('Invalid part filename')
        if not (folder / part['name']).is_file():
            raise FileNotFoundError(part['name'])
    total = 0
    whole = hashlib.sha256()
    try:
        with temporary.open('xb') as output:
            for part in manifest['parts']:
                data = (folder / part['name']).read_bytes()
                if len(data) != part['bytes'] or hashlib.sha256(data).hexdigest() != part['sha256']:
                    raise ValueError('Part verification failed: ' + part['name'])
                output.write(data)
                whole.update(data)
                total += len(data)
                print('Verified:', part['name'])
        if total != manifest['bytes'] or whole.hexdigest() != manifest['sha256']:
            raise ValueError('Full archive verification failed')
        # Exclusive creation prevents replacing an existing archive.
        with target.open('xb') as output, temporary.open('rb') as source:
            while chunk := source.read(1024 * 1024):
                output.write(chunk)
        temporary.unlink()
    except Exception:
        if temporary.exists():
            temporary.unlink()
        raise
    print('Success:', target)
    print('SHA-256:', whole.hexdigest())
    print('Extract the resulting ZIP with your normal archive application.')


if __name__ == '__main__':
    main()
