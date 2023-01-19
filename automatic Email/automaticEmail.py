import os
import smtplib
import ssl
from email.message import EmailMessage
from email.utils import formataddr
from dotenv import load_dotenv

import pandas as pd
import numpy as np

load_dotenv('.env') 

password = os.environ.get('__PASSWORD__')

df = pd.read_csv('emails.csv')
userEmails = np.array(df['Username'])
collegeEmails = np.array(df['College email'])
names=np.array(df['Name'])

email_sender = 'sharmakushalbastakoti@gmail.com'
email_password = password
# email_receiver = 'kushal.191517@ncit.edu.np'
# email_receiver = 'kushal.191517@ncit.edu.np'

for email_receiver,user_name in zip(collegeEmails,names):
    subject = 'Notice From Python Code Along'
    body = """
    Dear {0},

    We have recieved your registration for Python Code Along held on Jan 20 at 2:00 pm.
    You are cordially invited to attend the session.
    Please make sure to have python pre-installed in your platform.

    If you have any querries do reply to this mail.
    And if you are wondering this email is sent using help of Python Automation.

    With Regards,
    Kushal SB
    """.format(user_name)

    em = EmailMessage()
    em['From'] =formataddr(('Kushal SB', email_sender))
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
    except Exception as e:
        print(e)