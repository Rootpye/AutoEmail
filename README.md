# autoGmail
automatic email send program working on terminal

# requirements
- app password
- gmail

# Quick Start
1.install autoGmail.py

2. fix Username and Password to your google account and your 'app password'
```python
SMTP_Username = 'your_email@gmail.com'
SMTP_Password = 'abcd efgh ijkl mnop'
```

3. fix receiver@gmail.com to receivers gmail
```python
send_email("Test", "This is a test email.", "receiver@gmail.com
")
```

- You must follow this style to send email
```
send_email("Title", "Body", "receiver's gmail")
```
