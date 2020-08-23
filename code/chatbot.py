# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 08:44:19 2020

@author: erick
"""

import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random
#nltk.download('punkt') #para rodas tokenizze
#nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
words= []
classes = []
documents = []
ignore_words = ['?', '!']

data_file = open('intents.json').read()
intents = json.loads(data_file)

for intent in intents['intents']:
    for pattern in intent['patterns']:
        
        #Tokenizar cada palavra
        w = nltk.word_tokenize(pattern)
        
        #Add palavra na lista
        words.extend(w)
        
        #Documentar com tag
        documents.append((w,intent['tag']))
        
        #Add na lista de classes
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
            
#Lemmatizar, lower e remover duplicadas            
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]

words = sorted(list(set(words)))
classes = sorted(list(set(classes)))
print(len(documents), "documents")
print(len(classes), "classes", classes)
print(len(words), "unique lemmatized words", words)

pickle.dump(words,open('words.pkl', 'wb'))
pickle.dump(classes,open('classes.pkl','wb'))

training = []
output_empty = [0] * len(classes) #lista vazia

for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        training.append([bag, output_row])

random.shuffle(training)
training = np.array(training)
train_x = list(training[:,0])
train_y = list(training[:,1])

'''
from keras.layers import Embedding, LSTM, SpatialDropout1D
model = Sequential()
model.add(Embedding(5000, 50, input_length=(len(train_x[0]))))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(50, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(len(train_y[0]), activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='nadam', metrics=['accuracy'])
print(model.summary())

history = model.fit(np.array(train_x),
                    np.array(train_y),
                    epochs=30,
                    batch_size=32,
                    validation_split=0.1)
'''

model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(np.array(train_x), np.array(train_y), epochs=100, batch_size=4, verbose=1)


model.save('chatbot_model.h5', hist)

