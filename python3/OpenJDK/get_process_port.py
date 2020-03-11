# -*- coding: utf-8
#!/usr/bin/env python3
import re
import subprocess


def get_process_pid(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    process_pid_list = p.communicate()[0].decode('utf-8').split(' java\n')
    process_pid_filter = filter(lambda x: bool(x)==True, process_pid_list)
    process_pid_list = list(map(lambda x: int(x), process_pid_filter))
    return process_pid_list


def get_process_port(process_pid):
    p = subprocess.Popen('sudo netstat -tulnp | grep {0}/'.format(process_pid),
                         shell=True, stdout=subprocess.PIPE)
    try:
        process_net_info = re.split(r' *', p.communicate()[0].decode('utf-8'))
        process_port = int(process_net_info[3].split(':')[-1])
    except IndexError:
        process_port = ' 不存在'
    return process_port


def get_process_name(process_pid):
    cmd_file = '/proc/{0}/cmdline'.format(process_pid)
    with open(cmd_file) as f:
        for line in f:
            cmd_info = re.search(r'(CPM.*)(CPM-.*)\.jar', line)
    return cmd_info.group(2)


def main():
    pid_list = get_process_pid('pgrep -l "java"')
    for pid in pid_list:
        port = get_process_port(pid)
        name = get_process_name(pid)
        print("进程{0}的运行端口是:{1}".format(name, port))


if __name__ == '__main__':
    main()
