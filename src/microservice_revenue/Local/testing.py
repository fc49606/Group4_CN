import unittest
import server as s

class testRevenue(unittest.TestCase):
    
    def teste1(self):
        self.assertEqual(s.read('Waiting to Exhale', '1995'), "81452156") #Local

    def teste2(self):
        self.assertEqual(s.read('Tom and Huck', '1995'), "0") #Local

if __name__ == '__main__':
    unittest.main()