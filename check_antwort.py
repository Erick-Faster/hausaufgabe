# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:26:55 2020

@author: erick
"""

from spellchecker import SpellChecker

spell = SpellChecker(language='de') 

def check_spell(doc):
    #SpellChecker
    words = [token.text for token in doc]
    misspelled = spell.unknown(words)
    
    
    if misspelled:
        for word in misspelled:
            print(spell.correction(word))
            print(spell.candidates(word))    
    else:    
        print('Correct Spelling')    