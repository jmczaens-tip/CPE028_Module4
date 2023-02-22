import unittest

class TestInteger(unittest.TestCase):
    def test_int_diff_val(self):
        x = 10
        y = 10
        self.assertIsNot(x,y)

    def test_int_same_val(self):
        x = 10
        y = 20
        self.assertIs(x,y)
if __name__=='__main__':
    unittest.main()