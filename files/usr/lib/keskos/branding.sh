#!/usr/bin/env bash

keskos_load_branding() {
  OS_NAME="KeskOS"
  OS_PRETTY_NAME="KeskOS"
  OS_LAYER=""
  OS_LAYER_NAME=""
  OS_BRAND_LINE="KeskOS"
  OS_CHANNEL="stable"
  OS_BUILD_ID="dev"
  OS_ACCENT_COLOR="#ce6a35"
  OS_HOME_URL="https://keskos.org"
  OS_DOCUMENTATION_URL="https://docs.keskos.org"
  OS_DOWNLOAD_URL="https://downloads.keskos.org"
  OS_SUPPORT_URL="https://docs.keskos.org"
  OS_BUG_REPORT_URL="https://github.com/KeskOS"

  if [[ -r /usr/lib/keskos/branding.json ]]; then
    local python_bin=""

    if command -v python3 >/dev/null 2>&1; then
      python_bin="python3"
    elif command -v python >/dev/null 2>&1; then
      python_bin="python"
    fi

    if [[ -n "${python_bin}" ]]; then
      # shellcheck disable=SC2046
      eval "$("${python_bin}" - <<'PY'
import json
import pathlib
import shlex

path = pathlib.Path("/usr/lib/keskos/branding.json")
if not path.is_file():
    raise SystemExit(0)

try:
    payload = json.loads(path.read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError):
    raise SystemExit(0)

mapping = {
    "name": "OS_NAME",
    "pretty_name": "OS_PRETTY_NAME",
    "layer": "OS_LAYER",
    "layer_name": "OS_LAYER_NAME",
    "brand_line": "OS_BRAND_LINE",
    "channel": "OS_CHANNEL",
    "build_id": "OS_BUILD_ID",
    "accent_color": "OS_ACCENT_COLOR",
    "home_url": "OS_HOME_URL",
    "documentation_url": "OS_DOCUMENTATION_URL",
    "download_url": "OS_DOWNLOAD_URL",
    "support_url": "OS_SUPPORT_URL",
    "bug_report_url": "OS_BUG_REPORT_URL",
}

for json_key, shell_key in mapping.items():
    value = payload.get(json_key)
    if isinstance(value, str) and value.strip():
        print(f"{shell_key}={shlex.quote(value.strip())}")
PY
)"
    fi
  fi

  if [[ -r /etc/keskos-release ]]; then
    # shellcheck disable=SC1091
    . /etc/keskos-release

    [[ -n "${NAME:-}" ]] && OS_NAME="${NAME}"
    [[ -n "${PRETTY_NAME:-}" ]] && OS_PRETTY_NAME="${PRETTY_NAME}"
    [[ -n "${LAYER:-}" ]] && OS_LAYER="${LAYER}"
    [[ -n "${LAYER_NAME:-}" ]] && OS_LAYER_NAME="${LAYER_NAME}"
    [[ -n "${BRAND_LINE:-}" ]] && OS_BRAND_LINE="${BRAND_LINE}"
    [[ -n "${CHANNEL:-}" ]] && OS_CHANNEL="${CHANNEL}"
    [[ -n "${BUILD_ID:-}" ]] && OS_BUILD_ID="${BUILD_ID}"
    [[ -n "${ACCENT_COLOR:-}" ]] && OS_ACCENT_COLOR="${ACCENT_COLOR}"
    [[ -n "${HOME_URL:-}" ]] && OS_HOME_URL="${HOME_URL}"
    [[ -n "${DOCUMENTATION_URL:-}" ]] && OS_DOCUMENTATION_URL="${DOCUMENTATION_URL}"
    [[ -n "${DOWNLOAD_URL:-}" ]] && OS_DOWNLOAD_URL="${DOWNLOAD_URL}"
    [[ -n "${SUPPORT_URL:-}" ]] && OS_SUPPORT_URL="${SUPPORT_URL}"
    [[ -n "${BUG_REPORT_URL:-}" ]] && OS_BUG_REPORT_URL="${BUG_REPORT_URL}"
  fi

  if [[ -z "${OS_LAYER_NAME}" && -n "${OS_LAYER}" ]]; then
    OS_LAYER_NAME="Layer ${OS_LAYER}"
  fi

  if [[ -z "${OS_PRETTY_NAME}" ]]; then
    OS_PRETTY_NAME="${OS_BRAND_LINE:-${OS_NAME}}"
  fi

  if [[ -z "${OS_BRAND_LINE}" ]]; then
    OS_BRAND_LINE="${OS_PRETTY_NAME:-${OS_NAME}}"
  fi

  export OS_NAME
  export OS_PRETTY_NAME
  export OS_LAYER
  export OS_LAYER_NAME
  export OS_BRAND_LINE
  export OS_CHANNEL
  export OS_BUILD_ID
  export OS_ACCENT_COLOR
  export OS_HOME_URL
  export OS_DOCUMENTATION_URL
  export OS_DOWNLOAD_URL
  export OS_SUPPORT_URL
  export OS_BUG_REPORT_URL
}

keskos_load_branding
