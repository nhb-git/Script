#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 开发人员   ：Davis Niu
# 开发时间   ：7/2/2020  5:02 PM 
# 文件名称   ：漏洞分析.py
import os
import openpyxl


class Vul:
    """
    根据安全的漏洞报告统计分析数据
    """
    @property
    def vul_file_name(self):
        return self.vul_file

    @vul_file_name.setter
    def vul_file_name(self, vul_file):
        vul_file = vul_file.strip()
        if os.path.isfile(vul_file):
            self.vul_file = vul_file
        else:
            raise FileNotFoundError('文件不存在')

    def get_vul_ip(self, title='IP', col='C'):
        try:
            self.ip_list = list()
            vul_lx_obj = openpyxl.load_workbook(self.vul_file)
            sheet_obj = vul_lx_obj.active
            ips_info = sheet_obj[col]
            for ip in ips_info:
                if ip.value == title:
                    continue
                else:
                    self.ip_list.append(ip.value)
            return self.ip_list
        except:
            print('Excel文件存在异常')


v = Vul()
v.vul_file_name = r'C:\Users\niuhb2\Downloads\Weely Meeting OVP Vulnerability.xlsx'
print(v.get_vul_ip())
