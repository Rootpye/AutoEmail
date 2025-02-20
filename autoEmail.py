import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Email configuration
SMTP_Server = 'smtp.gmail.com'
SMTP_Port = 587
SMTP_Username = 'kimpenguin4300@gmail.com'
# You need to make app password in your google account!!
SMTP_Password = "zukg qyku nfrl oygo"


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

# Test
send_email("Test", "This is a test email.", "cdam0075@gmail.com")
