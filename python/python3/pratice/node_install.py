# -*- coding: utf-8 -*-
import os
import tarfile
import shutil
import subprocess


def unpack_package(package_dir, package_name, **kwargs):
    kwargs.setdefault('temp_dir', '/tmp/node')
    temp_dir = kwargs['temp_dir']
    package_full_path = os.path.join(package_dir, package_name)
    software_name = '.'.join(package_name.split('.')[0:-2])

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    try:
        t = tarfile.open(package_full_path, 'r:gz')
        t.extractall(temp_dir)
    except FileNotFoundError:
        raise SystemExit('Please check {0} path'.format(package_full_path))
    except tarfile.ReadError:
        raise SystemExit(
            'Please check if is {0} format is gzip file'.format(
                package_full_path
            )
        )
    return os.path.join(temp_dir, software_name)


def exec_cmd(cmd):
    p = subprocess.Popen(
        cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = p.communicate()

    if p.returncode != 0:
        return p.returncode, stderr
    return p.returncode, stdout


def install_node():
    package_name = 'node-v7.10.0-linux-x64.tar.gz'
    package_dir = '/home/appadmin'
    install_dir = '/usr/local/lenovosrv'
    software_path = unpack_package(package_dir, package_name)
    # 复制代码包到安装路径
    if not os.path.exists(install_dir):
        os.makedirs(install_dir)
    try:
        shutil.move(software_path, install_dir)
    except shutil.Error:
        pass
    os.symlink(os.path.join(install_dir, os.path.basename(software_path), 'bin/node'), '/usr/bin/node')
    os.symlink(os.path.join(install_dir, os.path.basename(software_path), 'bin/npm'), '/usr/bin/npm')


if __name__ == "__main__":
    install_node()
