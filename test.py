#!/bin/env python3
# Script for automating sending of appointment confirmation emails
# Licensed under GPLv2
from datetime import datetime, timedelta
print("Enter appointment date:")
apptdate=input()
print("Enter appointment time:")
appttime=input()
print("Enter the number of patients:")
patnum=input()
print("Enter the email address of the recipient:")
recipient=input()
if patnum in ("","0","1"):
	appt="son's circumcision"
else:
	appt="sons' circumcisions"
appttimeobj=datetime.strptime(appttime, "%H%M")
arrtimeobj=appttimeobj-timedelta(minutes=15)
arrtime=arrtimeobj.strftime("%I:%M%p").lstrip("0")
appttimedisp=appttimeobj.strftime("%I:%M%p").lstrip("0")
print(apptdate)
print(appttime)
print(appttimedisp)
print(arrtime)
print(appt)
