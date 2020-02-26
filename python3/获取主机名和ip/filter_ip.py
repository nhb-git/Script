# -*- coding: utf-8 -*-
import xlwt


def get_hostname_ip(filename):
    try:
        with open(filename) as f:
            for line in f:
                split_result = line.split('=')
                if len(split_result) == 2:
                    hostname = split_result[0].split()[0]
                    ip = split_result[1].split()[0]
                    yield hostname, ip
    except FileExistsError:
        print('check {0} file.'.format(filename))


def write_xl(result):
    hostname_ips = []
    for hostname_ip in result:
        hostname_ips.append(hostname_ip)
    index = len(hostname_ips)
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('服务器信息')
    title = ['HostName', 'IP']
    # for i in range(0, len(title)):
    #    sheet.write(0, i, title[i])
    for i in range(0, len(hostname_ips)):
        for j in range(0, len(hostname_ips[i])):
            sheet.write(i, j, hostname_ips[i][j])
    workbook.save(r'D:\Github\Script\python3\获取主机名和ip\test.xls')


hostname_ip = get_hostname_ip(r'D:\Github\Script\python3\获取主机名和ip\source.txt')
write_xl(hostname_ip)

