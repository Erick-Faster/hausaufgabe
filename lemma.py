# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:49:25 2020

@author: erick
"""

import spacy
custom_lookup = {'AAA':'Anonyme Affen Allianz','BBB':'Berliner Bauern Bund','CCC':'Chaos Chaoten Club'}

def change_lemma_property(doc):
    for token in doc:
        if (token.text in custom_lookup):
            token.lemma_ = custom_lookup[token.text]
    return doc

nlp = spacy.load('de_core_news_sm')

nlp.add_pipe(change_lemma_property, first=True)
text = 'Die AAA besiegt die BBB und den CCC unverdient.'
doc = nlp(text)
[print(x.lemma_) for x in doc]