#!/bin/bash

mailroot=$1
total=0
count=0
total1=0
total_count=0

while read mbid
do

    if [[ $total1 -ge 300000 ]]; then
        break
    fi

    real_mailroot=`zwjgetuserinfo -M $mbid | awk -F ':' '/mailroot/{print $2}'`
    if [[ ${real_mailroot} -eq $mailroot ]]; then
        space=`grep "^${mbid}|" ${mailroot}occpied.TXT.bak2 | cut -d '|' -f 2`
        total=`echo "scale=3;(${space}+${total})/1" | bc -l`
        total1=`echo "$total" | cut -d '.' -f 1`
        count=$[$count + 1]
    fi
    total_count=$[${total_count}+1]

done < ${mailroot}occpied.TXT

total=`echo "scale=3;$total/1000" | bc -l`
echo "有效迁移总量: ${total}G, 在 m$mailroot 分区人数: $count , 总共截取数：${total_count}"
