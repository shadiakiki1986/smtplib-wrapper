FROM ubuntu

# configure postfix
RUN mkdir /etc/postfix
COPY ./postfix-configs/sasl_passwd /etc/postfix/sasl_passwd
COPY ./postfix-configs/canonical /etc/postfix/canonical
COPY ./postfix-configs/generic /etc/postfix/generic
COPY ./postfix-configs/main.cf /etc/postfix/main.cf
RUN test -f /etc/postfix/sasl_passwd
RUN test -f /etc/postfix/canonical
RUN test -f /etc/postfix/generic
RUN test -f /etc/postfix/main.cf 

# check config of smtplibe-wrapper
COPY . /code
RUN test -f /code/config.yml

# prepare apt-get
RUN apt-get -qq update > /dev/null

# install postfix
RUN apt-get -qq -y install mailutils  > /dev/null
RUN apt-get -qq -y install postfix rsyslog libsasl2-2 ca-certificates libsasl2-modules > /dev/null

# for testing smtplib-wrapper
RUN apt-get -qq -y install libyaml-dev > /dev/null

# for inspection
RUN apt-get -qq -y install vim-tiny screen tree > /dev/null
RUN ln -s /usr/bin/vim.tiny /usr/bin/vim

# python
RUN apt-get install python-pip python-virtualenv python-dev

# complete postfix config
RUN postmap /etc/postfix/sasl_passwd
RUN postmap /etc/postfix/canonical
RUN postmap /etc/postfix/generic
RUN ln -s /etc/hostname /etc/mailname

# prepare
RUN pip install pew
RUN pew new -d ENV2
RUN pew in ENV2 pip install PyYaml

# install
RUN pew in ENV2 python /code/setup.py install

# Run
WORKDIR /code
ENTRYPOINT pew in ENV2 python -m unittest TestMailer TestConfig

