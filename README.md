# smtplib-wrapper
wrapper functions of smtplib python library

# Installation
Install into python project
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
After manual install (instructions above)
    apt-get install libyaml-dev mailutils
    cp config-sample.yml config.yml # and edit
    pew in ENV2 python -m unittest TestMailer
    pew in ENV2 python -m unittest TestConfig

