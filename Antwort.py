# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 02:49:12 2020

@author: erick
"""

import spacy
import time
import random

from tools import check_spell, check_kasus, save_pickle, load_pickle
from tools import show_ents, show_details

from fragen import get_fragen, get_patterns

from spacy.matcher import Matcher

import pandas as pd

class NLP:
    def __init__(self):
        
        #SpaCy Initializers
        self.nlp = spacy.load('de_core_news_sm')
        self.doc = self.nlp('Ich schicke meiner Mutter ein Geschenk')
        self.matcher = Matcher(self.nlp.vocab)
        
        #Dictionaries
        self.worter = load_pickle("Worter.p")
        
        #Patterns
        self.patterns = get_patterns()
        self.pattern_akk = [[{'TAG': 'ART'}, {'TAG':'ADJA','OP':'*'}, {'DEP': 'oa'}]]
        self.pattern_nom = [[{'TAG': 'ART'}, {'TAG':'ADJA','OP':'*'}, {'DEP': 'sb'}]]
        self.pattern_dat = [[{'TAG': 'ART'}, {'TAG':'ADJA','OP':'*'}, {'DEP': 'da'}]]

        #Add patterns

        self.matcher.add('Akk',self.pattern_akk)        
        self.matcher.add('Nom',self.pattern_nom)        
        self.matcher.add('Dat',self.pattern_dat)        
        
        #Variables
        self.found_matches = None

    def setDoc(self, string):
        self.doc = self.nlp(string)
    
    def checkSatz(self, frage):
        self.matcher.add('Ex', self.patterns[frage])
        self.check_match()
        
        
        #Check Pattern
        print("Check Pattern:")
        found = self.search_match('Ex')
        if found:
            print('Correct Match')
            print(found)
        else:
            print('Wrong Match')
        
        #Check Kasus
        print("Check Kasus:")
        #spans = self.search_match('Akk')
        errors = check_kasus(self.found_matches, self.worter)
        if errors:
            print("Found Errors")
            print(errors)
        else:
            print("Correct Kasus")
            
        #Check Spelling
        print("Check Spelling:")
        check_spell(self.doc)
        print('\n')

      
    def docDetails(self):
        show_details(self.doc)
        
    def check_match(self):
        results = []
        found_matches = self.matcher(self.doc)
        if found_matches:
            print(found_matches)
            for id_match, start, stop in found_matches:  
                string_id = self.nlp.vocab.strings[id_match]
                span = self.doc[start:stop]
                result = string_id, span
                results.append(result)
            self.found_matches = results
            print(self.found_matches)
        else:
            print('No Match')
            self.found_matches = None 
        
    def search_match(self,id_string):
        
        found = []
        if self.found_matches:
            for id_match, match in self.found_matches:
                if id_match == id_string:
                    found.append(match)
            if found:
                print("%d Matches with id_string %s found"%(len(found),id_string))
                return found
            print("No Matches with id_string %s found" %id_string)
            return None
        else:
            print('No Match Found')
            return None
                    

object_nlp = NLP()

begin = time.time()

object_nlp.setDoc(u'Ich sehe die Tisch. Ich sehe den Banane. Ich sehe den Haus. Die Banane und das Haus. Ich bin ein Hund. Die Mutter schickt der tollen Mutter ein tolles Geschenk. Ich sehe ein blaues Haus. Mein Name ist Eric. Der rote Apfel. Die Banane. Der Apfel')
object_nlp.docDetails()
object_nlp.checkSatz(0)

finish = time.time()
print("%.2fs"% (finish-begin))  
        

#Generate Question

#fragen = get_fragen()
#patterns = get_patterns()

#dice = random.randint(0,1)
#matcher.add('Ex', patterns[2])
#print(fragen[1])




#Details
#show_details(doc)

#show_ents(doc)

#Checks

#print("Check Patterns:")
#check_match(doc, matcher)
#print('\n')



#print("Check Kasus")
#spans = check_match(doc,matcherNomen)
#check_kasus(spans, worter)
#print('\n')






  


#show_details(doc)

#doc = nlp('Ich schicke meiner Mutter ein Geschenk')

