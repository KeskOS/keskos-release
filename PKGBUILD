pkgname=keskos-release
pkgver=0.1.0
pkgrel=2
pkgdesc="KeskOS release metadata files"
arch=(any)
url="https://github.com/memegeko/keskos"
license=(custom:KeskOS)
backup=(etc/keskos-release)
source=()
sha256sums=()

package() {
  local name="${KESKOS_NAME:-KeskOS}"
  local layer="${KESKOS_LAYER:-4}"
  local layer_name="${KESKOS_LAYER_NAME:-Layer ${layer}}"
  local pretty_name="${KESKOS_PRETTY_NAME:-${name} // ${layer_name}}"
  local brand_line="${KESKOS_BRAND_LINE:-${pretty_name}}"
  local channel="${KESKOS_RELEASE_CHANNEL:-stable}"
  local build_id="${KESKOS_BUILD_ID:-dev}"
  local accent_color="${KESKOS_ACCENT_COLOR:-#ce6a35}"
  local home_url="${KESKOS_HOME_URL:-https://keskos.org}"
  local documentation_url="${KESKOS_DOCUMENTATION_URL:-https://docs.keskos.org}"
  local download_url="${KESKOS_DOWNLOAD_URL:-https://downloads.keskos.org}"
  local support_url="${KESKOS_SUPPORT_URL:-https://docs.keskos.org}"
  local bug_report_url="${KESKOS_BUG_REPORT_URL:-https://github.com/KeskOS}"
  local version="${KESKOS_RELEASE_VERSION:-${layer_name}}"

  install -d "${pkgdir}/etc" "${pkgdir}/usr/lib/keskos"

  cat >"${pkgdir}/etc/keskos-release" <<EOF
NAME="${name}"
PRETTY_NAME="${pretty_name}"
VERSION="${version}"
VERSION_ID="${layer}"
CHANNEL="${channel}"
ID=keskos
ID_LIKE=arch
BUILD_ID="${build_id}"
LAYER="${layer}"
LAYER_NAME="${layer_name}"
BRAND_LINE="${brand_line}"
ACCENT_COLOR="${accent_color}"
HOME_URL="${home_url}"
DOCUMENTATION_URL="${documentation_url}"
DOWNLOAD_URL="${download_url}"
SUPPORT_URL="${support_url}"
BUG_REPORT_URL="${bug_report_url}"
EOF

  cat >"${pkgdir}/usr/lib/keskos/branding.json" <<EOF
{
  "name": "${name}",
  "pretty_name": "${pretty_name}",
  "layer": "${layer}",
  "layer_name": "${layer_name}",
  "brand_line": "${brand_line}",
  "channel": "${channel}",
  "build_id": "${build_id}",
  "accent_color": "${accent_color}",
  "home_url": "${home_url}",
  "documentation_url": "${documentation_url}",
  "download_url": "${download_url}",
  "support_url": "${support_url}",
  "bug_report_url": "${bug_report_url}"
}
EOF

  install -m 755 "${startdir}/files/usr/lib/keskos/branding.py" "${pkgdir}/usr/lib/keskos/branding.py"
  install -m 755 "${startdir}/files/usr/lib/keskos/branding.sh" "${pkgdir}/usr/lib/keskos/branding.sh"

  printf '%s\n' "${layer_name}" >"${pkgdir}/usr/lib/keskos/version"
  printf '%s\n' "${channel}" >"${pkgdir}/usr/lib/keskos/channel"
  printf '%s\n' "${build_id}" >"${pkgdir}/usr/lib/keskos/build-id"
  printf '%s\n' "${layer}" >"${pkgdir}/usr/lib/keskos/layer"
}
