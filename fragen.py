# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:21:10 2020

@author: erick
"""

def get_fragen():
    
    fragen = {}
    
    fragen[0] = 'Wie heissen Sie?'
    fragen[1] = 'Wo arbeiten Sie?'
    fragen[2] = 'Was mögen Sie?'
    
    return fragen

def get_patterns():
    
    patterns = {}
    
    patterns[0] = [[{'LOWER': 'ich'}, {'LOWER':'bin'}, {'POS': 'PROPN'}],      
        [{'LOWER': 'ich'},{'LOWER':'heisse'}, {'POS': 'PROPN'}],
        [{'LOWER': 'mein'}, {'LOWER':'name'}, {'LOWER':'ist'}, {'POS': 'PROPN'}]]
    patterns[1] = [[{'LOWER': 'ich'}, {'LOWER':'wohne'}, {'LOWER':'in'}, {'ENT_TYPE':'LOC','OP':'+'}]]
    patterns[2] = [[{'LOWER': 'ich'}, {'LOWER':'mag'}, {'DEP':'oa'}]]
    
    return patterns