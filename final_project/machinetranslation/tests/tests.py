import unittest

from translator import english_to_french, french_to_english

class TranslatorEnglishTest(unittest.TestCase):
    def test_english_to_french_equal(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_english_to_french_not_equal(self):
        self.assertNotEqual(english_to_french("Hello"), "Hello")

class TranslatorFrenchTest(unittest.TestCase):
    def test_french_to_english_equal(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test_french_to_english_not_equal(self):
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

if __name__ == '__main__':
    unittest.main()
