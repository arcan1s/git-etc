git-etc
=======

Information
-----------
Simple daemon that automatically creates git repository in the given directory and creates commit at the specified time interval. To start deamon just run `systemctl start git-etc` as root.

License
-------
GPLv3

help message
------------
* git-etc:

        Usage: git-etc [ -c | --config /etc/git-etc.conf ] [ -h | --help ] [ -v | --version ]

        Parametrs:
            -c  --config      - path to configuration file
            -h  --help        - show this help and exit
            -v  --version     - show version and exit

        See "man 1 git-etc" for more details


* ctrlconf:

        Usage: ctrlconf [--default] [ -h | --help ] [ -v | --version ]

        Additional parametrs:
            --default     - create default configuration file
            -h  --help        - show this help and exit
            -v  --version     - show version and exit

            See "man 1 ctrlconf" for more details

Configuration
-------------
All settings are stored in `/etc/git-etc.conf`. After edit them you must restart daemon (`systemctl restart git-etc`).

See also
--------
    man 1 git-etc
    man 1 ctrlconf
    man 5 git-etc.conf

Instruction
===========

Dependencies
------------
* bash (sed, awk, etc)
* git
* systemd
* python2 (make)
* python2-pyqt4 (GUI)
* xterm (GUI)

Installation
------------
* download sources
* run `install.sh` from source directory:

        cd git-etc
        sudo ./install.sh "/path/to/root"
