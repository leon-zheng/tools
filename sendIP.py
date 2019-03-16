import os
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from datetime import datetime as dt

def get_ip():
    os.system("hostname > ip.txt")
    os.system("ip -f inet addr >> ip.txt")
    f = open("ip.txt")
    text = "".join(f.readlines())
    f.close()
    os.system("rm ip.txt")
    return text

def email_send(smtp_server,from_addr,username,password,to_addr,subject,text):
	msg = MIMEText(text, 'plain', 'utf-8')
	msg['From'] = format_addr(username + '<%s>' % from_addr)
	msg['To'] = format_addr('<%s>' % to_addr)
	msg['Subject'] = Header(subject, 'utf-8').encode()
	
	server = smtplib.SMTP(smtp_server, 25)
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()

def format_addr(s):
	name, addr = parseaddr(s)
	return formataddr((Header(name, 'utf-8').encode(), addr))

if __name__ == '__main__':
	smtp_server = '<replace with your smtp server>'
	from_addr = '<replace with your email address>'
	username = '<replace with your username>'
	password = '<replace with your smtp authorization code>'
	to_addr = '<replace with receiver email address>'
	subject = "Report at " + dt.strftime(dt.now(),'%Y-%m-%d %H:%M:%S')
	text = get_ip()
	email_send(smtp_server,from_addr,username,password,to_addr,subject,text)