email = ['timotiusgeralddandy@gmail.com', 'anisadianislami105@gmail.com', 'anggiaputri6016@gmail.com']
with open('email.txt', 'w') as f:
    for email in email:
        f.write(email)
        f.write('\n')

my_file = open('email.txt', 'r')
email = my_file.read()
email_list = email.split("\n")
print(email_list)

#teknik 1
import smtplib
import ssl
from email.message import EmailMessage

email_sender = 'anisadianislami105@gmail.com'
email_password = 'yojdwisynmmtdmoy'
email_receiver = email_list

subject = 'Check out my new video!'
body = """hii test test
"""
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

# teknik 2
import smtplib
  
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
  
# start TLS for security
s.starttls()
  
# Authentication
s.login("anisadianislami105@gmail.com", "yojdwisynmmtdmoy")
  
# message to be sent
message = "Message_you_need_to_send"
  
# sending the mail
s.sendmail("anisadianislami105@gmail.com", email_list[0], message)
  
# terminating the session
s.quit()
