#!/bin/bash
#
#Basic Linux Enumeration Tool
#Author: Patrick Coleman
#
#Basic Checks
echo -e "\n########################################\n     \nBASICS\n\n########################################"
echo -e "\n# KERNEL INFORMATION\n"
uname -a
echo -e "\n# SESSION INFORMATION \n"
whoami
pwd
id
echo -e "\n# COMMAND HISTORY \n"
cat ~/.bash_history
echo -e "\n# SUDO PRIVS \n"
sudo -l
echo -e "\n########################################\n     \nINTERESTING FILES\n\n########################################\n"
while getopts d: flag
do
    case "${flag}" in
        d) goodfile=${OPTARG};;
    esac
done
ls -la $(cat $goodfile) | sed '/^$/d;/total/d;/\.$/d'
echo -e "\n########################################\n     \nSUID\n\n########################################\n"
find / -perm /u=s -type f 2>/dev/null | sort -f
echo -e "\n########################################\n     \nNETSTAT\n\n########################################\n"
netstat -lanput
echo -e "\n########################################\n     \nTODO\n\n########################################\n"
echo "crontab -e"
echo "find / -group <GROUP> 2>/dev/null"
echo 'export PATH=/tmp:$PATH; echo $PATH;'
echo "check doas.conf"