# -*- coding: utf-8 -*-
import os
import sys
import tarfile
import shutil
import subprocess


def unpack_package(package_dir, package_name, **kwargs):
    """"Unzip nginx package to dir"""
    kwargs.setdefault('temp_dir', '/tmp/nginx')
    temp_dir = kwargs['temp_dir']
    package_full_path = os.path.join(package_dir, package_name)
    software_name = '.'.join(package_name.split('.')[0:-2])
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    try:
        t = tarfile.open(package_full_path, 'r:gz')
        t.extractall(temp_dir)
    except FileNotFoundError:
        print('Please check {0} exist?'.format(package_full_path))
        sys.exit(1)
    except tarfile.ReadError:
        print(
            'Please check if the {0} format is gzip file'.format(
                package_full_path
            )
        )
        sys.exit(1)

    return os.path.join(temp_dir, software_name)


def format_compile_command(src_code_dir, install_dir):
    """"Format nginx's compile command"""
    compile_command_pattern = "cd {0} && ./configure --prefix={1} && make \
         && make install"
    compile_command = compile_command_pattern.format(
        src_code_dir, install_dir
    )
    return compile_command


def format_nginx_start_command(install_dir):
    nginx_start_command_pattern = " {0}/sbin/nginx "
    nginx_start_command = nginx_start_command_pattern.format(
        install_dir
    )

    return nginx_start_command


def exec_cmd(cmd):
    p = subprocess.Popen(
        cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = p.communicate()

    if p.returncode != 0:
        return p.returncode, stderr
    return p.returncode, stdout


def main():
    package = 'nginx-1.12.2.tar.gz'
    package_dir = '/root'
    install_dir = '/usr/local/nginx-1.12'
    src_code_dir = unpack_package(package_dir, package)
    # compile and install nginx
    exec_info = exec_cmd(format_compile_command(src_code_dir, install_dir))
    if exec_info[0] != 0:
        print(str(exec_info[1], encoding='utf-8'))
        print('*************************************')
        sys.exit(exec_info[0])
    print('nginx already compiled and installed.')
    print('*************************************')

    # start nginx
    exec_info = exec_cmd(format_nginx_start_command(install_dir))
    if exec_info[0] != 0:
        print(str(exec_info[1], encoding='utf-8'))
        print('*************************************')
        sys.exit(exec_info[0])
    print('nginx already started.')
    print('*************************************')


if __name__ == "__main__":
    main()
