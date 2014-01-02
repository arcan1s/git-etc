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
md5sums=('53cce08a39ced4df2c2a6a8e8793a3f3')
backup=('etc/git-etc.conf')

package()
{
  "${srcdir}/${pkgname}/install.sh" "${pkgdir}"
}
