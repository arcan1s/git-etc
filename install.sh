#!/bin/bash

func_error() {
  echo "Error installing"
  exit 1
}

[ -z "$1" ] && DESTDIR="/" || DESTDIR="$1"
[ -d "$DESTDIR" ] || mkdir -p "$DESTDIR" || func_error

cd "$(dirname "${BASH_SOURCE[0]}")"
# daemon and configuration
install -Dm755 "usr/bin/git-etc" "$DESTDIR/usr/bin/git-etc" || func_error
install -Dm755 "usr/bin/ctrlconf" "$DESTDIR/usr/bin/ctrlconf" || func_error
install -Dm644 "etc/git-etc.conf" "$DESTDIR/etc/git-etc.conf" || func_error
install -Dm644 "usr/share/applications/ctrlconf.desktop" "$DESTDIR/usr/share/applications/ctrlconf.desktop" || func_error
# python files
python2 setup.py install --root="$DESTDIR"
# service
install -Dm644 "usr/lib/systemd/system/git-etc.service" "$DESTDIR/usr/lib/systemd/system/git-etc.service"  || func_error
# man pages
install -Dm644 "usr/share/man/man1/git-etc.1" "$DESTDIR/usr/share/man/man1/git-etc.1" || func_error
install -Dm644 "usr/share/man/man1/ctrlconf.1" "$DESTDIR/usr/share/man/man1/ctrlconf.1" || func_error
install -Dm644 "usr/share/man/man5/git-etc.conf.5" "$DESTDIR/usr/share/man/man5/git-etc.conf.5" || func_error

exit 0
