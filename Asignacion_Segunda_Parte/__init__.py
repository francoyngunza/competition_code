from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'asignacion'
    PLAYERS_PER_GROUP = None  # You can set this to a specific number if needed
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    player_choice = models.BooleanField(label="Escoge el esquema en el que quieres jugar",choices=[
        [True, 'No Competitivo'],
        [False, 'Competitivo'],
    ], widget=widgets.RadioSelectHorizontal)

# def creating_session(subsession):
#     import random
#     for player in subsession.get_players():
#         player.player_choice = player.player_choice

class MyWaitPage(WaitPage):
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        if player.player_choice:
            return "Parte_2"
        else:
            return "Parte_3_copy"

class player_choice(Page):
    form_model = 'player'
    form_fields = ['player_choice']


        

        
page_sequence = [player_choice, MyWaitPage]