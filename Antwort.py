# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 02:49:12 2020

@author: erick
"""

import spacy
import time
import random

from tools import check_spell, check_match, check_kasus, save_pickle, load_pickle
from tools import show_ents, show_details

from fragen import get_fragen, get_patterns

from spacy.matcher import Matcher

import pandas as pd

string = u'Ich wohne in Santo Andre. Ich mag Pizza. Ich sehe die Haus. Ich schicke meiner Mutter eine tolles Geschenk'
    
#Carregar Dicionario de Substantivos
worter = load_pickle("Worter.p")

#Configuration
nlp = spacy.load('de_core_news_sm')
doc = nlp(string)
matcher = Matcher(nlp.vocab)
matcherNomen = Matcher(nlp.vocab)

pattern = [[{'TAG': 'ART'}, {'TAG':'ADJA','OP':'*'}, {'DEP': 'oa'}]]
matcherNomen.add('Nomen', pattern)

#Generate Question
fragen = get_fragen()
patterns = get_patterns()

dice = random.randint(0,1)
matcher.add('Ex', patterns[2])
print(fragen[2])


begin = time.time()

#Details
show_details(doc)
show_ents(doc)

#Checks

print("Check Patterns:")
check_match(doc, matcher)
print('\n')

print("Check Spelling:")
check_spell(doc)
print('\n')

print("Check Kasus")
spans = check_match(doc,matcherNomen)
check_kasus(spans, worter)
print('\n')






finish = time.time()
print("%.2fs"% (finish-begin))    


show_details(nlp('Ich gehe. Du gehst. Er geht. Sie geht, Es geht. Wir gehen. Ihr geht. sie gehen. Sie gehen'))

