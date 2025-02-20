# autoEmail
automatic email send program working on terminal

# requirements
- app password
- gmail

# Quick Start
install autoEmail.py

fix Username and Password to your google account and your 'app password'
```python
SMTP_Username = 'your_email@gmail.com'
SMTP_Password = 'abcd efgh ijkl mnop'
```

fix receiver@gmail.com to receivers gmail
```python
send_email("Test", "This is a test email.", "receiver@gmail.com
")
```

You must follow this style to send email
```
send_email("Title", "Body", "receiver's gmail")
```
