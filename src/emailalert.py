import smtplib
from smtplib import SMTPException
import email


class EmailAlert(object):
    def __init__(self, smtpserver = None):
        if smtpserver == None:
            raise Exception('SMTP server not specified')

        self.smtpObj = smtplib.SMTP(smtpserver)

    def send(self, sender, receivers, subject, body):
        try:
            message = "From: %s \nTo: %s \nSubject: %s \n\n%s\n" % \
                (sender, ', '.join(receivers), subject, body)
            self.smtpObj.sendmail(sender, receivers, message)
        except SMTPException as se:
            print "Error: unable to send email: ", str(se)
