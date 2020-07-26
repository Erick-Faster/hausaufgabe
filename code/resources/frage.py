from flask_restful import Resource, reqparse

from flask import json
from fragen import get_fragen
from models.nlp import NLPModel
from models.antwort import AntwortModel
from models.bot import ChatBotModel

import random

fragen = get_fragen()
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

        frage = {'num_frage':0,
                 'frage': fragen[0]}

        return frage

    def post(self):

        data = self.parser.parse_args() #Validacao das condicoes de entrada

        nlp.setDoc(data['antwort'])
        errors = nlp.checkSatz(data['num_frage'])

        response = {}
        response['antwort'] = data['antwort']

        if errors:
            success = False
            response['errors'] = errors
        else:
            success = True

        response['success'] = success

        antwort = AntwortModel(data['num_frage'], data['antwort'], success)

        try:
            antwort.save_to_db()
            print('Save to database successful')
        except Exception as e:
            return {'message': "An error occured while creating the store: {}".format(str(e))}, 500

        if errors:
            return response, 200

        response['bot_antwort'] = bot.chatbot_response(data['antwort'])


        return response, 200

class AntwortList(Resource):
    def get(self):
        return {'antworten': [antwort.json() for antwort in AntwortModel.find_all()]}