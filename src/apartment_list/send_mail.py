import smtplib


def send_email():
    gmail_user = "heathensoul.inc@gmail.com"
    gmail_pwd = "*Godisgreat1"
    FROM = "heathensoul.inc@gmail.com"
    TO = "heathensoul.inc@gmail.com" 
    SUBJECT = "hello"
    TEXT = "hey you!"

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")
send_email()