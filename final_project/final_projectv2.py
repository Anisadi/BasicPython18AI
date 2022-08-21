from cgitb import text
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

#list reciver email
email_list = open("final_project\email.txt", "r")
x = (email_list.readlines())

def myfunc():
    print(x)

myfunc()

#details
from_email = "anisadianislami@gmail.com"
to_email = x
msg = MIMEMultipart()
msg["From"] = from_email
msg["To"] = x
msg["Subject"] = "Simple VA Project"
body = "Simple VA Project"
msg.attach(MIMEText(body, "plain"))


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("anisadianislami105@gmail.com", "abcde")
text = msg.as_string()
#server.sendmail(fromaddr, toaddr, text)
#server.quit()

