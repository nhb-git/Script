#!/bin/bash

source /etc/profile
home_dir=/home/nhb

if [ $(whoami) != 'root' ]
then
	echo "please use sudo install!!!"
	exit
fi

# install basic packages
apt-get install ansible python3 python3-pip wget vim npm gcc make perl gdebi ssh-askpass bpython -y
apt-get install ansible python3 python3-pip wget vim npm gcc gcc-c++ openssl-devel make perl -y

# modify pip resource and update pip3
mkdir -p ~/.pip
echo "[global]" >> ~/.pip/pip.conf
echo "trusted-host = pypi.douban.com" >> ~/.pip/pip.conf
echo "index-url = https://pypi.douban.com/simple" >> ~/.pip/pip.conf

su - nhb -c "mkdir -p ~/.pip"
su - nhb -c 'echo "[global]" >> ~/.pip/pip.conf'
su - nhb -c 'echo "trusted-host = pypi.douban.com" >> ~/.pip/pip.conf'
su - nhb -c 'echo "index-url = https://pypi.douban.com/simple" >> ~/.pip/pip.conf'
pip3 install --upgrade pip
apt-get update && apt-get dist-upgrade

# install monaco font
cd /home/nhb/Downloads
git clone https://github.com/cstrap/monaco-font
cd  monaco-font
./install-font-ubuntu.sh https://github.com/todylu/monaco.ttf/blob/master/monaco.ttf?raw=true

# install shadowsocks-clint
mkdir -p  $home_dir/vpn && cd $home_dir/vpn
wget https://github.com/shadowsocks/shadowsocks-qt5/releases/download/v3.0.0/Shadowsocks-Qt5-3.0.0-x86_64.AppImage
chmod a+x Shadowsocks-Qt5-3.0.0-x86_64.AppImage

# git setting
git config --global user.email "niuhaibao@gmail.com"
git config --global user.name "nhb"

# install python3's django depend packages
pip3 install django==1.11 pylint-django pylint autopep8
pip3 install virtualenv virtualenvwrapper

# add virtualenv variable to $home_dir/.bashrc
su - nhb -c "mkdir -p $home_dir/niuhaibao/github"
su - nhb -c "mkdir -p $home_dir/niuhaibao/Django_Projects"
echo "export WORKON_HOME=$home_dir/.virtualenvs" >> $home_dir/.bashrc
echo "export PROJECT_HOME=$home_dir/niuhaibao/Django_Projects" >> $home_dir/.bashrc
echo "export VIRTUALENVWRAPPER_PYTHON=python3" >> $home_dir/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> $home_dir/.bashrc
echo "alias mygit='cd $home_dir/niuhaibao/github'" >> $home_dir/.bashrc
source $home_dir/.bashrc
chown -R nhb.nhb $home_dir/.virtualenvs

# npm install bootstrap, vue, jquery
su - nhb -c "npm config set registry https://registry.npm.taobao.org"
su - nhb -c "cd $home_dir/niuhaibao/Django_Projects ; npm install bootstrap vue vue-route jquery"
