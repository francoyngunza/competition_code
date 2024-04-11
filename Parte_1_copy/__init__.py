import random
from otree.api import *
import re

class C(BaseConstants):
    NAME_IN_URL = 'parte_1_copy'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    multiplicador = 5

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    columna_1 = models.BooleanField(initial=False)
    columna_2 = models.BooleanField(initial=False)
    columna_3 = models.BooleanField(initial=False)

#Pages  
class Pagina_1(Page):
    form_model = 'player'
    form_fields = ['columna_1', 'columna_2', 'columna_3']

    def vars_for_template(self):
        return {
            'preguntas': [
                {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
                {'22 DE OCTUBRE 1975': 'Pregunta 2', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            #     {'2 DE ENERO 1976': 'Pregunta 1', 'columna_1': self.player.columna_1, 'columna_2': self.player.columna_2, 'columna_3': self.player.columna_3},
            ]
        }

page_sequence = [
    Pagina_1,
]