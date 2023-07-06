import unittest
from translator import english_tofrench, french_toenglish

class TestEngToFr(unittest.TestCase):
    '''Class for function english_tofrench'''
    def test1(self):
        '''Method for testing with input and expected output'''
        self.assertEqual(english_tofrench('Hello'), 'Bonjour')

class TestFrToEng(unittest.TestCase):
    '''Test for function french_toenglish'''
    def test1(self):
        '''Method for testing with input and expected output'''
        self.assertEqual(french_toenglish('Bonjour'), 'Hello')

if __name__ == '__main__':
    unittest.main()


# disabling:
# C0304: Trailing newlines (trailing-newlines)
# pylint: disable=C0304
