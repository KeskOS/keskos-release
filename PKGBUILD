pkgname=keskos-release
pkgver=0.1.0
pkgrel=1
pkgdesc="KeskOS release metadata files"
arch=(any)
url="https://github.com/memegeko/keskos"
license=(custom:KeskOS)
backup=(etc/keskos-release)
source=()
sha256sums=()

package() {
  local version="${KESKOS_RELEASE_VERSION:-0.1}"
  local channel="${KESKOS_RELEASE_CHANNEL:-stable}"
  local build_id="${KESKOS_BUILD_ID:-dev}"

  install -d "${pkgdir}/etc" "${pkgdir}/usr/lib/keskos"

  cat >"${pkgdir}/etc/keskos-release" <<EOF
NAME="KeskOS"
VERSION="${version}"
CHANNEL="${channel}"
ID=keskos
ID_LIKE=arch
BUILD_ID="${build_id}"
EOF

  printf '%s\n' "${version}" >"${pkgdir}/usr/lib/keskos/version"
  printf '%s\n' "${channel}" >"${pkgdir}/usr/lib/keskos/channel"
  printf '%s\n' "${build_id}" >"${pkgdir}/usr/lib/keskos/build-id"
}
