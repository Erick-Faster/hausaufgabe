# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:49:25 2020

@author: erick
"""

import spacy
import time
import string

#custom_lookup = {'aaa':'Anonyme Affen Allianz','BBB':'Berliner Bauern Bund','CCC':'Chaos Chaoten Club'}


#sentences = base.iloc[:1000,1].values
#sentences = list(sentences)

custom_lookup = dic_list.copy()

def change_lemma_property(doc):
    for token in doc:
        if (token.text in custom_lookup):
            token.lemma_ = custom_lookup[token.text]
    return doc

nlp = spacy.load('pt_core_news_sm', disable = ['ner', 'tagger', 'parser', 'textcat'])
punctuations = string.punctuation
stop_words = spacy.lang.pt.stop_words.STOP_WORDS

nlp.add_pipe(change_lemma_property, first=True)

begin = time.time()

result2 = []
for sentence in sentences:
    sentence = sentence.lower().lstrip().rstrip()
    doc = nlp(sentence)
    list = [token.lemma_ for token in doc if not (token.is_stop or #Elimina stop words
                                                   token.is_punct or #Elimina pontuacoes
                                                   token.is_space)]
    list = ' '.join([str(element) for element in list])
    result2.append(list)
    #[print(x.lemma_) for x in doc]
    
    
end = time.time()
print("%.2fs"%(end-begin))

#test
sentence = "BD ABERTURA aaa PHASEAL INJECTOR LUER LOCK (N35). INJECTOR N35. INJECTOR LUER LOCK N35: Dispositivo de transferencia de medicamentos que se acopla a uma seringa descartavel, um a adaptador de infusao ou conector com conexao Luer Lok padrao. Dimensoes: 71"
print(sentence)
sentence = sentence.lower().lstrip().rstrip()
doc = nlp(sentence)
print(doc.text)

print(nlp.pipe_names)

##########

import spacy
custom_lookup = {'AAA':'Anonyme Affen Allianz','BBB':'Berliner Bauern Bund','CCC':'Chaos Chaoten Club'}

def change_lemma_property(doc):
    for token in doc:
        if (token.text in custom_lookup):
            token.lemma_ = custom_lookup[token.text]
    return doc

nlp = spacy.load('de_core_news_sm')

nlp.add_pipe(change_lemma_property, first=True)
text = 'Die AAA besiegt die BBB und den CCC unverdient.'
doc = nlp(text)
doc.text
list = [x.lemma_ for x in doc]

result == result2




