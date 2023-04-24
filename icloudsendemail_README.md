Email Sending Script

This is a Python script that sends an email with an attachment using the Simple Mail Transfer Protocol (SMTP). Currently, it is set up to work with iCloud email service as the Email Service Provider (ESP) and can be modified to work with other ESPs as well.

Prerequisites

Before running this script, you must have the following:

Python 3.x installed
An email account with iCloud
An app password created in iCloud account (to use outside Apple developer projects)
The email address and app password stored in your terminal as environment variables
Usage

To use this script, follow these steps:

Clone or download this repository to your local machine.
Open a terminal window and navigate to the project directory.
Set the email address and app password as environment variables by running the following commands:
arduino
Copy code
export SENDER_EMAIL=<your email address>
export SENDER_PASSWORD=<your app password>
Modify the recipients list, attachment_path variable, and the email content to your needs.
Run the script by executing the following command in your terminal:
Copy code
python emailsend.py
Check the log file email.log to verify that the email was sent successfully.
