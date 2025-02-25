import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

otp = random.randint(1111,9999)

smtp_server = "smtp.gmail.com"
smtp_port = 587

username = "harshithamudhiraj16@gmail.com"
password = "asdc ximm dyvu ujxs"

from_email = "harshithamudhiraj16@gmail.com"
to_email = input("Enter email to send OTP: ")
subject = "OTP Validation:"
body = f"OTP for validation is {otp}. \nthank you."

msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['subject'] = subject
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP(smtp_server,smtp_port)
server.starttls()
server.login(username,password)
server.send_message(msg)
server.quit()

print("email sent")
for i in range(3):
    x=int(input("Enter OTP Recieved to your mail: "))
    if (x == otp):
      print("valid")
      break
    else:
        print("invalid,try again")
else:
    print("invalid, no options left")


