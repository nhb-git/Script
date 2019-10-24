#!/bin/bash

source /etc/profile
home_dir=/home/nhb

if [ $(whoami) != 'root' ]
then
	echo "please use sudo install!!!"
	exit
fi
# change software resource
cp /etc/apt/sources.list /etc/apt/sources.list.bak
cat > /etc/apt/sources.list <<EOF
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security universe 
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security multiverse
EOF

apt-get update -y 
sudo apt remove libappstream3
# install basic packages
apt-get install ansible python3 python3-pip  python3-venv python-pip git wget vim npm gcc make perl gdebi ssh-askpass bpython zsh -y
apt purge unity-webapps-common thunderbird totem rhythmbox empathy brasero simple-scan gnome-mahjongg aisleriot gnome-mines cheese gnome-sudoku transmission-common gnome-orca webbrowser-app landscape-client-ui-install deja-dup -y

chsh -s /bin/zsh
su - nhb -c "chsh -s /bin/zsh"

# modify pip resource and update pip3
mkdir -p ~/.pip
rm -f ~/.pip/pip.conf
echo "[global]" >> ~/.pip/pip.conf
echo "trusted-host =  mirrors.aliyun.com" >> ~/.pip/pip.conf
echo "index-url = https://mirrors.aliyun.com/pypi/simple" >> ~/.pip/pip.conf

su - nhb -c "mkdir -p ~/.pip"
su - nhb -c "rm -f ~/.pip/pip.conf"
su - nhb -c 'echo "[global]" >> ~/.pip/pip.conf'
su - nhb -c 'echo "trusted-host =  mirrors.aliyun.com" >> ~/.pip/pip.conf'
su - nhb -c 'echo "index-url = https://mirrors.aliyun.com/pypi/simple" >> ~/.pip/pip.conf'
pip3 install --upgrade pip
# install python3's django depend packages
pip3 install pylint autopep8 virtualenv virtualenvwrapper
apt-get update -y && apt-get dist-upgrade -y

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
git config --global credential.helper store

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

# npm
su - nhb -c "npm config set registry https://registry.npm.taobao.org"

# change anaconda source
cat > ~/.condarc <<EOF
channels:
  - defaults
show_channel_urls: true
default_channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
custom_channels:
  conda-forge: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  msys2: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  bioconda: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  menpo: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  pytorch: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
  simpleitk: https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud
EOF
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security universe 
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security multiverse
EOF
