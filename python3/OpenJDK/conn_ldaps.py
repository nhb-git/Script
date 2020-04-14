# -*- coding: utf-8 -*-
import json
from ldap3 import ALL ATTRIBUTES
# 注意：ldap3库如果要使用tls（安全连接），需要ad服务先安装并配置好证书服务，才能通过tls连接，否则连接测试时会报LDAPSocketOpenError('unable to open socket'
# 如果是进行账号密码修改及账户激活时，会报错：“WILL_NOT_PERFORM”
from ldap3 import Connection, NTLM, Server
from ldap3 import MODIFY_REPLACE

server1 = Server("lenovo.com", port=636, use_ssl=True, get_info=ALL, connect_timeout=5)
LDAP_SERVER_POOL = [server1]
SERVER_USER = 'adtest\\administrator'
SERVER_PASSWORD = "XXXXXXX"
 
class AD(object):
    '''    AD用户操作    '''
    def __init__(self):
        '''初始化'''
        self.conn = Connection( #配置服务器连接参数
            server=LDAP_SERVER_POOL,
            auto_bind=True,
            authentication=NTLM,  #连接Windows AD需要配置此项
            read_only=False,  #禁止修改数据：True
            user=SERVER_USER,#管理员账户
            password=SERVER_PASSWORD,
        )
 
        self.leaved_base_dn = 'ou=Leaved,dc=adtest,dc=intra'#离职账户所在OU
        self.active_base_dn = 'ou=测试部门,dc=adtest,dc=intra'#正式员工账户所在OU
        self.search_filter = '(objectclass=user)'#只获取【用户】对象
        self.ou_search_filter = '(objectclass=organizationalUnit)'#只获取【OU】对象
 
    def users_get(self):
        '''获取所有的用户'''
        self.conn.search(search_base=self.active_base_dn,search_filter=self.search_filter,attributes=ALL_ATTRIBUTES)
        res = self.conn.response_to_json()
        res = json.loads(res)['entries']
        return res
 
    def OU_get(self):
        '''获取所有的OU'''
        self.conn.search(search_base=self.active_base_dn,search_filter=self.ou_search_filter,attributes=ALL_ATTRIBUTES)
        res = self.conn.response_to_json()
        res = json.loads(res)['entries']
        return res
