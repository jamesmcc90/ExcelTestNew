import smtplib
import ssl
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import cx_Oracle
import pandas as pd
from datetime import datetime
import schedule

dsn = cx_Oracle.makedsn('localhost', '1521', 'xe')
conn = cx_Oracle.connect('SYS', '64lislunnan', dsn, cx_Oracle.SYSDBA)
c = conn.cursor()
script = 'SELECT * FROM CARS'
c.execute(script)
balance_report = pd.read_sql(script, conn).to_csv('BalanceDetails_' + time.strftime("%Y%m%d") + ".csv")

filename = "C:\\Users\\James\\Desktop\\ExcelTestNew\\BalanceDetails_20210130.csv"
now = datetime.now()

def mail():
    subject = "Balance report - " + now.strftime("%b") + " " + now.strftime("%d") + " " + now.strftime("%Y")
    body = "This is an email with attachment sent from Python"
    sender_email = "james.mcc90@gmail.com"
    receiver_email = "james.mcc90@gmail.com"
    password = "64lislunnan"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email

    message.attach(MIMEText(body, "plain"))

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)

    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)
    text = message.as_string()

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


schedule.every().day.at("16:44").do(mail)
print("Report sent")

while True:
    schedule.run_pending()
    # time.sleep(86400)  # suspend for 24 hours