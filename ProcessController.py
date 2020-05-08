import csv
import random
import smtplib, ssl, email, imaplib



def dataloader(path, mode='n'):
    with open(path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # print(csv_reader)
        n = random.randint(1, 284000)

        #print(n)
        for i, row in enumerate(csv_reader):
            if i == n and mode(mode=='r'):
                data = row
                #print(data)
                #print(data[30])
                break
            elif (i == 624 and mode=='f'):
                data = row
                #print(data)
                break
            elif (i == 732 and mode == 'n'):
                data = row
                #print(data)
                break


        return data

def transaction(data):
    print("ID-"+str(data[0])+"has initiated transaction amount of "+str(data[29])+" USD")

def Mlmodel(input):
    network_output=30
    #print(input[network_output])
    if(input[network_output]=='1'):
        print("Fraud is detected")
        fraud=True
    else:
        print("No Fraud is detected")
        fraud= False
    return fraud

def sms(data):
    id=data[0]
    amount=data[29]
    final_message_no = """Subject: Credit Card Security Alert
    Transaction Blocked."""

    final_message_yes = """Subject: Credit Card Security Alert
    You may proceed with your transaction."""

    final_message_unknown = """Subject: Credit Card Security Alert
    Couldn't Process Reply. Reply with either Yes or No."""

    port = 465
    context = ssl.create_default_context()
    sender = "chiefwarlock1707@gmail.com"
    password = "dementors"

    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(sender, password)

    mail.select("inbox")
    result, data = mail.uid("search", None, "ALL")
    inbox_item_list = data[0].split()
    most_recent = inbox_item_list[-1]

    result2, email_data = mail.uid("fetch", most_recent, "(RFC822)")
    raw_email = email_data[0][1].decode("utf-8")

    email_message = email.message_from_string(raw_email)

    text_content = email_message.get_payload()
    text_content2 = text_content[0].get_payload()

    if text_content2.find("No") >= 0:
        print("Starting to send reply to No..")
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, final_message_no)
        print("Sent. Yay!")
    elif text_content2.find("Yes") >= 0:
        print("Starting to send reply to Yes..")
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, final_message_yes)
        print("Sent. Yay!")
    else:
        print("Starting to send reply to unrecognised..")
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, final_message_unknown)
        print("Sent. Yay!")





if __name__=="__main__":
    path = r"/home/shuvozit/Downloads/creditcardfraud/creditcard.csv"
    #Loading the Transaction data
    print("Transaction data loading started")
    transaction_data=dataloader(path, 'f')
    print(transaction_data)
    print("data loading complete")
    transaction(transaction_data)
    print("ML model start")
    fraud_factor= Mlmodel(transaction_data)
    print(fraud_factor)
    if fraud_factor:
        sms(transaction_data)
        print("okay")
    else:
        print("Transaction successful")



