#Work in progress, goal is to have it send up to only 100 emails from the csv, then switch accounts to another email and send 100 more emails from the csv. 
#do this process until csv file is empty
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

# varible for our email address that will change 
email_sender=""
#varible for our email address that will change
password= ""
#subject var
subject="Subscription activated"
#function that sends the email
def sendEmail():
    with open(r'C:\Users\chris\OneDrive\Documents\PythonScrape\project\emails.csv.csv','r') as csvfile:
        reader=csv.reader(csvfile)
        for line in reader:
            text= "hello " + line[1] +" your "+line[2]+" plan has activated"
            #(test our subject message) 
            # print(text)
            #lets store the email address we are sending to
            doctorEmail= line[0]
            msg=MIMEMultipart()
            msg['From']= email_sender
            msg['To']=doctorEmail
            msg['Subject']=subject
            msg.attach(MIMEText(text,"plain"))
            text=msg.as_string()

            server= smtplib.SMTP_SSL("smtp.gmail.com",465)
            server.login(email_sender,password)
            server.sendmail(email_sender,doctorEmail,text)

            server.quit()
# main function time
email_sender=input(print("what is your email address\n"))

password= input(print('enter your password'))




        