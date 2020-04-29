import smtplib

sender_email = "susmit12ronaldo@gmail.com"
rec_email = "susmit12ronaldo@gmail.com"
password = input(str("Please enter your password : "))
message = """\
Subject: Python Email Tutorial

This is from python!

Tech With Tim
"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)
