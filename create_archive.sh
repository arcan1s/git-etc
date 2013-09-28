#!/bin/bash

if [ -d git-etc ]; then
  rm -rf git-etc
fi
mkdir git-etc

mkdir -p git-etc/usr/{bin,lib,share/applications}
mkdir -p git-etc/ctrlconf
mkdir -p git-etc/usr/lib/systemd/system
mkdir -p git-etc/usr/share/man/{man1,man5}
mkdir -p git-etc/etc/conf.d

cp sources/git-etc git-etc/usr/bin/
cp sources/git-etc.service git-etc/usr/lib/systemd/system/
cp sources/git-etc.conf git-etc/etc/conf.d/
cp sources/ctrlconf.sh git-etc/usr/bin/ctrlconf
cp sources/setup.py git-etc/
cp sources/ctrlconf.py git-etc/ctrlconf.py
cp sources/ctrlconf/*.py git-etc/ctrlconf/
cp sources/*.desktop git-etc/usr/share/applications/
cp sources/*.1 git-etc/usr/share/man/man1/
cp sources/*.5 git-etc/usr/share/man/man5/
cp install.sh git-etc/

cd git-etc
tar -cf - * | xz -9 -c - > ../git-etc-2.2.2.tar.xz
cd ..
rm -r git-etc
