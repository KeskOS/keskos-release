# keskos-release

`keskos-release` packages the release metadata files that identify a machine as KeskOS and expose build/channel details to user-space tools.

## What this is

This repository builds the package that drops simple release-identification files into `/etc` and `/usr/lib/keskos` so apps and scripts can query distro version, channel, and build metadata.

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
- Installs `/usr/lib/keskos/version`, `/usr/lib/keskos/channel`, and `/usr/lib/keskos/build-id`.
- Does not install commands or services; it is a metadata package.

## Commands and launchers

- This package does not install standalone commands or GUI launchers.

## Config, logs, and state

- `/etc/keskos-release` is a pacman backup file and may be preserved across upgrades.
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
- Use it as the canonical place for distro release metadata rather than duplicating version files elsewhere.

## Troubleshooting

- If a tool reports the wrong distro version, inspect `/etc/keskos-release` and `/usr/lib/keskos/*` after reinstalling the package.

## Docs website export notes

- Docs site usage: distro identity metadata reference and file-format note.
