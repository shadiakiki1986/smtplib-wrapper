# https://docs.python.org/2/library/unittest.html#basic-example

import unittest, os
import yaml
# import pprint

class TestConfig(unittest.TestCase):

  def test_readable(self):
    cf = "config.yml"
    self.assertTrue(os.path.isfile(cf))
    c0 = yaml.safe_load(open(cf))
    # pp = pprint.PrettyPrinter(indent=4)
    # pp.pprint(c0)

if __name__ == '__main__':
    unittest.main()
