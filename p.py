import smtplib, ssl, email, imaplib

final_message_no="""Subject: Credit Card Security Alert

Transaction Blocked."""

final_message_yes="""Subject: Credit Card Security Alert

You may proceed with your transaction."""

final_message_unknown="""Subject: Credit Card Security Alert

Couldn't Process Reply. Reply with either Yes or No."""

port=465
context =ssl.create_default_context()
sender="chiefwarlock1707@gmail.com"
password="dementors"

mail=imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(sender, password)

mail.select("inbox")
result, data=mail.uid("search", None, "ALL")
inbox_item_list=data[0].split()
most_recent=inbox_item_list[-1]

result2, email_data=mail.uid("fetch", most_recent, "(RFC822)")
raw_email=email_data[0][1].decode("utf-8")

email_message=email.message_from_string(raw_email)

text_content=email_message.get_payload()
text_content2=text_content[0].get_payload()

if text_content2.find("No")>=0:
    print("Starting to send reply to No..")
    with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
        server.login(sender,password)
        server.sendmail(sender,receiver,final_message_no)
    print("Sent. Yay!")
elif text_content2.find("Yes")>=0:
    print("Starting to send reply to Yes..")
    with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
        server.login(sender,password)
        server.sendmail(sender,receiver,final_message_yes)
    print("Sent. Yay!")
else:
    print("Starting to send reply to unrecognised..")
    with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
        server.login(sender,password)
        server.sendmail(sender,receiver,final_message_unknown)
    print("Sent. Yay!")
