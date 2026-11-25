import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import configure
def msg():
    subject="ALERT!"
    msg=MIMEMultipart()
    msg['From']=configure.USER_NAME
    msg['To']=configure.USER_NAME
    msg['Subject']=subject
    body="Some activity has been detected in your office. An image has been attached in this alert mail.The remaining have been backed up in your system."
    msg.attach(MIMEText(body,'plain'))
    fp=open("screen5.png",'rb')
    img=MIMEImage(fp.read())
    fp.close()
    img.add_header('Content-Disposition', 'attachment', filename="screen5.png")
    msg.attach(img)
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(configure.USER_NAME,configure.PASSWORD)
    s.sendmail(configure.USER_NAME,configure.USER_NAME,msg.as_string())
    s.quit()
print("Done")
