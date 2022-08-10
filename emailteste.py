import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders

host2 = 'smail.jlab.org'
host = " smtpmail.jlab.org"
port = "25"
login = ""
password = ""

server = smtplib.SMPT(host, port)

server.ehlo()
server.starttls()
server.login(login, senha)

corpo = "<b>Email teste</b>"

email_message = MIMEMultipart()
email_msg['From'] = login
emai_msg['To'] = login
emai_msg['Subject'] = login
email_msg.attach(MIMEText(corpo,'html'))

arquivo = "C:\Users\arthu\Pictures\Saved Pictures"
## Read and Binary na variavel
attachment = open(cam_arquivo, "rb")

att = MIMEBase('application', 'octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)

att.add_header('Content-Disposition','attachment; filename= filename') ## filename = nome do arquivo que quero anexar
attachment.close()
email_msg.attach(att)



server.sendemail(email_msg['From'], emai_msg['To'], emai_msg.as_string)

server.quit()


