# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 09:23:02 2020

@author: erick
"""

import nltk
from nltk.stem import WordNetLemmatizer
import pickle
import numpy as np

from keras.models import load_model
import json
import random

from logconfig import logger

class ChatBotModel:

    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()

        self.model = load_model('chatbot_model.h5')

        #Loading and Encoding Json
        with open('intents.json', encoding='utf-8') as fh:
            self.intents = json.load(fh)

        self.words = pickle.load(open('words.pkl', 'rb'))
        self.classes = pickle.load(open('classes.pkl','rb'))

    def clean_up_sentence(self, sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words

    def bow(self, sentence, words, show_details=True):
        sentence_words = self.clean_up_sentence(sentence)
        
        bag = [0]*len(words)
        for s in sentence_words:
            for i, w in enumerate(words):
                if w == s:
                    bag[i] = 1
                    #if show_details:
                    #   print("found in bag %s" %w)
        return(np.array(bag))

    def predict_class(self, sentence, model):
        p = self.bow(sentence, self.words, show_details=True)
        res = model.predict(np.array([p]))[0]
        ERROR_THRESHOLD = 0.75
        results = [[i,r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
        results.sort(key=lambda x: x[1], reverse=True)
        return_list = []
        for r in results:
            return_list.append({"intent": self.classes[r[0]], "probability": str(r[1])})

        if not return_list:
            return_list.append({"intent": "noanswer", "probability": str(0)})
        return return_list

    def getResponse(self, ints, intents_json):
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if(i['tag'] == tag):
                result = random.choice(i['responses'])
                context = i['context']
                patterns = i['patterns']
                tag = i['tag']
                break

        res = {"result": result, "context": context, "patterns": patterns, "tag": tag}
        return res

    def chatbot_response(self, text):
        logger.info('Predicting answers...')
        ints = self.predict_class(text, self.model)
        res = self.getResponse(ints, self.intents)
        logger.info('Prediction complete!')
        return res

