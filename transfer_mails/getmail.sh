#!/usr/bin/env bash                                                                                                                                                     
hash_string()
{
  f_mbid=$1
  f_mbid_len=`expr length $f_mbid `
  #echo $f_mbid_len

  value=`echo $[$((num=0x238F13AF)) * $f_mbid_len]`

  for ((index=0; index<$f_mbid_len; index++));
  do
       index_temp=`echo ${f_mbid:index:1} `
       #echo "index_temp is $index_temp"

       acsii_temp=`printf "%d" "'$index_temp" `
       #echo "acsii_temp is $acsii_temp"

       value=`echo $[$((num=0x7FFFFFFF)) & ($value + (($acsii_temp) << ($index*5 % 24)) )] `
  done

  hashed_mbid=`echo $[(1103515243 * $value + 12345) & $((num=0x7FFFFFFF))]`

}

get_db_path()
{
  g_mbid=$1
  hash_string $g_mbid 
  #echo "hashed_mbid is $hashed_mbid"

  hash_dir1=`echo  $[$hashed_mbid % $HASH1] `
  hash_dir2=`echo  $[$hashed_mbid / $HASH1 % $HASH2]`
  mb_path="$hash_dir1/$hash_dir2"

  #echo "The mbid:$hashed_mbid   mailbox hashdir1/hashdir2 :$mb_path"
  #mb_db_path="$hash_dir1/$hash_dir2/$g_mbid/db"
  #echo $mb_db_path

}




FindDBPath()
{
  f_mbid=$1
  f_mailroot=$2
  MSSConfigPath=$3


  ### find mailroot dirname
  DBRootPathTemp=`cat $MSSConfigPath|grep "MailDir="|awk -F '=' '{print $2}'|awk -F';' '{print $1}' | awk -F' ' '{print $1}' `
  MBRootPath="$DBRootPathTemp/m"$f_mailroot"/MB2"

  get_db_path $f_mbid

  DBPath="$MBRootPath/$mb_path/$f_mbid/db"
  f_db=`echo $DBPath|cut -b 22-100`
  if [ -f $f_db ];then 
  	MailBoxResult=`(echo "$Mode"; echo " "$MailBoxInfo" " ; echo ".quit") |sqlite3 "$f_db"`  
  	echo $f_db"-----------"$MailBoxResult
  else
   	$f_db"-----------db is not exist"
  fi
}


###main
Mode=".mode line"

files=$1
mailroot=$2
mssini=$3

MailBoxInfo=" select count(*) as total_count ,count(*) - sum(seen) as unseen_count,sum(recent) as recent_count,\
              sum(mail_size) / 1024.0 / 1024.0 as occupied_size  from maillist  where folder_id !=6;"
FolderStatInfo="select count(*) as total_count ,count(*) - sum(seen) as unseen_count,sum(recent) as recent_count,\
                sum(mail_size) / 1024.0 / 1024.0 as occupied_size  from maillist  "

HASH1=100
HASH2=100
if [ "$files" != "" ] && [ $mailroot ] && [ $mssini ]
then
	if [ -f $files ]
	then
	cat $files | while read mbid
	do
    		FindDBPath $mbid $mailroot $mssini
	done
	else
		echo "file is not exists"
                echo  'eg   : ./getmbpath.sh 33127 0 ~/aimcpro/config/mss.ini'
	fi
else
	        echo  'please input right parameter. '
                echo  'usage: ./getmbpath.sh  file  mailroot mssinipath'
                echo  'eg   : ./getmbpath.sh mbid.txt 160 ~/aimcpro/config/mss.ini'
fi
