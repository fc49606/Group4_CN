import unittest
import server as s

class testBudget(unittest.TestCase):
    
    def jumanjiBudget(self):
        self.assertTrue(s.read('Jumanji'), "{\"result\": [{\"avg\": \"3.7601626016260163\"}]}")

    def Grumpier_Old_MenBudget(self):
        self.assertTrue(s.read('Heat'), "{\"result\": [{\"avg\": \"3.8700331125827815\"}]}")

if __name__ == '__main__':
    unittest.main()