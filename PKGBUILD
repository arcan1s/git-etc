# Author: Evgeniy "arcanis" Alexeev <esalexeev@gmail.com>
# Maintainer: Evgeniy "arcanis" Alexeev <esalexeev@gmail.com>

pkgname=git-etc
pkgver=2.2.1
pkgrel=1
pkgdesc="Simple daemon for monitoring changes in files"
arch=('x86_64')
url="https://github.com/arcan1s/git-etc"
license=("GPL")
depends=('bash' 'git')
optdepends=('python2-pyqt4: for GUI'
            'xterm: for GUI')
source=(https://github.com/arcan1s/git-etc/releases/download/V.${pkgver}/${pkgname}-${pkgver}.tar.xz)
md5sums=('32374e9285bc0cc330a4aea6932bbeb4')
backup=('etc/conf.d/git-etc.conf')

package()
{
  # daemon and gui
  install -D -m755 ${srcdir}/usr/bin/git-etc ${pkgdir}/usr/bin/git-etc || return 1
  install -D -m755 ${srcdir}/usr/bin/ctrlconf ${pkgdir}/usr/bin/ctrlconf || return 1
  install -D -m755 ${srcdir}/usr/lib/python2.7/site-packages/ctrlconf.py \
                   ${pkgdir}/usr/lib/python2.7/site-packages/ctrlconf.py || return 1
  mkdir -p ${pkgdir}/usr/lib/python2.7/site-packages/ctrlconf
  install -m644 -t ${pkgdir}/usr/lib/python2.7/site-packages/ctrlconf \
                ${srcdir}/usr/lib/python2.7/site-packages/ctrlconf/* || return 1
  install -D -m644 ${srcdir}/usr/share/applications/ctrlconf.desktop \
                   ${pkgdir}/usr/share/applications/ctrlconf.desktop || return 1
  
  # service
  install -D -m644 ${srcdir}/usr/lib/systemd/system/git-etc.service \
                   ${pkgdir}/usr/lib/systemd/system/git-etc.service || return 1
  install -D -m644 ${srcdir}/etc/conf.d/git-etc.conf \
                   ${pkgdir}/etc/conf.d/git-etc.conf || return 1
  
  # man pages
  install -D -m644 ${srcdir}/usr/share/man/man1/git-etc.1 \
                   ${pkgdir}/usr/share/man/man1/git-etc.1 || return 1
  install -D -m644 ${srcdir}/usr/share/man/man1/ctrlconf.1 \
                   ${pkgdir}/usr/share/man/man1/ctrlconf.1 || return 1
  install -D -m644 ${srcdir}/usr/share/man/man5/git-etc.conf.5 \
                   ${pkgdir}/usr/share/man/man5/git-etc.conf.5 || return 1
}
