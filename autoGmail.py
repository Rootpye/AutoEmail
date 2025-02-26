import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
SMTP_Server = 'smtp.gmail.com'
SMTP_Port = 587
# This is sample email address and 'app password'.
SMTP_Username = 'your_email@gmail.com'
# You need to make 'app password' in your google account!
SMTP_Password = "abcd efgh ijkl mnop"

# Get information to user
to = input("Enter recievers' email address: ")
subject = input("Enter subject of email : ")
body = input("Enter body of email : ")

# Send email function
def send_email(subject, body, to):
    msg = MIMEMultipart()
    msg['From'] = SMTP_Username
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

# SMTP server connection, send email and close connection
    try:
        server = smtplib.SMTP(SMTP_Server, SMTP_Port)
        server.starttls()
        server.login(SMTP_Username, SMTP_Password)
        text = msg.as_string()
        server.sendmail(SMTP_Username, to, text)
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print('Something went wrong...', e)

# Send email
send_email(subject, body, to)
