import smtplib
import os
import imghdr
import re
import logging
import datetime
from email.message import EmailMessage
from smtplib import SMTPConnectError

# Set up logging
logging.basicConfig(filename='email.log', level=logging.INFO)

# Define regular expression pattern to validate email addresses
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

# Read email credentials from environment variables
sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')

# If email credentials are not set as environment variables, exit the script
if sender_email is None:
    logging.error('Error: Sender email not found in environment variables')
    exit()
if sender_password is None:
    logging.error('Error: Sender password not found in environment variables')
    exit()

# Set the recipients' email addresses
recipients = ['test1@gmail.com', 'test2@gmail.com']

# Validate email addresses
for recipient in recipients:
    if not re.match(email_pattern, recipient):
        logging.error(f"Error: '{recipient}' is not a valid email address")
        exit()

# Create a new email message
msg = EmailMessage()
msg['Subject'] = 'Test email'
msg['From'] = sender_email
msg['To'] = ', '.join(recipients)
msg.set_content('This is a test email')

# Attach a file to the email
attachment_path = '/path/to/attachment/file'

# Validate that the attachment file exists
if not os.path.exists(attachment_path):
    logging.error("Error: Attachment file doesn't exist")
    exit()

# The file to be attached to the email is opened and read into memory using a with statement.
with open(attachment_path, 'rb') as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)
    file_name = os.path.basename(f.name)
msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

# Send the email using the SMTP server
try:
    with smtplib.SMTP('smtp.mail.me.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)
except SMTPConnectError as e:
    logging.error('Error: Unable to connect to SMTP server')
    logging.error(str(e))
    exit()

logging.info('Email sent!')