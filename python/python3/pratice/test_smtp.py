# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


sender_mail = 'niuhaibaovip@163.com'
receivers_mail = ['niuhb2@lenovo.com']

mail_host = 'smtp.163.com'
mail_user = 'niuhaibaovip@163.com'
mail_password = '6dXR6wWs1xxI'

message = MIMEText('Python mail test...', 'plain', 'utf-8')
message['From'] = _format_addr('niu<%s>' % sender_mail)
message['To'] = _format_addr('接收者<%s>' % receivers_mail)

subject = 'Python mail test'
message['Subject'] = Header(subject, 'utf-8').encode()

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 465)
    smtpObj.set_debuglevel(1)
    # smtpObj.starttls()
    smtpObj.login(mail_user, mail_password)
    smtpObj.sendmail(sender_mail, receivers_mail, message.as_string())
    smtpObj.quit()
    print('mail send sucessful.')
except smtplib.SMTPException:
    print('Error: mail send fail.')
