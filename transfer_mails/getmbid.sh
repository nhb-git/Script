#!/bin/bash

. ${HOME}/.bash_profile

if [ $# -ne 1 ]
  then
    echo "please input right parameter."
    echo "Usage: ./getmbid.sh <MBID>"
    echo "eg   : ./getmbid.sh 173"
    exit 0
fi

MBID=$1
cat ${MBID}mbid.txt|while read line
do
   MAILROOT=`~/aimcpro/tools/zwjgetuserinfo -M $line|grep mailroot|awk -F: '{print $2}'`
   if [ "$MAILROOT" == "$MBID" ]
   then
        echo $line >>${MBID}sucess.txt 
   else
       echo $line is ${MAILROOT} >>${MBID}error.txt
   fi
done
