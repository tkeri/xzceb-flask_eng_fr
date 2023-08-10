'''
Unit tests
'''

import unittest

from translator import english_to_french, french_to_english

class TranslatorEnglishTest(unittest.TestCase):
    '''
    Translator english tester class
    '''
    def test_english_to_french_equal(self):
        '''
        English to french unit test.
        '''
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    def test_english_to_french_not_equal(self):
        '''
        English to french not equal unit test.
        '''
        self.assertNotEqual(english_to_french("Hello"), "Hello")

class TranslatorFrenchTest(unittest.TestCase):
    '''
    Translator french tester class
    '''
    def test_french_to_english_equal(self):
        '''
        French to english equal unit test.
        '''
        self.assertEqual(french_to_english("Bonjour"), "Hello")
    def test_french_to_english_not_equal(self):
        '''
        French to english not equal unit test.
        '''
        self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

if __name__ == '__main__':
    unittest.main()
