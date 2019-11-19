import argparse
import datetime
import ntpath
import smtplib 
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# return a list of recepients obtained from a contacts file
# each line in the file represents a single contact.
def getRecipientsFromFile(filename):
	recepients=[]
	with open(filename, 'r') as contacts:
		for contact in contacts:
			recepients.append(contact.rstrip('\n'))
	return recepients

# return a string that is the message body obtained from a 
# message file.
def getMessageBodyFromFile(filename):
	message_body=""
	with open(filename, 'r') as body:
		message_body=body.read()
	return message_body

# assign variables from command line arguments
sender=sys.argv[1]
subject=sys.argv[2]
contacts_filename=sys.argv[3]
body_filename=sys.argv[4]
full_path=sys.argv[5]
filename=ntpath.basename(full_path)

recipients=getRecipientsFromFile(contacts_filename)
message_body=getMessageBodyFromFile(body_filename)
smtp = smtplib.SMTP(host='', port=)

# configure the email message
msg = MIMEMultipart()
msg['From']=sender
msg['To']=",".join(recipients)
msg['Subject']=subject
msg.attach(MIMEText(message_body, 'plain'))

# retrieve the attachment from the full path
attachment=open(full_path, 'rb')

p=MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', 'attachment; filename= %s' % filename)

# attach file
msg.attach(p)

# send the message
smtp.send_message(msg)

# delete message and quit
del msg
smtp.quit()
