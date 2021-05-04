import unittest
import server as s

class testBudget(unittest.TestCase):
    
    def jumanjiBudget(self):
        self.assertTrue(s.read('Jumanji', 1995), '{"result": [{"budget": "65000000"}]}')

    def Grumpier_Old_MenBudget(self):
        self.assertTrue(s.read('Grumpier Old Men', 1995), '{"result": [{"budget": "0"}]}')

if __name__ == '__main__':
    unittest.main()