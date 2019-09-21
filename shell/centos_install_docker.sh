#!/usr/bin/env bash
sudo yum remove -y docker \
              docker-client \
              docker-client-latest \
              docker-common \
              docker-latest \
              docker-latest-logrotate \
              docker-logrotate \
              docker-engine

sudo yum install -y yum-utils \
    device-mapper-persistent-data \
    lvm2

sudo yum-config-manager --add-repo \
    https://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
sudo yum makecache

# check docker's valiable version
# yum list docker-ce --showduplicates
sudo yum install docker-compose -y
sudo yum install docker-ce-... containerd.io -y
sudo systemctl enable docker