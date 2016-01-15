#!/bin/bash

source ~/.bash_profile

if [ $# -ne 1 ]
then
	echo "usage: getsize.sh mailroot"
	echo "usage: getsize.sh 77"
	exit 1	
fi

mailroot=$1
cp ${mailroot}occpied.TXT ${mailroot}occpied.TXT.bak
>${mailroot}dbpath.txt
cat ${mailroot}occpied.TXT|while read line
do
	getmbpath.sh ${line} ${mailroot} ~/aimcpro/${mailroot}/config/mss.ini  >> ${mailroot}dbpath.txt
	#sleep 0.1
done
>${mailroot}dbpath.sql
cat ${mailroot}dbpath.txt|while read dd
do
	echo "sqlite3 ${dd} \"select mbid,sum(mail_size)/1024.0/1024.0 as occupied_size  from maillist;\"" >> ${mailroot}dbpath.sql
done
sh ${mailroot}dbpath.sql > ${mailroot}dbpath.res
cat ${mailroot}dbpath.res |grep "^[0-9]"|sort -t'|' -k2 -r -g > ${mailroot}occpied.TXT.bak2
cat ${mailroot}occpied.TXT.bak2|awk -F'|' '{print $1}' > ${mailroot}occpied.TXT
