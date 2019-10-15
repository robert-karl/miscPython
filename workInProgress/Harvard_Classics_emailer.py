# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 13:54:21 2019

This function takes a file full of pdfs (or other eBooks) and emails them all 
to a Kindle device

@author: rinfi_000
"""

#import glob
import smtplib, ssl

path2file = r'C:\Users\rinfi_000\Documents\eBooks\HarvardClassics'

port = 587
#username = input("Type user name: ")
username = 'rinfinityk'
password = '5Neec9Ls7Qdr'
#password = input("Type Password: ")
fromAdd = "{}@gmx.us".format(username)
toAdd = 'rinfinityk@gmail.com'

message = """\
Subject: Testing

Hello World."""


#context = ssl.create_default_context()

server = smtplib.SMTP('mail.gmx.com',587)
#server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.ehlo()
server.login(fromAdd,password)
server.sendmail(fromAdd,fromAdd,message)

server.quit()


#with smtplib.SMTP_SSL("mail.gmx.com",port,context=context) as server:
    #server.login(fromAdd,password)
    #server.sendmail(fromAdd,toAdd,message)

#for filename in glob.glob(path2file):
    