import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.text='Hi'

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())

if __name__=='__main__':
    unittest.main()
