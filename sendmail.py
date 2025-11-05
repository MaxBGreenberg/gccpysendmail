#!/bin/env python3
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
print("Enter appointment date:")
apptdate=input()
print("Enter appointment time:")
appttime=input()
print("Enter the number of patients:")
patnum=input()
print("Enter the email address of the recipient:")
recipient=input()
if patnum=="1":
	appt="son's circumcision"
else:
	appt="sons' circumcisions"
appttimeobj=datetime.strptime(appttime, "%I:%M%p")
arrtimeobj=appttimeobj-timedelta(minutes=15)
arrtime=arrtimeobj.strftime("%I:%M%p")
subject="Appointment Notification"
body=f"Hello,<br><br>Thank you for booking your {appt} with the <a href='https://drgreenberg.ca'>Greenberg Circumcision Centre</a>.<br>Your appointment is booked for {apptdate} at {appttime}. Please arrive no later than {arrtime}.<br>Please remember to pay by the end of the day today either via the <a href='https://drgreenberg.ca/product/circumcision-services/'>secture web protal</a> or by Interac e-Transfer to <a href='mailto:mark@drgreenberg.ca'>mark@drgreenberg</a>.<br>A map to our location can be found <a href='https://drgreenberg.ca/contact/'>here</a>.<br>Everything else you need to know is on <a href='https://drgreenberg.ca'>our website</a>.<br><br>Thanks,<br>Max"
msg=MIMEText(body,'html')
msg['Subject']=subject
msg['From']='info@drgreenberg.ca'
msg['To']=recipient
with smtplib.SMTP_SSL('mail.drgreenberg.ca',465) as server:
	server.login("info@drgreenberg.ca","<password>")
	server.send_message(msg)
