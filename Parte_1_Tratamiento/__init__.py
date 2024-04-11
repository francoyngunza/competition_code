import random
from otree.api import *
import re

class C(BaseConstants):
    NAME_IN_URL = 'parte_1_t'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    multiplicador = 5

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    correct_answers = models.IntegerField(initial=0)

    columna_1 = models.BooleanField(initial=False)
    columna_2 = models.BooleanField(initial=False)
    columna_3 = models.BooleanField(initial=False)
    columna_4 = models.BooleanField(initial=False)
    columna_5 = models.BooleanField(initial=False)
    columna_6 = models.BooleanField(initial=False)
    columna_7 = models.BooleanField(initial=False)
    columna_8 = models.BooleanField(initial=False)
    columna_9 = models.BooleanField(initial=False)
    columna_10 = models.BooleanField(initial=False)
    columna_11 = models.BooleanField(initial=False)
    columna_12 = models.BooleanField(initial=False)
    columna_13 = models.BooleanField(initial=False)
    columna_14 = models.BooleanField(initial=False)
    columna_15 = models.BooleanField(initial=False)
    columna_16 = models.BooleanField(initial=False)
    columna_17 = models.BooleanField(initial=False)
    columna_18 = models.BooleanField(initial=False)
    columna_19 = models.BooleanField(initial=False)
    columna_20 = models.BooleanField(initial=False)
    columna_21 = models.BooleanField(initial=False)
    columna_22 = models.BooleanField(initial=False)
    columna_23 = models.BooleanField(initial=False)
    columna_24 = models.BooleanField(initial=False)
    columna_25 = models.BooleanField(initial=False)
    columna_26 = models.BooleanField(initial=False)
    columna_27 = models.BooleanField(initial=False)
    columna_28 = models.BooleanField(initial=False)
    columna_29 = models.BooleanField(initial=False)
    columna_30 = models.BooleanField(initial=False)
    columna_31 = models.BooleanField(initial=False)
    columna_32 = models.BooleanField(initial=False)
    columna_33 = models.BooleanField(initial=False)
    columna_34 = models.BooleanField(initial=False)
    columna_35 = models.BooleanField(initial=False)
    columna_36 = models.BooleanField(initial=False)
    columna_37 = models.BooleanField(initial=False)
    columna_38 = models.BooleanField(initial=False)
    columna_39 = models.BooleanField(initial=False)
    columna_40 = models.BooleanField(initial=False)
    columna_41 = models.BooleanField(initial=False)
    columna_42 = models.BooleanField(initial=False)
    columna_43 = models.BooleanField(initial=False)
    columna_44 = models.BooleanField(initial=False)
    columna_45 = models.BooleanField(initial=False)
    columna_46 = models.BooleanField(initial=False)
    columna_47 = models.BooleanField(initial=False)
    columna_48 = models.BooleanField(initial=False)
    columna_49 = models.BooleanField(initial=False)
    columna_50 = models.BooleanField(initial=False)
    columna_51 = models.BooleanField(initial=False)
    columna_52 = models.BooleanField(initial=False)
    columna_53 = models.BooleanField(initial=False)
    columna_54 = models.BooleanField(initial=False)
    columna_55 = models.BooleanField(initial=False)
    columna_56 = models.BooleanField(initial=False)
    columna_57 = models.BooleanField(initial=False)
    columna_58 = models.BooleanField(initial=False)
    columna_59 = models.BooleanField(initial=False)
    columna_60 = models.BooleanField(initial=False)
    columna_61 = models.BooleanField(initial=False)
    columna_62 = models.BooleanField(initial=False)
    columna_63 = models.BooleanField(initial=False)   
    columna_64 = models.BooleanField(initial=False)
    columna_65 = models.BooleanField(initial=False)
    columna_66 = models.BooleanField(initial=False)
    columna_67 = models.BooleanField(initial=False)
    columna_68 = models.BooleanField(initial=False)
    columna_69 = models.BooleanField(initial=False)
    columna_70 = models.BooleanField(initial=False)
    columna_71 = models.BooleanField(initial=False)
    columna_72 = models.BooleanField(initial=False)
    columna_73 = models.BooleanField(initial=False)
    columna_74 = models.BooleanField(initial=False)
    columna_75 = models.BooleanField(initial=False)


#Functions
def set_payoffs(group: Group):
    players = group.get_players()
    for player in players:
        if player.columna_1 == True:
            player.correct_answers += 1
        if player.columna_3 == True:
            player.correct_answers += 1
        if player.columna_5 == True:
            player.correct_answers += 1
        if player.columna_7 == True:
            player.correct_answers += 1   
        if player.columna_15 == True:
            player.correct_answers += 1
        if player.columna_16 == True:
            player.correct_answers += 1
        if player.columna_21 == True:
            player.correct_answers += 1
        if player.columna_28 == True:
            player.correct_answers += 1
        if player.columna_33 == True:
            player.correct_answers += 1   
        if player.columna_38 == True:
            player.correct_answers += 1
        if player.columna_45 == True:
            player.correct_answers += 1
        if player.columna_55 == True:
            player.correct_answers += 1
        if player.columna_57 == True:
            player.correct_answers += 1
        if player.columna_58 == True:
            player.correct_answers += 1   
        if player.columna_59 == True:
            player.correct_answers += 1
        if player.columna_63 == True:
            player.correct_answers += 1
        if player.columna_66 == True:
            player.correct_answers += 1
        if player.columna_67 == True:
            player.correct_answers += 1
        if player.columna_73 == True:
            player.correct_answers += 1   
        if player.columna_74 == True:
            player.correct_answers += 1
    for player in players:
            player.payoff = player.correct_answers*0.05


class Introduction(Page):
    pass

class Pagina_1(Page):
    timeout_seconds = 420
    form_model = 'player'
    form_fields = []
    for i in range(1, 76):
        form_fields.append('columna_' + str(i))

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class Results_copy(Page):
    def vars_for_template(player: Player):
        rpta = player.correct_answers
        return {"rpta": rpta}

page_sequence = [
    Introduction,
    Pagina_1,
    ResultsWaitPage,
    Results_copy,
]