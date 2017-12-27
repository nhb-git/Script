#!/bin/bash
#function:
#	start all tomcat
#setting java run environment 
#将脚本路径添加到rc.local后前面可加个命令：sleep 60，延迟60s再启动
export JAVA_HOME=/home/ocmp/jdk1.6.0_37

#start tomcats
/home/ocmp/icity/tomcat6_dashboard/bin/startup.sh
/home/ocmp/icity/tomcat6-fmc/bin/startup.sh
/home/ocmp/icity/tomcat6_selfservice/bin/startup.sh &
/home/ocmp/icity/tomcat6_mon/bin/startup.sh &
/home/ocmp/icity/tomcat6_lt/bin/startup.sh &
