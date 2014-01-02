#!/bin/bash

ARCHIVE="git-etc"
[ -d ${ARCHIVE} ] && rm -rf ${ARCHIVE}

mkdir -p ${ARCHIVE}/usr/{bin,lib/systemd/system,share/applications}
mkdir -p ${ARCHIVE}/usr/share/man/{man1,man5}
mkdir -p ${ARCHIVE}/ctrlconf
mkdir -p ${ARCHIVE}/etc

cp sources/git-etc ${ARCHIVE}/usr/bin/
cp sources/git-etc.service ${ARCHIVE}/usr/lib/systemd/system/
cp sources/git-etc.conf ${ARCHIVE}/etc/
cp sources/ctrlconf.sh ${ARCHIVE}/usr/bin/ctrlconf
cp sources/setup.py ${ARCHIVE}/
cp sources/ctrlconf.py ${ARCHIVE}/ctrlconf.py
cp sources/ctrlconf/*.py ${ARCHIVE}/ctrlconf/
cp sources/*.desktop ${ARCHIVE}/usr/share/applications/
cp sources/*.1 ${ARCHIVE}/usr/share/man/man1/
cp sources/*.5 ${ARCHIVE}/usr/share/man/man5/
cp install.sh ${ARCHIVE}/
cp {AUTHORS,COPYING} ${ARCHIVE}/

VERSION=$(grep Version sources/git-etc | awk '{printf $5;}')
tar -cf - ${ARCHIVE} | xz -9 -c - > ${ARCHIVE}-${VERSION}-src.tar.xz
rm -r ${ARCHIVE}

# update PKGBUILD
MD5SUMS=$(md5sum ${ARCHIVE}-${VERSION}-src.tar.xz | awk '{print $1}')
sed -i "s/md5sums=('[0-9a-f]\{32\}')/md5sums=('${MD5SUMS}')/" PKGBUILD
sed -i "s/pkgver=[0-9.]\{5\}/pkgver=${VERSION}/" PKGBUILD
