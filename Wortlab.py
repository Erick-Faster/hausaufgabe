# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 02:49:12 2020

@author: erick
"""

from nlp import NLP
import time                

object_nlp = NLP()

begin = time.time()

string = u'Ich bin am 26.12.1993 geboren'
object_nlp.setDoc(string)

object_nlp.docDetails()

#dsobject_nlp.docDetails()

errors = object_nlp.checkSatz(2)

finish = time.time()
#print("%.2fs"% (finish-begin))  


#print(f'Frase: {object_nlp.doc}\n')
for error in errors:
    print(f'Erro: {error["match"]}')
    print(f'Correção: {error["tip"]}\n')
        

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






  




#doc = nlp('Ich schicke meiner Mutter ein Geschenk')

