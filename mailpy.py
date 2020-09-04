# -*- coding: utf-8 -*-


import smtplib
import config

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message) 
        #sendmail(from, to , (sub, mgs))
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")
        
#subject = "this is a sample mail"
#msg = "Hello there, this mail is sent from a python programmed"  
#send_email(subject, msg)
