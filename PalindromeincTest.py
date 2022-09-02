word = "minim"
def palindrome(string):
 string = string.lower()
 return string == string[::-1]
print(palindrome(word))


#Unittest

import unittest
from Palindrome import *

class TestArea(unittest.TestCase):
 def test_area(self):
 self.assertTrue(palindrome('minim'))
 self.assertTrue(palindrome('madam'))
 self.assertTrue(palindrome('racecar'))
 self.assertFalse(palindrome('sophie'))
 self.assertFalse(palindrome('kamara'))
 self.assertFalse(palindrome('scott'))
 
if __name__ == '__main__':
 unittest

