#!/bin/bash
#     git-etc simple daemon written on BASH for monitoring changes in files
#     Copyright (C) 2013 Evgeniy Alekseev
#
#     This program is free software; you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation; either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program; if not, see http://www.gnu.org/licenses
#     or write to the Free Software Foundation,Inc., 51 Franklin Street,
#     Fifth Floor, Boston, MA 02110-1301  USA

# functions
error_mes() {
  case "$1" in
    "flag"      ) echo "[EE] Unknown flag";;
  esac
  exit 1
}
func_help() {
  echo -e "GUI for git-etc daemon"
  echo -e "\nUsage: ctrlconf [--default] [ -h | --help ] [ -v | --version ]"
  echo -e "\nAdditional parametrs:"
  echo -e "      --default     - create default configuration file"
  echo -e "  -h  --help        - show this help and exit"
  echo -e "  -v  --version     - show version and exit"
  echo -e "\nSee \"man 1 ctrlconf\" for more details"
  exit 0
}
func_ver() {
  echo -e "                    Control Config"
  echo -e "GUI for git-etc daemon to work with GIT repository"
  echo -e "Version : 2.3.1                    License : GPLv3"
  echo -e "                                        by arcanis"
  echo -e "                      E-mail : esalexeev@gmail.com"
  exit 0
}

# parametrs parsing
until [ -z $1 ]; do
  case "$1" in
    "-h" | "--help"    ) func_help;;
    "-v" | "--version" ) func_ver;;
    "--default"        ) [ -f "${HOME}/.config/ctrlconf.conf" ] && rm "${HOME}/.config/ctrlconf.conf";;
    *                  ) error_mes "flag";;
  esac
  shift
done

xterm -e "python2 /usr/lib/python2.7/site-packages/ctrlconf.py"
