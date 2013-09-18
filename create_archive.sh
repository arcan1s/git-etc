#!/bin/bash

if [ -d git-etc ]; then
  rm -rf git-etc
fi
mkdir git-etc

mkdir -p git-etc/usr/{bin,lib,share/applications}
mkdir -p git-etc/usr/lib/python2.7/site-packages/ctrlconf
mkdir -p git-etc/usr/lib/systemd/system
mkdir -p git-etc/usr/share/man/{man1,man5}
mkdir -p git-etc/etc/conf.d

cp sources/git-etc.service git-etc/usr/lib/systemd/system/
cp sources/git-etc.conf git-etc/etc/conf.d/
cp sources/ctrlconf.sh git-etc/usr/bin/ctrlconf
cp sources/ctrlconf.py git-etc/usr/lib/python2.7/site-packages/ctrlconf.py
cp sources/git-etc git-etc/usr/bin/
cp sources/*.1 git-etc/usr/share/man/man1/
cp sources/*.5 git-etc/usr/share/man/man5/
cp sources/*.desktop git-etc/usr/share/applications/
cp sources/ctrlconf/*.py* git-etc/usr/lib/python2.7/site-packages/ctrlconf/
cp install.sh git-etc/

cd git-etc
tar -cf - * | xz -9 -c - > ../git-etc-2.2.0.tar.xz
cd ..
rm -r git-etc
