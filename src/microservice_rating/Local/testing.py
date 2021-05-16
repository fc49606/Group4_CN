import unittest
import server as s

class testRating(unittest.TestCase):
    
    def teste1(self):
        #print(s.read('Jumanji'))
        self.assertEqual(s.read('Jumanji'), "3.7601626016260163") #Local

    def teste2(self):
        #print(s.read('Heat'))
        self.assertEqual(s.read('Heat'), "3.8700331125827815") #Local

if __name__ == '__main__':
    unittest.main()