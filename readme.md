bootstrap5 - https://getbootstrap.com/
bootstrap-icons - https://icons.getbootstrap.com/

### how to make email work

edit .env file

MAIL_SERVER = "smtp.qq.com"  <-- mail server
MAIL_USE_SSL = False
MAIL_USE_TLS = True
MAIL_USERNAME = "user-name@outlook.com"  <-- email address
MAIL_PASSWORD = "your-password"  <-- email address
    
FLASKY_MAIL_SUBJECT_PREFIX = "[Flask Education]"
FLASKY_MAIL_SENDER_TITLE = "Flask Education Admin"

flow the tutorial https://mailtrap.io/blog/flask-email-sending/
