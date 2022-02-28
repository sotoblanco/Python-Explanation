# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 20:14:45 2022

@author: Pastor
"""

import unittest
import cap

class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')
        
        
    def test_multiple_words(self):
        text = "monty python"
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')
        
        
if __name__=='__main__':
    unittest.main()