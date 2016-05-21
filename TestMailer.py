# https://docs.python.org/2/library/unittest.html#basic-example

import unittest, os
import Mailer
import tempfile
import yaml

c0 = yaml.safe_load(open("config.yml"))
class TestMailer(unittest.TestCase):
  rcpt1=c0["smtp"]["test_rcpt1"] # "s.akiki@ffaprivatebank.com"
  rcpt2=c0["smtp"]["test_rcpt2"] # "shadiakiki1986@gmail.com"

  @unittest.skip('SMTPException: STARTTLS extension not supported by server')
  def test_sendemail1(self):
    Mailer.sendemail1(c0,[self.rcpt1],"Test 1","Empty")

  @unittest.skip('SMTPException: STARTTLS extension not supported by server')
  def test_sendemail2_1(self):
    Mailer.sendemail2(c0,[self.rcpt1],"Test 2","Empty")

  @unittest.skip('SMTPException: STARTTLS extension not supported by server')
  def test_sendemail2_2(self):
    with tempfile.NamedTemporaryFile() as tf:
      with open(tf.name, 'w') as wf:
        wf.write("Test attachment")
        wf.close()
        Mailer.sendemail2(c0,[self.rcpt1],"Test 3","Should have attachment",[tf.name])

  def test_sendemail2_3(self):
    with tempfile.NamedTemporaryFile() as tf:
      with open(tf.name, 'w') as wf:
        wf.write("Test attachment")
        wf.close()
        Mailer.sendemail2(c0,[self.rcpt1,self.rcpt2],"Test 3","Should have attachment",[tf.name],True)

if __name__ == '__main__':
    unittest.main()
