#!/bin/bash
#function:
# find every mbid  correspond mailsize
source ~/.bash_profile

if [ $# -ne 1 ]
then
	echo "usage: getsize.sh mailroot"
	echo "usage: getsize.sh 77"
	exit 1	
fi

mailroot=$1
cp ${mailroot}occpied.TXT ${mailroot}occpied.TXT.bak
while read mbid
do
        getmbpath.sh ${mbid} ${mailroot} ~/aimcpro/${mailroot}/config/mss.ini | \
        xargs -i sqlite3 {} "select mbid,sum(mail_size)/1024.0/1024.0 as occupied_size from maillist;"
done< ${mailroot}occpied.TXT | grep "^[0-9]" | sort -t'|' -k2  -r -g | uniq >${mailroot}occpied.TXT.bak2
awk -F'|' '{print $1}' ${mailroot}occpied.TXT.bak2 >${mailroot}occpied.TXT
