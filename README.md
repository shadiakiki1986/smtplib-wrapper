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

# Unit tests
I have no unit tests

# Integration Testing
Prepare postfix configs
    mkdir postfix-configs
    touch postfix-configs/sasl_passwd # and edit
    touch postfix-configs/canonical # and edit
    touch postfix-configs/generic # and edit
    touch postfix-configs/main.cf # and edit

Prepare smtplib-wrapper config
    cp config-sample.yml config.yml # and edit

Use dockerfile
    docker build . -t smtplib-wrapper
    docker run -it smtplib-wrapper
