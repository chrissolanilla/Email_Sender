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
#sum varible so we can send 100 emails at a time
sum=0
#function that sends the email
def sendEmail():
    with open(r'C:\Users\chris\OneDrive\Documents\PythonScrape\project\emails.csv.csv','r') as csvfile:
        reader=csv.reader(csvfile)
        #I need to make sure it only sends up to 100 emails. after that I need to make sure when its called again it picks up where it left off. 
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
#now we have to actually call the function but within some loop for how many email address we have. 
#I think one solution is to have another csv file of all our email addresses with their passwords and read the varible from there as well.

#open csv file with our email addresses and passwords to send emails
with open('emailsenders.csv','r') as csvfile:
    reader2= csv.reader(csvfile)
    #loop for how many emails we have in the csv file
    for col in reader2:
        #setting the email and password to what is in the csv file
        email_sender=col[0]
        password=col[1]
        #now we call the function passing in the varibles?
        #create a sum varible that increments by 100 so that we can pass it in the function so it can loop from there to there
        sum+=100
        sendEmail()
        # i guess we dont pass in varibles cause it has no parameters lol
        #perhaps we should pass in varibles in the parameter containing the email server and stuff. 





        