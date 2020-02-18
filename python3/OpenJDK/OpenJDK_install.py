#! -*- coding: utf-8 -*-
"""
author: bao
email: niuhaibaovip@163.com
"""

import os
import tarfile
import requests


class OpenJdk:
    def __init__(self):
        self.name = 'jdk'
        self.package_path = ''
        self.jdk_install_dir = '/usr/java'

    def download_jdk(self):
        package_name = self.name + '.tar.gz'
        package_path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), package_name
        )
        os.chdir(os.path.dirname(package_path))
        download_url = 'https://download.java.net/java/GA/' \
            + 'jdk12.0.2/e482c34c86bd4bf8b56c0b35558996b9/10/' \
            + 'GPL/openjdk-12.0.2_linux-x64_bin.tar.gz'
        try:
            r = requests.get(download_url)
            with open(package_name, 'wb') as content:
                content.write(r.content)
            self.package_path = package_path
            print('Download JDK Success.')
        except:
            print('Download JDK FAILED.')

    def unzip_jdk(self):
        if not os.path.exists(self.jdk_install_dir):
            os.makedirs(self.jdk_install_dir)
        try:
            tar = tarfile.open(self.package_path, "r:gz")
            file_names = tar.getnames()
            for names in file_names:
                tar.extract(names, self.jdk_install_dir)
            tar.close()
            print('解压到了{0}路径'.format(self.jdk_install_dir))
        except:
            print('解压失败')

    def add_env(self):
        try:
            with open('/etc/profile', 'a') as profile:
                profile.write('export JAVA_HOME=/usr/java/jdk-12.0.2/')
                profile.write('\n')
                profile.write('export PATH=$PATH:$JAVA_HOME/bin')
                profile.write('\n')
            print('java环境变量增加成功')
        except FileExistsError:
            print('文件不存在')


java = OpenJdk()
java.download_jdk()
java.unzip_jdk()
java.add_env()

