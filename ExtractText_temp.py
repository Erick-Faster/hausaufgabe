# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 01:55:55 2020

@author: erick
"""

import pandas as pd

worter = pd.read_csv('worter.txt', encoding = 'utf-8')

palavras = worter.iloc[:,0].values
palavras = list(palavras)


words = {}
error = []

for palavra in palavras:
    wort = palavra.lstrip().rstrip().split()
    try:
        words[wort[4].lower()] = {'translate': wort[1], 'Gender': wort[3], 'Plural': wort[7], 'ORTH': wort[4]}
    except:
        error.append(palavra)
        print(palavra)
