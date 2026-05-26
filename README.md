# keskos-release

KeskOS release metadata files

This repository contains the standalone Arch package source for `keskos-release`.

## Contents

- `PKGBUILD`
- `files/` for packaged assets, scripts, themes, or source snapshots where needed

## Build

```bash
makepkg -s --noconfirm
```

## Package Metadata

- Version: `0.1.0`
- Architectures: `any`

This repo is intended to be consumed by the KeskOS package build server and can also be built locally with standard Arch tooling.
