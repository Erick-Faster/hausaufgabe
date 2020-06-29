# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 02:49:12 2020

@author: erick
"""

import spacy
from spellchecker import SpellChecker 
from spacy.matcher import Matcher
import time
import pickle

import pandas as pd

def save_pickle(filename, objeto):
    outfile = open(filename,'wb')
    pickle.dump(objeto,outfile)
    outfile.close()
    
def load_pickle(filename):
    infile = open(filename,'rb')
    objeto = pickle.load(infile)
    infile.close()
    return objeto
    
#Carregar Dicionario de Substantivos
worter = load_pickle("Worter.p")

#Configuration
nlp = spacy.load('de_core_news_sm')
matcher = Matcher(nlp.vocab)
spell = SpellChecker(language='de')

#Patterns
patterns = [[{'LOWER': 'ich'}, {'LOWER':'bin'}, {'POS': 'PROPN'}],
            [{'LOWER': 'ich'},{'LOWER':'heisse'}, {'POS': 'PROPN'}],
            [{'LOWER': 'mein'}, {'LOWER':'name'}, {'LOWER':'ist'}, {'POS': 'PROPN'}]]
matcher.add('Ex1', patterns)

#Inputs
string = u'Ich heisse Eric. Mein Name ist Eric. Ich bin Eric. Ich schicke meiner Mutter ein Geschenk'

begin = time.time()

#Variables
doc = nlp(string)

found_matches = matcher(doc)
if found_matches:
    print('Correct Match')
    print(found_matches)
else:
    print('Incorrect Match')


#Spacy
print("\n")
for token in doc:
    print(f'{token.text:{12}} {token.pos_:{6}} {spacy.explain(token.pos_):{15}} {token.tag_:{6}} {spacy.explain(token.tag_):{40}} {token.dep_:{6}} {spacy.explain(token.dep_)}')
print("\n")

#SpellChecker
words = [token.text for token in doc]
misspelled = spell.unknown(words)


if misspelled:
    for word in misspelled:
        print(spell.correction(word))
        print(spell.candidates(word))    
else:    
    print('Correct Spelling')

finish = time.time()
print("%.2fs"% (finish-begin))    




