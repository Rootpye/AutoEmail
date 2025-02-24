import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Email configuration
SMTP_Server = 'smtp.gmail.com'
SMTP_Port = 587
# This is sample email address and 'app password'.
# You need to make 'app password' in your google account!
SMTP_Username = 'your_email@gmail.com'
SMTP_Password = "abcd efgh ijkl mnop"

def user_input_reciever():
    input("Enter the email address of the reciever: ")

def user_input_subject():    
    input("Enter the subject of the email: ")

def user_input_body():   
    input("Enter the body of the email: ")

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
send_email("Test", "This is a test email.", "receiver@gmail.com")
