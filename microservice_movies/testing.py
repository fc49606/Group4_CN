import unittest
import server as s

class testBudget(unittest.TestCase):
    
    def teste1(self):
        self.assertEqual(s.read("1972", "netflix"), [('Bawarchi',)])

    def teste2(self):
        self.assertEqual(s.read("1919", "prime_video"), [('A Romance of Happy Valley',)])

    def teste3(self):
        self.assertEqual(s.read("1988", "hulu"), [('Grave of the Fireflies',), ('Akira',), ('Hellbound: Hellraiser II',), ('The Boost',)])

    def teste4(self):
        self.assertEqual(s.read("2020", "disneyplus"), [('Onward',), ('Timmy Failure: Mistakes Were Made',), ('Lamp Life',), ('In the Footsteps of Elephant',), ('Diving with Dolphins',), ('Penguins: Life on the Edge',)])

    def teste5(self):
        self.assertNotEqual(s.read("2015", "xpto"), [('Bawarchi',)])

if __name__ == '__main__':
    unittest.main()