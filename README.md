# smtplib-wrapper
wrapper functions of smtplib python library

# Installation
    pip install https://github.com/shadiakiki1986/smtplib-wrapper

Manual install in pew virtualenv
    [sudo] apt-get update
    [sudo] apt-get install python-pip python-virtualenv python-dev
    pip install pew
    pew new -d ENV2
    pew in ENV2 python setup.py install

# Requirements
The `sendemail2` function requires the `/usr/sbin/sendmail` executable.
To install it run `[sudo] apt-get install postfix` and configure postfix

# Testing

Check .travis.yml file.
It was created with
    [sudo] apt-get install ruby ruby-dev
    [sudo] gem install travis
    # https://github.com/travis-ci/travis.rb#encrypt
    travis encrypt SMTP_EMAIL=myemail@provider.com --add
    travis encrypt SMTP_PWD=mypassword --add
    travis encrypt SMTP_SERVER=smtp.provider.com --add

Manual test (after manual install)
    cp config-sample.yml config.yml # and edit
    pew in ENV2 python -m unittest TestMailer
    pew in ENV2 python -m unittest TestConfig

