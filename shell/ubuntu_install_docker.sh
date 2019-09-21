#!/usr/bin/env bash
sudo apt-get remove docker docker-engine docker-ce docker.io -y
# add image source
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common

##################################################################################
# add source's gpg secret
# curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# sudo apt-key fingerprint 0EBFCD88

# sudo add-apt-repository \
    # "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    # $(lsb_release -cs) \
    # stable"
##################################################################################
sudo echo "deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu $(lsb_release -cs) stable" \
    >> /etc/apt/sources.list
sudo apt-get update -y

# check docker's valiable version
# apt-cache madison docker-ce
sudo apt-get install docker-ce=... containerd.io -y
sudo apt-get install docker-compose -y

sudo systemctl enable docker