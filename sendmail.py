#!/usr/bin/python

import smtplib
import os
import glob

def sendmail():
    for f in glob.glob('/home/hansolo81/projects/crawler/html/*.html'):
        fname = os.path.basename(f)
        to = fname[:-5]
        subject = 'New Property Alert'
        os.system('mailx -a "Content-type: text/html;" -s "%s"  %s < html/%s.html'\
              % (subject, to, to))

if __name__ == '__main__':
    sendmail()

