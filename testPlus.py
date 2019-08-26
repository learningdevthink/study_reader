import unittest

class TestPlus(unittest.TestCase):
    def test_one_plus_one(self):
        def plus_num(num, num2):
            return num + num2

        self.assertEqual(plus_num(1, 1), 1)
    
if __name__ == '__main__':  
    unittest.main()