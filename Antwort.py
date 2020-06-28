# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 02:49:12 2020

@author: erick
"""

import spacy
from spellchecker import SpellChecker 

#Configuration
nlp = spacy.load('de_core_news_sm')
spell = SpellChecker(language='de')

#Inputs
string = u'Ich heisse Gabriel'
richtig = u"Ich heisse PROPN".split()

#Variables
doc = nlp(string)
words = []
antwort = []

#Spacy
for token in doc:
    print(f'{token.text:{12}} {token.pos_:{6}} {spacy.explain(token.pos_):{14}} {token.dep_:{6}} {spacy.explain(token.dep_)}')
    if token.pos_ == 'PROPN':
        antwort.append('PROPN')
    else:
        antwort.append(token.text)
    words.append(token.text)

misspelled = spell.unknown(words)

#SpellChecker
if len(misspelled) == 0:
    print('Correct')

for word in misspelled:
    print(spell.correction(word))
    print(spell.candidates(word))
 
if antwort == richtig:
    print('Resposta Correta')
else:
    print('Resposta Errada')
    


 



