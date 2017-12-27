#!/bin/env python3
#导入smtp发件模块
import smtplib
 
#导入邮件内容构造模块
#from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user=""    #用户名
mail_pass=""   #口令 
 
 
#发件人地址
sender = 'xxx@xxxxxxxxx.com'

#接收邮件
receivers = 'niuhaibaovip@163.com'  
 
message = MIMEText('Python 邮件发送...', 'plain', 'utf-8')
message['From'] = _format_addr('niu<%s>' % sender)
message['To'] =  _format_addr('接收者<%s>' % receivers)
 
subject = 'Python SMTP 邮件'
message['Subject'] = Header(subject, 'utf-8').encode()
 
 
try:
    smtpObj = smtplib.SMTP('localhost', 25) 
    #smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    #smtpObj.set_debuglevel(1)
    #smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException as err:
    print ("Error: 无法发送邮件 %s" % err)
