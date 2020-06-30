# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:26:55 2020

@author: erick
"""
import spacy
import random
import pickle
from spellchecker import SpellChecker

artikels = {'NM': ['die', 'das', 'eine'],
            'NF': ['der', 'das', 'ein'],
            'AM': ['der', 'die', 'das', 'ein', 'eine'],
            'AF': ['der', 'das', 'den', 'einen', 'ein'],
            'AN': ['der', 'die', 'den', 'einen', 'eine']}


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
        
def check_match(doc, matcher):
    sentences = []
    found_matches = matcher(doc)
    if found_matches:
        print('Correct Match')
        print(found_matches)
        for item in found_matches:
            sentences.append(doc[item[1]:item[2]])
        return sentences
    else:
        print('Incorrect Match')
        return None

def check_kasus(spans, worter):       
    for match in spans:
        for token in match:
            wort = token.text.lower()
            if wort in worter:
                artikel = worter[wort]['Gender']
                
        if artikel == 'Das':
            for token in match:
                for a in artikels['AN']:
                    if token.text == a:
                        print("Wrong Gender: %s"%token.text)
       
def save_pickle(filename, objeto):
    outfile = open(filename,'wb')
    pickle.dump(objeto,outfile)
    outfile.close()
    
def load_pickle(filename):
    infile = open(filename,'rb')
    objeto = pickle.load(infile)
    infile.close()
    return objeto

def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))
    else:
        print('No named entities found.')
        
def show_details(doc):
    print("\n")
    for token in doc:
        print(f'{token.text:{12}} {token.pos_:{6}} {spacy.explain(token.pos_):{15}} {token.tag_:{6}} {spacy.explain(token.tag_):{40}} {token.dep_:{6}} {spacy.explain(token.dep_)}')
    print("\n")