import unittest

from translator import english_to_french, french_to_english

class TestEngToFr(unittest.TestCase):
    def test_e2f(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertIsNotNone(english_to_french('hello'))

class TestFrToEng(unittest.TestCase):
    def test_f2e(self):    
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertIsNotNone(french_to_english('bonjour'))

unittest.main()