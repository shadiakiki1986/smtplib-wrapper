#!/bin/bash

export SMTP_SERVER=$1
export SMTP_PORT=$2
export SMTP_USER=$3
export SMTP_PASS=$4
export SMTP_EMAIL=$5
export SMTP_TEST=$6
export SMTP_SASL=$7
export SMTP_HOST=`cat /etc/hostname`

if [ -z "$SMTP_SERVER" ]; then echo "Empty SMTP_SERVER"; exit 1; fi
if [ -z "$SMTP_PORT"   ]; then echo "Empty SMTP_PORT";   exit 1; fi
if [ -z "$SMTP_USER"   ]; then echo "Empty SMTP_USER";   exit 1; fi
if [ -z "$SMTP_PASS"   ]; then echo "Empty SMTP_PASS";   exit 1; fi
if [ -z "$SMTP_EMAIL"  ]; then echo "Empty SMTP_EMAIL";  exit 1; fi
if [ -z "$SMTP_TEST"   ]; then echo "Empty SMTP_TEST";   exit 1; fi
if [ -z "$SMTP_SASL"   ]; then echo "Empty SMTP_SASL";   exit 1; fi
if [ -z "$SMTP_HOST"   ]; then echo "Empty SMTP_HOST";   exit 1; fi

cat /code/postfix-configs/main.cf | envsubst > /etc/postfix/main.cf

cat /code/postfix-configs/sasl_passwd | envsubst > /etc/postfix/sasl_passwd
cat /code/postfix-configs/generic | envsubst > /etc/postfix/generic
cat /code/postfix-configs/canonical | envsubst > /etc/postfix/canonical
postmap /etc/postfix/sasl_passwd
postmap /etc/postfix/generic
postmap /etc/postfix/canonical

cat /code/config-sample.yml | envsubst > /code/config.yml

service postfix start
service rsyslog start
pew in ENV2 python /code/setup.py install
pew in ENV2 python -m unittest TestMailer TestConfig
# sleep is needed in the entrypoint above so that the postfix queue has time to be flushed
isec=10
while [ $isec -gt 0 ]; do
  echo "Please wait $isec seconds while the queue is flushed"
  sleep 1
  isec=$((isec-1))
done
postfix stop
service postfix stop
service rsyslog stop
cat /var/log/mail.log
"true"
