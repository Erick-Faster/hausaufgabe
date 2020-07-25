from flask_restful import Resource, reqparse

from flask import json
from models.bot import ChatBotModel

import random

bot = ChatBotModel()

class Neural(Resource):

    parser = reqparse.RequestParser() #Condicoes de entrada

    parser.add_argument('antwort',
        type=str,
        required=True,
        help="Este campo não pode ficar em branco"
    )

    def get(self):
        
        pass

    def post(self):

        data = self.parser.parse_args() #Validacao das condicoes de entrada

        response = {"response": bot.chatbot_response(data['antwort'])}

        return response