# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:26:55 2020

@author: erick
"""
import spacy
import random
import pickle
from spellchecker import SpellChecker
'''
artikels = {'NM': ['die', 'das', 'den', 'dem', 'einen', 'einem', 'einer', 'eine'],
            'NF': ['der', 'das', 'den', 'dem','einen', 'einem', 'einer', 'ein'],
            'NN': ['der', 'die', 'den', 'dem','einen', 'einem', 'einer', 'eine'],
            'AM': ['der', 'die', 'das', 'dem','ein', 'eine', 'einem', 'einer'],
            'AF': ['der', 'das', 'den', 'dem','einen', 'ein', 'einem', 'einer'],
            'AN': ['der', 'die', 'den', 'dem','einen', 'eine', 'einem', 'einer'],
            'DM': ['der', 'die', 'den', 'dem','einen', 'eine', 'einem', 'einer'],
            'DF': ['der', 'die', 'den', 'dem','einen', 'eine', 'einem', 'einer'],
            'DN': ['der', 'die', 'den', 'dem','einen', 'eine', 'einem', 'einer']
            }
'''
artikels = {'NM': ['der', 'ein'],
            'NF': ['die', 'eine'],
            'NN': ['das', 'ein'],
            'AM': ['den', 'einen'],
            'AF': ['die', 'eine'],
            'AN': ['das', 'ein'],
            'DM': ['dem', 'einem'],
            'DF': ['der', 'einer'],
            'DN': ['dem', 'einem']
            }


spell = SpellChecker(language='de')


def check_spell(doc):
    #SpellChecker
    words = [token.text for token in doc]
    misspelled = spell.unknown(words)
    misspelled
    
    errors = []
    
    if misspelled:
        for misspell in misspelled:
            correct = spell.correction(misspell)
            tip = spell.candidates(misspell)
            error = {'match': misspell,'correct': correct, 'tip': 'Você quis dizer "{}"?'.format(correct)}
            errors.append(error)
        
    return errors
        
def check_match(doc, matcher):
    sentences = []
    found_matches = matcher(doc)
    if found_matches:
        for item in found_matches:
            
            sentences.append(doc[item[1]:item[2]])
        return sentences
    return None

def kasus_error(match, kasus):
    for token in match:
        token = token.text.lower()
        for a in artikels[kasus]:
            if token == a:
                return False
    return True
    

def check_kasus(spans, worter):
    
    if not spans:
        return None
    artikel = None
    errors = []   
    
    for kasus, match in spans:
        
        if kasus == 'Nom':
            
            for token in match:
                wort = token.text.lower()
                if wort in worter:
                    artikel = worter[wort]['Gender']
                    
            if artikel == 'Das':
                if kasus_error(match,'NN'):
                    errors.append({'match':match, 'correct': 'Neutral', 'tip':'Deve-se declinar no Nominativo Neutro'})

            elif artikel == 'Die':
                if kasus_error(match,'NF'):
                    errors.append({'match':match, 'correct': 'Feminin', 'tip':'Deve-se declinar no Nominativo Feminino'})
                            
            elif artikel == 'Der':
                if kasus_error(match,'NM'):
                    errors.append({'match':match, 'correct': 'Masculin', 'tip':'Deve-se declinar no Nominativo Masculino'})
                            
            else:
                print('No Gender Found')
                
        elif kasus == 'Akk':
            
            for token in match:
                wort = token.text.lower()
                if wort in worter:
                    artikel = worter[wort]['Gender']
                    
            if artikel == 'Das':
                if kasus_error(match,'AN'):
                    errors.append({'match':match, 'correct': 'Neutral', 'tip':'Deve-se declinar no Acusativo Neutro'})

            elif artikel == 'Die':
                if kasus_error(match,'AF'):
                    errors.append({'match':match, 'correct': 'Feminin', 'tip':'Deve-se declinar no Acusativo Feminino'})
                            
            elif artikel == 'Der':
                if kasus_error(match,'AM'):
                    errors.append({'match':match, 'correct': 'Masculin', 'tip':'Deve-se declinar no Acusativo Masculino'})
                            
            else:
                print('No Gender Found')

        elif kasus == 'Dat':
            
            for token in match:
                wort = token.text.lower()
                if wort in worter:
                    artikel = worter[wort]['Gender']
                    
            if artikel == 'Das':
                if kasus_error(match,'DN'):
                    errors.append({'match':match, 'correct': 'Neutral', 'tip':'Deve-se declinar no Dativo Neutro'})

            elif artikel == 'Die':
                if kasus_error(match,'DF'):
                    errors.append({'match':match, 'correct': 'Feminin', 'tip':'Deve-se declinar no Dativo Feminino'})
                            
            elif artikel == 'Der':
                if kasus_error(match,'DM'):
                    errors.append({'match':match, 'correct': 'Masculin', 'tip':'Deve-se declinar no Dativo Masculino'})
                            
            else:
                print('No Gender Found')
        else:
            pass
                            
    if errors:
        return errors
    else:
        return None
       
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