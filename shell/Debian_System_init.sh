#!/bin/bash

source /etc/profile
home_dir=/home/nhb

if [ $(whoami) != 'root' ]
then
	echo "please use sudo install!!!"
	exit
fi

# install basic packages
apt-get install ansible python3 python3-pip wget vim -y
pip3 install --upgrade pip

# install monaco font
git clone https://github.com/cstrap/monaco-font
cd  monaco-font
./install-font-ubuntu.sh https://github.com/todylu/monaco.ttf/blob/master/monaco.ttf?raw=true

# install shadowsocks-clint
cd $home_dir/×ÀÃæ/
wget https://github.com/shadowsocks/shadowsocks-qt5/releases/download/v3.0.0/Shadowsocks-Qt5-3.0.0-x86_64.AppImage
chmod a+x Shadowsocks-Qt5-3.0.0-x86_64.AppImage

# install python3's django depend packages
pip3 install django==1.11 pylint-django pylint autopep8
pip3 install virtualenv virtualenvwrapper

# add virtualenv variable to $home_dir/.bashrc
su - nhb -c "mkdir $home_dir/niuhaibao/Django_Projects"
echo "export WORKON_HOME=$home_dir/.virtualenvs" >> $home_dir/.bashrc
echo "export PROJECT_HOME=$home_dir/niuhaibao/Django_Projects" >> $home_dir/.bashrc
echo "source /usr/local/bin/virtualenvwrapper.sh" >> $home_dir/.bashrc
