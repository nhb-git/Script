#!/bin/bash

source ~/.bash_profile

if [ $# -ne 2 ]
then
	echo "uasge: cutline.sh lines mailroot"
	echo "exp  : cutline.sh 100  77"
	exit 1
fi
lines=$1
mailroot=$2

sed -n '1,'${lines}'p' ${mailroot}occpied.TXT > qianyi.list
mv qianyi.list ${mailroot}mbid.txt
sed -i 's/ //g' ${mailroot}mbid.txt
sed -e '1,'${lines}'d' ${mailroot}occpied.TXT > tmp
mv tmp ${mailroot}occpied.TXT
