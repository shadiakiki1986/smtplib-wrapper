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
    [sudo] apt-get install ruby ruby-dev
    [sudo] gem install travis
    # https://github.com/travis-ci/travis.rb#encrypt
    travis encrypt --add SMTP_EMAIL=myemail@provider.com
    travis encrypt --add SMTP_PWD=mypassword
    travis encrypt --add SMTP_SERVER=smtp.provider.com
