# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 19:21:05 2020

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
    
    def checkSatz(self, id_frage=None):
        
        if id_frage is not None:
            self.matcher.add('Ex', self.patterns[id_frage])
        
        self.check_match()
        
        total_errors = []
        
        #Check Pattern
        if id_frage is not None:
            found = self.search_match('Ex')
            if not found:
                error = {'match': 'Padrão não encontrado', 'correct':'-','tip':'-'}
                total_errors.append(error)

        #Check Spelling
        errors = check_spell(self.doc)
        if errors:
            total_errors.extend(errors)
        
        #Check Kasus
        errors = check_kasus(self.found_matches, self.worter)
        if errors:
            total_errors.extend(errors) 
            
        return total_errors

      
    def docDetails(self):
        show_details(self.doc)
        
    def check_match(self):
        results = []
        found_matches = self.matcher(self.doc)
        if found_matches:
            for id_match, start, stop in found_matches:  
                string_id = self.nlp.vocab.strings[id_match]
                span = self.doc[start:stop]
                result = string_id, span
                results.append(result)
            self.found_matches = results
        else:
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
    