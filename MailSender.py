# mail 

import smtplib

smtp = smtplib.SMTP('smtp.gmail.com',587)

smtp.ehlo()
smtp.starttls()

smtp.login("username","password")

msg=" this is my message"

try:
    smtp.sendmail("ashna.khanna100@gmail.com","trainer.gkattri@gmail.com",msg)
    print("mail sent ")
except:
    print("mail not sent")