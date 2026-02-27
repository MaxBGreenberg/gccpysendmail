#!/bin/env python3
# Script for automating sending of appointment confirmation emails
# Licensed under GPLv2
# Import modules
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
import json
import imaplib
import time
from email.utils import formatdate
# Prompt for user input
print("Enter appointment date (YYYYMMDD format):")
apptdate=input()
print("Enter appointment time (HHMM 24hr format):")
appttime=input()
print("Enter the number of patients:")
patnum=input()
print("Enter the email address of the recipient:")
recipient=input()
# Adjust grammar of email depending on number of patients specified
if patnum in ("","0","1"):
	appt="son's circumcision"
else:
	appt="sons' circumcisions"
# Convert input date and time to date time objects
# Get arrival time by doing arithmetic on apppointment time
# Convert appointment time from input fomrat to display format
apptdateobj=datetime.strptime(apptdate, "%Y%m%d")
appttimeobj=datetime.strptime(appttime, "%H%M")
arrtimeobj=appttimeobj-timedelta(minutes=15)
arrtime=arrtimeobj.strftime("%I:%M%p").lstrip("0")
appttimedisp=appttimeobj.strftime("%I:%M%p").lstrip("0")
apptdatedisp=f"{apptdateobj.strftime('%A')}, {apptdateobj.strftime('%B')} {apptdateobj.day}"
# HTML for body of the email
body=f"Hello,<br><br>Thank you for booking your {appt} with the <a href='https://drgreenberg.ca'>Greenberg Circumcision Centre</a>.<br>Your appointment is booked for {apptdatedisp} at {appttimedisp}. Please arrive no later than {arrtime}.<br>Please remember to pay by the end of the day today either via the <a href='https://drgreenberg.ca/product/circumcision-services/'>secture web portal</a> or by Interac e-Transfer to <a href='mailto:mark@drgreenberg.ca'>mark@drgreenberg.ca</a>.<br>A map to our location can be found <a href='https://drgreenberg.ca/contact/'>here</a>.<br>Everything else you need to know is on <a href='https://drgreenberg.ca'>our website</a>.<br><br>Thanks,<br>Max"
# Load email credentials from JSON file
with open("secrets.json","r") as f:
	secrets=json.load(f)
username=secrets["username"]
password=secrets["password"]
server_url=secrets["server_url"]
port=secrets["port"]
# Define email structure
msg=MIMEText(body,'html')
msg['Subject']='Appointment Notification'
msg['From']=username
msg['To']=recipient
# Send email
with smtplib.SMTP_SSL(server_url,port) as server:
	server.login(username,password)
	server.send_message(msg)
imap_server="mail.drgreenberg.ca"
sent_folder="INBOX.Sent"
with imaplib.IMAP4_SSL(imap_server) as imap:
	imap.login(username,password)
	imap.append(sent_folder,'\\Seen',imaplib.Time2Internaldate(time.time()),msg.as_bytes())
	imap.logout()
