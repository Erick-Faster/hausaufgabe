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
    patterns[5] = [[{'LOWER': 'ich'}, {'LOWER':'lerne'}, {'DEP':'mo', 'OP': '?'}, {'DEP':'oa'}]]
    
    return patterns

def get_answers():

    answers = {}

    answers[0] = [{'element': 'gut', 'response': "Toll! Woher kommen Sie?", 'context': 3},
                 {'element': 'prima', 'response': "Wo Wohnen Sie?", 'context': 2},
                 {'element': '', 'response': "Toll!", 'context': None}] 

    answers[1] = [{'element': 'Bolsonaro', 'response': "Ach so?? Du Arschloch! Fick dich!", 'context': None},
                 {'element': 'Lula', 'response': "Ich liebe dich <3 ?", 'context': None},
                 {'element': '', 'response': "Du hast ein schöner Name! Schön, Sie kennenzulernen!", 'context': None}]   

    answers[2] = [{'element': 'São Paulo', 'response': "São Paulo? Das ist eine sehr große Stadt", 'context': None},
                 {'element': 'Berlin', 'response': "Ich möchte Berlin kennenlernen! ><", 'context': None},
                 {'element': '', 'response': "Hm... diese Stadt kenne ich nicht...", 'context': None}]   

    answers[3] = [{'element': 'Brasilien', 'response': "Brasilien ist wunderbar", 'context': None},
                 {'element': 'Deutschland', 'response': "Deutschland ist toll", 'context': None},
                 {'element': '', 'response': "Das ist ein tolles Land!", 'context': None}]

    answers[4] = [{'element': 'Pizza', 'response': "Pizza ist wunderbar", 'context': None},
                 {'element': 'Persona', 'response': "ICH MAG AUCH PERSONA!!", 'context': None},
                 {'element': '', 'response': "Hmm...", 'context': None}]

    answers[5] = [{'element': 'Deutsch', 'response': "Deutsch ist die beste Sprache der Welt! Das gefällt mir wirklich sehr! Mögen Sie auch Deutsch?", 'context': 4},
                 {'element': 'Spanisch', 'response': "Mir gefällt Spanisch, aber ich lerne lieber Portugiesisch! Mögen Sie auch Portugiesisch?", 'context': 4},
                 {'element': '', 'response': "Das ist eine tolle Sprache zu lernen!", 'context': None}]

    return answers