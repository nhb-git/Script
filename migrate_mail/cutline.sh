#!/bin/bash
#function:
#	计算出要迁移本分区邮件量为300G时所需在本分区的用户的mbid
mailroot=$1		#分区号
space_sum=0		#在本分区的用户邮件总和
count=0			#在$mailroot 分区的用户数目
max_space=0		#用户邮件大小总和的最大值
total=0			#截止到最大值时的所有用户数目

if [ $# -ne 1 ]
then
        echo "uasge: cutline.sh mailroot"
        echo "exp  : cutline.sh 77"
        exit 1
fi

#运行脚本时会删除原来存在的mbid.txt文件
if [ -f "$1mbid.txt" ];then
	rm $1mbid.txt
fi

while read mbid
do

    if [ ${max_space} -ge 300000 ]; then
        break
    fi

    real_mailroot=`zwjgetuserinfo -M $mbid | awk -F ':' '/mailroot/{print $2}'`
    if [ "${real_mailroot}" = "$mailroot" ]; then
        space=`grep "^${mbid}|" ${mailroot}occpied.TXT.bak2 | cut -d '|' -f 2`
        space_sum=`echo "scale=3;(${space}+${space_sum})/1" | bc -l`
        max_space=`echo "$space_sum" | cut -d '.' -f 1`
        count=$[$count + 1]
	echo "$mbid" >>${1}mbid.txt
    fi
    total=$[${total}+1]

done < ${mailroot}occpied.TXT
sed -i "1,${total}d" ${mailroot}occpied.TXT
space_sum=`echo "scale=3;${space_sum}/1000" | bc -l`
echo "有效迁移总量: ${space_sum}G, 在 m$mailroot 分区人数: $count , 总共截取数：${total}"
