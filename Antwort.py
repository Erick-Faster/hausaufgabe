# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 02:49:12 2020

@author: erick
"""

from nlp import NLP
import time                

object_nlp = NLP()

begin = time.time()

object_nlp.setDoc(u'Ich sehe die Tisch. Ich sehe den Banane. Ich sehe den Haus. Die Banane und das Haus. Ich bin ein Hund. Die Mutter schickt der tollen Mutter ein tolles Geschenk. Ich sehe ein blaues Haus. Der rote Apfel. Die Banane. Der Apfel')
object_nlp.docDetails()

errors = object_nlp.checkSatz(0)

finish = time.time()
print("%.2fs"% (finish-begin))  

print(errors)
        

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

