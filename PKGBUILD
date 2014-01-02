# Author: Evgeniy "arcanis" Alexeev <esalexeev@gmail.com>
# Maintainer: Evgeniy "arcanis" Alexeev <esalexeev@gmail.com>

pkgname=git-etc
pkgver=2.3.0
pkgrel=1
pkgdesc="Simple daemon for monitoring changes in files"
arch=('i686' 'x86_64')
url="https://github.com/arcan1s/git-etc"
license=("GPLv3")
depends=('bash' 'git')
makedeps=('python2')
optdepends=('python2-pyqt4: for GUI'
            'xterm: for GUI')
source=(https://github.com/arcan1s/git-etc/releases/download/V.${pkgver}/${pkgname}-${pkgver}-src.tar.xz)
md5sums=('200eadf734f7b8a25d77dda0322c1975')
backup=('etc/git-etc.conf')

package()
{
  "${srcdir}/${pkgname}/install.sh" "${pkgdir}"
}
