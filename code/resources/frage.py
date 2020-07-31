from flask_restful import Resource, reqparse

from flask import json
from models.nlp import NLPModel
from fragen import get_answers
from models.antwort import AntwortModel
from models.bot import ChatBotModel
import datetime
import random
from fuzzywuzzy import fuzz

answers = get_answers()
nlp = NLPModel()
bot = ChatBotModel()

class Frage(Resource):

    parser = reqparse.RequestParser() #Condicoes de entrada
    parser.add_argument('num_frage',
        type=int,
        required=True,
        help="Este campo não pode ficar em branco"
    )
    parser.add_argument('antwort',
        type=str,
        required=True,
        help="Este campo não pode ficar em branco"
    )

    def get(self):

        frage = {'num_frage':None,
                 'frage': 'Hallo!'}

        return frage

    def post(self):

        data = self.parser.parse_args() #Validacao das condicoes de entrada

        num_frage = data['num_frage']

        nlp.setDoc(data['antwort'])
        errors = nlp.checkSatz(num_frage)

        response = {}
        response['antwort'] = data['antwort']

        if errors:
            success = False
            response['errors'] = errors
        else:
            success = True

        response['success'] = success

        date = datetime.datetime.now()
        response['date'] = date.strftime("%c")

        antwort = AntwortModel(num_frage, data['antwort'], success)


        try:
            antwort.save_to_db()
            print('Save to database successful')
        except Exception as e:
            return {'message': "An error occured while creating the store: {}".format(str(e))}, 500

        if errors:
            return response, 200

        if num_frage in answers:
            for answer in answers[num_frage]:
                ratio = fuzz.token_set_ratio(answer['element'],data['antwort'])
                if ratio == 100:
                    response['bot_antwort'] = {"result": answer['response'], "context": answer['context'], "patterns": "teste", "tag": "tagteste"}
                    break
            if 'bot_antwort' not in response:
                #answer = answers[num_frage][-1]
                response['bot_antwort'] = {"result": answer['response'], "context": answer['context'], "patterns": "teste", "tag": "tagteste"}
                
        else:
            response['bot_antwort'] = bot.chatbot_response(data['antwort'])

        return response, 200

class AntwortList(Resource):
    def get(self):
        return {'antworten': [antwort.json() for antwort in AntwortModel.find_all()]}