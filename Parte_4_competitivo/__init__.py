import random
from otree.api import *
import re

class C(BaseConstants):
    NAME_IN_URL = 'Parte_4_competitivo'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    multiplicador = 0.05

# class Subsession(BaseSubsession):
#     pass

class Group(BaseGroup):
    max_correct_answers = models.IntegerField()
    num_winners = models.IntegerField()


class Player(BasePlayer):
    is_winner = models.BooleanField(initial=False)
    correct_answers = models.IntegerField(initial=0)

    pregunta_3 = models.StringField(label="Identifica el elemento que falta para completar el patrón", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6", "7", "8"])
    pregunta_4 = models.StringField(label="Identifica el elemento que falta para completar el patrón", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6", "7", "8"])
    pregunta_5 = models.StringField(label="¿Cuál figura completa lógicamente la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])
    pregunta_6 = models.StringField(label="¿Cuál figura completa lógicamente la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])
    pregunta_7 = models.IntegerField(label="Determina que número debe reemplazar el signo de interrogación:")

def set_payoffs(group: Group):
    players = group.get_players()
    for player in players:
        if player.pregunta_3 == '7':
            player.correct_answers += 1
        if player.pregunta_4 == '6':
            player.correct_answers += 1
        if player.pregunta_5 == '2':
            player.correct_answers += 1
        if player.pregunta_6 == '1':
            player.correct_answers += 1   
        if player.pregunta_7 == 12:
            player.correct_answers += 1
    winner = max(players, key=lambda player: player.correct_answers)
    winner.is_winner = True
        # Define los pagos
    for player in players:
        if player.is_winner:
            player.payoff = player.correct_answers*0.05
        else:
            player.payoff = 0


# FUNCTIONS 
# def set_payoffs(group: Group):
#     players = group.get_players()
#     for player in players:
#         player.correct_answers
#         # Encuentra al jugador con más respuestas correctas
#     winner = max(players, key=lambda player: player.correct_answers)
#     winner.is_winner = True
#         # Define los pagos
#     for player in players:
#         if player.is_winner:
#             player.payoff = player.correct_answers * 5
#         else:
#             player.payoff = 0
    
#PAGES
class pregunta_3(Page):
    form_model = "player"
    form_fields = ["pregunta_3"]

class pregunta_4(Page):
    form_model = "player"
    form_fields = ["pregunta_4"]

class pregunta_5(Page):
    form_model = "player"
    form_fields = ["pregunta_5"]

class pregunta_6(Page):
    form_model = "player"
    form_fields = ["pregunta_6"]

class pregunta_7(Page):
    form_model = "player"
    form_fields = ["pregunta_7"]

class GroupingWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.subsession.assign_participants()

class Subsession(BaseSubsession):
    def assign_participants(self):
        players = self.get_players()
        num_players = len(players)
        new_structure = []

        if num_players <= 4:
            new_structure = [list(range(1, num_players + 1))]
        else:
            while num_players > 0:
                if num_players % 3 == 0 or num_players % 4 == 0:
                    group_size = 3 if num_players % 3 == 0 else 4
                    new_structure.append(list(range(num_players - group_size + 1, num_players + 1)))
                    num_players -= group_size
                elif num_players == 5:
                    new_structure.append([num_players - 1, num_players])
                    num_players -= 2
                else:
                    new_structure.append([num_players])
                    num_players -= 1

        self.set_group_matrix(new_structure)




# class GroupingWaitPage(WaitPage):
#     def after_all_players_arrive(subsession: Subsession):
#         players = subsession.get_players()
#         num_players = len(players)

#     Si hay menos de 4 jugadores, se les asigna a un grupo
#         if num_players == 2:
#             new_structure = [[1,2]]
#         elif num_players == 3:
#             new_structure = [[1,2,3]]
#         elif num_players == 4:
#             new_structure = [[1,2,3,4]]
#         elif num_players == 5:
#             new_structure = [[1,2,3,4,5]]
#         elif num_players == 6:
#             new_structure = [[1,2,3], [4,5,6]]
#         elif num_players == 7:
#             new_structure = [[1,2,3,4], [5,6,7]]
#         elif num_players == 8:
#             new_structure = [[1,2,3,4], [5,6,7,8]]
#         elif num_players == 9:
#             new_structure = [[1,2,3], [4,5,6], [7,8,9]]
#         elif num_players ==10:
#             new_structure = [[1,2,3,4], [5,6,7], [8,9,10]]  
#         elif num_players == 11:
#             new_structure = [[1,2,3,4], [5,6,7,8], [5,6,7,8]]
#         elif num_players == 12:
#             new_structure = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
#         elif num_players == 13:
#             new_structure = [[1,2,3,4], [5,6,7], [8,9,10], [11,12,13]]
#         elif num_players ==14:
#             new_structure = [[1,2,3,4], [5,6,7,8], [9,10,11], [12,13,14]]
#         elif num_players == 15:
#             new_structure = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15]]
#         elif num_players == 16:
#             new_structure = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
#         elif num_players == 17:
#             new_structure = [[1,2,3,4], [5,6,7,8], [9,10,11], [12,13,14], [15,16,17]]
#         elif num_players == 18:
#             new_structure = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15], [16,17,18]]
#         elif num_players == 19:
#             new_structure = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16], [17,18,19,20]]
#         elif num_players == 20:
#             new_structure = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16], [17,18,19,20]]

#         subsession.set_group_matrix(new_structure)


class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class Results_copy(Page):
    def vars_for_template(player: Player):
        rpta = player.correct_answers
        return {"rpta": rpta}


page_sequence = [
    GroupingWaitPage,
    pregunta_3,
    pregunta_4,
    pregunta_5,
    pregunta_6,
    pregunta_7,
    ResultsWaitPage,
    Results_copy,
    #FinalResults,
]