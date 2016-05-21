# Description: send email through FFA SMTP

import smtplib, yaml
import os
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import logging
from subprocess import Popen, PIPE

logger = logging.getLogger('RiskReconMargin')

# From stack overflow (lost url)
#   config2 = yaml.safe_load(open('config.yml'))
def sendemailCore(config2,sender,receivers,message):
  assert "server" in config2["smtp"]
  server = smtplib.SMTP(config2["smtp"]["server"],587)
  logger.info("Email server: "+config2["smtp"]["server"])
  server.starttls()
  server.ehlo()
  user = config2["smtp"]["user"] if "user" in config2["smtp"] else sender
  server.login(user, config2["smtp"]["pwd"])
  server.sendmail(sender, receivers, message)         
  logger.info("Successfully sent email")
  server.close()

# From stack overflow (lost url)
#   config2 = yaml.safe_load(open('config.yml'))
def sendemail1(config2,receivers,subject,body):
  assert "smtp" in config2
  assert "email" in config2["smtp"]
  assert isinstance(receivers, list)
  sender = config2["smtp"]["email"]

  message = """From: Shadi Akiki <%s>
  To: Shadi Akiki <%s>
  Subject: %s
  mime-version: 1.0
  content-type: text/html

  %s
  """ % (sender, sender, subject, body)
  sendemailCore(config2,sender,receivers,message)

# http://stackoverflow.com/a/3363254/4126114
#   config2 = yaml.safe_load(open('config.yml'))
# If the config uses Gmail smtp, this can be used with useLocalSendmail=False
# If the config uses FFA SMTP, need to use useLocalSendmail=True
#    because the FFA SMTP server uses NTLM, which I couldn't figure out with python's smtplib
def sendemail2(config2,receivers,subject,body,files=None,useLocalSendmail=False):
  assert isinstance(receivers, list)
  if isinstance(files,list):
    if len(files)==0:
      files=None
  if files is not None: assert isinstance(files,list)
  assert "smtp" in config2
  assert "email" in config2["smtp"]

  sender = config2["smtp"]["email"]

  msg = MIMEMultipart()
  msg['From']=sender
  msg['To']=email.utils.COMMASPACE.join(receivers)
  msg['Date']=email.utils.formatdate(localtime=True)
  msg['Subject']=subject
  msg.attach(MIMEText(body,'html'))

  for f in files or []:
      with open(f, "rb") as fil:
          msg.attach(MIMEApplication(
              fil.read(),
              Content_Disposition='attachment; filename="%s"' % os.path.basename(f),
              Name=os.path.basename(f)
          ))

  message = msg.as_string().encode('utf-8')
  if not useLocalSendmail:
    sendemailCore(config2,sender,receivers,message)
  else:
    # http://stackoverflow.com/a/74084/4126114
    sendmailPath="/usr/sbin/sendmail"
    if not os.path.exists(sendmailPath): raise ValueError("/usr/sbin/sendmail not found")
    p = Popen([sendmailPath,"-t","-oi"], stdin=PIPE)
    stdout,stderr = p.communicate(message)
    if stderr: raise ValueError('Error: '+stderr)
    if stdout: raise ValueError( "Out: "+stdout)
