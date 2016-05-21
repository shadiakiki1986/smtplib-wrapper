# smtplib-wrapper
wrapper functions of smtplib python library

# Installation
    pip install https://github.com/shadiakiki1986/smtplib-wrapper

# Requirements
The `sendemail2` function requires the `/usr/sbin/sendmail` executable.
To install it run `[sudo] apt-get install postfix` and configure postfix

# Testing
Check .travis.yml file.
It was created with
    travis env set SMTP_EMAIL    myemail@provider.com
    travis env set SMTP_PWD      mypassword
    travis env set SMTP_SERVER   smtp.provider.com
