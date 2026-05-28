from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path

RELEASE_PATH = Path("/etc/keskos-release")
BRANDING_JSON_PATH = Path("/usr/lib/keskos/branding.json")

DEFAULT_VALUES = {
    "name": "KeskOS",
    "pretty_name": "KeskOS",
    "layer": "",
    "layer_name": "",
    "brand_line": "KeskOS",
    "channel": "stable",
    "build_id": "dev",
    "accent_color": "#ce6a35",
    "home_url": "https://keskos.org",
    "documentation_url": "https://docs.keskos.org",
    "download_url": "https://downloads.keskos.org",
    "support_url": "https://docs.keskos.org",
    "bug_report_url": "https://github.com/KeskOS",
}

ENV_TO_FIELD = {
    "NAME": "name",
    "PRETTY_NAME": "pretty_name",
    "LAYER": "layer",
    "LAYER_NAME": "layer_name",
    "BRAND_LINE": "brand_line",
    "CHANNEL": "channel",
    "BUILD_ID": "build_id",
    "ACCENT_COLOR": "accent_color",
    "HOME_URL": "home_url",
    "DOCUMENTATION_URL": "documentation_url",
    "DOWNLOAD_URL": "download_url",
    "SUPPORT_URL": "support_url",
    "BUG_REPORT_URL": "bug_report_url",
}


@dataclass(frozen=True)
class Branding:
    name: str
    pretty_name: str
    layer: str
    layer_name: str
    brand_line: str
    channel: str
    build_id: str
    accent_color: str
    home_url: str
    documentation_url: str
    download_url: str
    support_url: str
    bug_report_url: str

    def as_env(self) -> dict[str, str]:
        return {
            "OS_NAME": self.name,
            "OS_PRETTY_NAME": self.pretty_name,
            "OS_LAYER": self.layer,
            "OS_LAYER_NAME": self.layer_name,
            "OS_BRAND_LINE": self.brand_line,
            "OS_CHANNEL": self.channel,
            "OS_BUILD_ID": self.build_id,
            "OS_ACCENT_COLOR": self.accent_color,
            "OS_HOME_URL": self.home_url,
            "OS_DOCUMENTATION_URL": self.documentation_url,
            "OS_DOWNLOAD_URL": self.download_url,
            "OS_SUPPORT_URL": self.support_url,
            "OS_BUG_REPORT_URL": self.bug_report_url,
        }

    def as_json(self) -> dict[str, str]:
        return asdict(self)


def _read_json(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}

    if not isinstance(payload, dict):
        return {}

    values: dict[str, str] = {}
    for key, value in payload.items():
        if isinstance(value, str):
            values[key] = value.strip()
    return values


def _read_key_value_file(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}

    values: dict[str, str] = {}
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return values

    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if value.startswith('"') and value.endswith('"') and len(value) >= 2:
            value = value[1:-1]
        field_name = ENV_TO_FIELD.get(key)
        if field_name:
            values[field_name] = value
    return values


def _normalize(values: dict[str, str]) -> dict[str, str]:
    normalized = dict(DEFAULT_VALUES)
    normalized.update({key: value for key, value in values.items() if value})

    if not normalized["layer_name"] and normalized["layer"]:
        normalized["layer_name"] = f"Layer {normalized['layer']}"

    if not normalized["pretty_name"]:
        normalized["pretty_name"] = normalized["brand_line"] or normalized["name"]

    if not normalized["brand_line"]:
        normalized["brand_line"] = normalized["pretty_name"] or normalized["name"]

    if not normalized["pretty_name"]:
        normalized["pretty_name"] = normalized["name"]

    return normalized


def load_branding() -> Branding:
    merged: dict[str, str] = {}
    merged.update(_read_json(BRANDING_JSON_PATH))
    merged.update(_read_key_value_file(RELEASE_PATH))
    normalized = _normalize(merged)
    return Branding(**normalized)


def write_branding_json(path: Path, branding: Branding) -> None:
    path.write_text(json.dumps(branding.as_json(), indent=2) + "\n", encoding="utf-8")


_branding = load_branding()

OS_NAME = _branding.name
OS_PRETTY_NAME = _branding.pretty_name
OS_LAYER = _branding.layer
OS_LAYER_NAME = _branding.layer_name
OS_BRAND_LINE = _branding.brand_line
OS_CHANNEL = _branding.channel
OS_BUILD_ID = _branding.build_id
OS_ACCENT_COLOR = _branding.accent_color
OS_HOME_URL = _branding.home_url
OS_DOCUMENTATION_URL = _branding.documentation_url
OS_DOWNLOAD_URL = _branding.download_url
OS_SUPPORT_URL = _branding.support_url
OS_BUG_REPORT_URL = _branding.bug_report_url
