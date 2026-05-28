# keskos-release

`keskos-release` packages the release and branding metadata that identify a machine as KeskOS and expose the current layer, channel, build, accent, and project URLs to user-space tools.

## What this is

This repository builds the package that drops the canonical KeskOS branding metadata into `/etc` and `/usr/lib/keskos` so apps, scripts, installer helpers, and browser/startpage assets can read one shared source of truth.

## Role in KeskOS

Release metadata package.

## Package name

```txt
Package: keskos-release
Repo: [keskos]
Architecture: any
```

## What it installs or provides

- Installs `/etc/keskos-release`.
- Installs `/usr/lib/keskos/branding.json`.
- Installs `/usr/lib/keskos/branding.py` and `/usr/lib/keskos/branding.sh`.
- Installs compatibility metadata files `/usr/lib/keskos/version`, `/usr/lib/keskos/channel`, `/usr/lib/keskos/build-id`, and `/usr/lib/keskos/layer`.
- Does not install commands or services; it is a metadata package.

## Commands and launchers

- This package does not install standalone commands or GUI launchers.

## Config, logs, and state

- `/etc/keskos-release` is a pacman backup file and may be preserved across upgrades.
- `branding.json` is the packaged machine-readable copy of the same release identity and is intended for GUI/runtime consumers.
- No logs or systemd units are shipped by this package.

## Dependencies

- No runtime dependencies are declared.
- Build with `makepkg -s --noconfirm`.

## Build

```bash
makepkg -s --noconfirm
```

## Packaging notes

- This package is intentionally tiny and should remain easy for scripts to consume.
- Use it as the canonical place for distro release metadata rather than duplicating brand lines or layer strings elsewhere.
- Updating the layer branding should happen here first; other packages should read these files rather than hardcoding `Layer 4`, `Layer 5`, or old edition labels.

## Troubleshooting

- If a tool reports the wrong distro version or brand line, inspect `/etc/keskos-release` and `/usr/lib/keskos/branding.json` after reinstalling the package.

## Docs website export notes

- Docs site usage: distro identity metadata reference and file-format note.
