#!/bin/bash
#function:
#	every day dump database data of icitydb1
host="172.30.36.119"
dumpmysql="/opt/mysql/bin/mysqldump"
time=`date +%Y``date +%m``date +%d``date +%H``date +%M`
dump_path=/home/ocmp/mysql_back
dump_file="$dump_path/icitydb1.$time.sql.gz"

#检测备份路径，如果不存在则创建
if [ ! -d "$dump_path" ];then
	mkdir -p $dump_path
fi

#将数据库icitydb1进行全备份
$dumpmysql -h$host -P39306 -uicityusr1 icitydb1 | gzip >$dump_file
#检测上一步备份的文件存在且大小不为0时删除上一天的备份文件
if [ -f "$dump_file" ] && [ `ls -l $dump_file | awk '{print $5}'` -gt 100 ];then
	cat $dump_path/filename.txt | xargs -i rm {}
fi
#将当天备份的文件名记录到filename.txt文件中
echo "$dump_file" >$dump_path/filename.txt
