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

from logconfig import logger

class NLPModel:

    def __init__(self):

        logger.info('Initializing NLP configuration...')
        
        #SpaCy Initializers
        self.antwort = 'None'
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

        logger.info('NLP configuration complete!')

    def setDoc(self, string):
        self.doc = self.nlp(string)
    
    def checkSatz(self, id_frage=None):

        logger.info('Checking errors and patterns...')
        
        if id_frage is not None:
            self.matcher.add('Ex', self.patterns[id_frage])
        
        self.check_match()
        
        total_errors = []
        
        #Check Pattern
        if id_frage is not None:
            found = self.search_match('Ex')
            if not found:
                error = {'match': 'Acho que essa resposta não fez muito sentido...', 'correct':'-','tip':'Se quiser, pode tentar de novo =D'}
                total_errors.append(error)
            self.matcher.remove('Ex')

        #Check Spelling
        errors = check_spell(self.doc)
        if errors:
            total_errors.extend(errors)
        
        #Check Kasus
        errors = check_kasus(self.found_matches, self.worter)
        if errors:
            total_errors.extend(errors)

        logger.info('Errors and patterns checked!') 
            
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
                logger.info("%d Matches with id_string %s found"%(len(found),id_string))
                return found
            return None
        else:
            logger.info("No Match Found")
            return None

    def text_structure(self):
        structure = {"ENT": [], "POS": [], "TAG": [], "DEP": [], "TEXT": []}
        
        if self.doc.ents:
            for ent in self.doc.ents:

                ent_add = {ent.label_: ent.text, "start": ent.start, "end": ent.end}
                structure["ENT"].append(ent_add)
        
        for token in self.doc:

            pos = token.pos_, token.i
            structure["POS"].append(pos)

            tag = token.tag_, token.i
            structure["TAG"].append(tag)

            dep = token.dep_, token.i
            structure["DEP"].append(dep)
            
            text = token.text, token.i
            structure["TEXT"].append(text)     
        
        print(structure)
        return structure

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self, antwort):
        to_db = {id}
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self, antwort):
        db.session.delete()
        db.session.commit()
    