import smtplib

sender_email = "chiefwarlock1707@gmail.com"
rec_email = "ushnikuk11@gmail.com"
password = "dementors"
message = """\
Subject: Possible Credit Card Fraud

Your Credit Card Number xxxx-xxxx-xxxx-xxxx is being used to make a 
transaction of amount: _______ 
If it is an authorised transaction reply : Yes
If it is not authorised by you reply : No

Regards
Wizengamot 
"""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)
