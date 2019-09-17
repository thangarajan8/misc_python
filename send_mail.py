#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:12:07 2018

@author: thanga
"""
def send_mail(mail_body,subject,attachemnet = 'sample.py'):
    mail_id = 'vinithas29@gmail.com' #sender mail id
    password = 'AooAoo_123' # sender password
    to = ['thangam.rajan8@gmail.com','vinithas29@gmail.com'] # list of mail ID you want to send
    msg = MIMEMultipart()  # building MIME
    msg['From'] = mail_id 
    msg['To'] = mail_id
    msg['Subject'] = subject
    msg.attach(MIMEText(mail_body))
    with open(attachemnet, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=os.path.basename(attachemnet)
            )
        # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % os.path.basename(attachemnet)
    msg.attach(part)
    smtpserver = smtplib.SMTP("smtp.gmail.com", 587) #this config is for gmail if you are using anyother mail please get smtp details 
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(mail_id, password)
    smtpserver.sendmail(mail_id, to, msg.as_string()) 
    smtpserver.quit() 

import smtplib 
import logzero
import os
from logzero import logger
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import COMMASPACE, formatdate
from datetime import datetime
now = datetime.now()
log_file_name = 'sample_{}.log'.format(now.strftime("%Y%m%d"))
logzero.logfile(log_file_name, maxBytes=1e6, backupCount=3) #log file generation

a = 10
b = 20
message = {'fail':'Cannot divide by Zero','sucess': 'able to divide'}
logger.info('Dividing {} by {}'.format(a,b))
try:
    c = b/a
    logger.info('Able to divide') #sample log for information
    send_mail(mail_body=message['sucess'],subject = 'Sucess {}'.format(datetime.now()))
except Exception:
    logger.error('Cannot divide by zero') #sample log for error
    send_mail(mail_body=message['fail'], subject = 'Fail {}'.format(datetime.now()))