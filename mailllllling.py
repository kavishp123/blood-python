import smtplib
from email.mime.text import MIMEText
# import register

def email(user):
    body="Thank you for registering on our application you are doing a great job by donating blood. "

    #creteMIMEText class object with body text
    msg=MIMEText(body)

    #from which address the mail is sent
    fromaddr="your_email_id_here"

    # to which address the mail is sent
    toaddr=user

    #store the address into msg object

    msg['From']=fromaddr
    msg['To']=toaddr
    msg['subject']="Thank you for Registering"

    #connect to gmail.com server using 587 port no.
    server=smtplib.SMTP('smtp.gmail.com',587)

    # starting TLS mode
    server.starttls()
    # logining into the mail
    server.login(fromaddr,"*************")

    server.send_message(msg)
    print('Mail sent....')

    server.quit()
