# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 19:21:10 2020

@author: erick
"""

def get_fragen():
    
    fragen = {}
    
    fragen[0] = 'Hallo!'
    fragen[1] = 'Wie heissen Sie?'
    fragen[2] = 'Wo wohnen Sie?'
    fragen[3] = 'Was mögen Sie?'
    
    return fragen

def get_patterns():
    
    patterns = {}
    
    '''
    patterns[0] = [[{'LOWER': 'hallo'}],      
        [{'LOWER': 'guten'},{'LOWER':'tag'}],
        [{'LOWER': 'guten'},{'LOWER':'morgen'}],
        [{'LOWER': 'gute'},{'LOWER':'nacht'}],
        [{'LOWER': 'guten'}, {'LOWER':'abend'}]]
    '''
    patterns[0] = [[{'LOWER': 'es'},{'LOWER': 'geht'}, {'LOWER': 'mir'}], 
        [{'LOWER': 'mir'},{'LOWER':'geht'}, {'LOWER':'es'}]]

    patterns[1] = [[{'LOWER': 'ich'}, {'LOWER':'bin'}, {'POS': 'PROPN'}],      
        [{'LOWER': 'ich'},{'LOWER':'heisse'}, {'POS': 'PROPN'}],
        [{'LOWER': 'mein'}, {'LOWER':'name'}, {'LOWER':'ist'}, {'POS': 'PROPN'}]]
    patterns[2] = [[{'LOWER': 'ich'}, {'LOWER':'wohne'}, {'LOWER':'in'}, {'ENT_TYPE':'LOC','OP':'+'}]]
    patterns[3] = [[{'LOWER': 'ich'}, {'LOWER':'komme'}, {'LOWER':'aus'}, {'ENT_TYPE':'LOC','OP':'+'}]]
    patterns[4] = [[{'LOWER': 'ich'}, {'LOWER':'mag'}, {'DEP':'oa'}]]
    
    
    return patterns