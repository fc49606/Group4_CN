import unittest
import server as s

class testBudget(unittest.TestCase):
    
    def teste1(self):
        self.assertEqual(s.read('Jumanji', '1995'), "65000000")

    def teste2(self):
        self.assertEqual(s.read('Grumpier Old Men', '1995'), "0")

if __name__ == '__main__':
    unittest.main()