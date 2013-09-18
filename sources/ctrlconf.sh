#!/bin/bash

func_help() {
  echo -e "GUI for git-etc daemon"
  echo -e "\nUsage: ctrlconf [--default] [ -h | --help ] [ -v | --version ]" 
  echo -e "\nAdditional parametrs:"
  echo -e "      --default     - create default configuration file"
  echo -e "  -h  --help        - show this help and exit"
  echo -e "  -v  --version     - show version and exit"
  echo -e "\nSee \"man 1 ctrlconf\" for more details"
  exit 1
}
func_ver() {
  echo -e "                    Control Config"
  echo -e "GUI for git-etc daemon to work with GIT repository"
  echo -e "Version : 2.1.2                      License : GPL"
  echo -e "                                        by arcanis"
  echo -e "                      E-mail : esalexeev@gmail.com"
  exit 1
}

until [ -z $1 ]; do
  if [ "$1" = "-h" ]; then
    func_help; fi
  if [ "$1" = "--help" ]; then
    func_help; fi
  if [ "$1" = "-v" ]; then
    func_ver; fi
  if [ "$1" = "--version" ]; then
    func_ver; fi
  if [ "$1" = "--default" ]; then
    if [ -f "~/.config/ctrlconf.conf" ]; then
      rm ~/.config/ctrlconf.conf; fi; fi
  shift
done

xterm -e "cd /usr/lib/python2.7/site-packages/ && ./ctrlconf.py"
