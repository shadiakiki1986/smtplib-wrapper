# smtplib-wrapper
wrapper functions of smtplib python library

# Installation
Install into python project
```bash
pip install https://github.com/shadiakiki1986/smtplib-wrapper
```
Manual install in pew virtualenv
```bash
[sudo] apt-get update
[sudo] apt-get install python-pip python-virtualenv python-dev
pip install pew
pew new -d ENV2
pew in ENV2 python setup.py install
```
# Requirements
The `sendemail2` function requires the `/usr/sbin/sendmail` executable.
To install it run `[sudo] apt-get install postfix` and configure postfix

# Unit tests
I have no unit tests

# Integration Testing
* Install docker-engine (requires 64-bit OS)
 * Do not use apt-get install docker
 * Ref: https://docs.docker.com/v1.8/installation/ubuntulinux/
```bash
curl -sSL https://get.docker.com/ | sh
# add user to group docker
sudo usermod -aG docker ubuntu
# log out and back in
# test
docker run hello-world
```
* If desired, can run `apt-cacher`
 * https://hub.docker.com/r/clue/apt-cacher/
```bash
docker run -d -p 3142:3142 -t clue/apt-cacher
```
* Run built image
 * either just pull the [automated build image](https://hub.docker.com/r/shadiakiki1986/smtplib-wrapper/) and run
```bash
docker run -i -t shadiakiki1986/smtplib-wrapper server port username password email1 email2 (ntlm|login)
```
 * or build dockerfile manually (skip `--build-arg USE_APT_CACHER` if apt-cacher not running)
```bash
docker build --build-arg USE_APT_CACHER -t smtplib-wrapper .
docker run -i -t smtplib-wrapper server port username password email1 email2 (ntlm|login)
```

* check that a test email is received at email1 and email2
