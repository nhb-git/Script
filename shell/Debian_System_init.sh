#!/bin/bash

source /etc/profile

# install basic packages
apt-get install ansible python3 python3-pip wget -y
pip3 install --upgrade pip

# install monaco font
git clone https://github.com/cstrap/monaco-font
cd  monaco-font
./install-font-ubuntu.sh https://github.com/todylu/monaco.ttf/blob/master/monaco.ttf?raw=true

# install shadowsocks-clint
cd /home/nhb/×ÀÃæ/
wget https://github.com/shadowsocks/shadowsocks-qt5/releases/download/v3.0.0/Shadowsocks-Qt5-3.0.0-x86_64.AppImage
chmod a+x Shadowsocks-Qt5-3.0.0-x86_64.AppImage

# install python3's django depend packages
pip3 install django==1.11 pylint-django pylint autopep8
