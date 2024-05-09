import random
from otree.api import *
import re

class C(BaseConstants):
    NAME_IN_URL = 'parte_2_c'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    multiplicador = 5

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    correct_answers = models.IntegerField(initial=0)
    complicada_1 = models.IntegerField(initial=1)

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


#Pages  
# class Pagina_1(Page):
#     form_model = 'player'
#     form_fields = ['columna_1', 'columna_2', 'columna_3', 'columna_4',
#     'columna_5',
#     'columna_6',
#     'columna_7',
#     'columna_8',
#     'columna_9,
#     columna_10,
#     columna_11,
#     columna_12,
#     columna_13,
#     columna_14,
#     columna_15,
#     columna_16,
#     columna_17,
#     columna_18,
#     columna_19,
#     columna_20,
#     columna_21,
#     columna_22,
#     columna_23,
#     columna_24,
#     columna_25,
#     columna_26,
#     columna_27,
#     columna_28,
#     columna_29,
#     columna_30,
#     columna_31,
#     columna_32,
#     columna_33,
#     columna_34,
#     columna_35,
#     columna_36,
#     columna_37,
#     columna_38,
#     columna_39,
#     columna_40,
#     columna_41,
#     columna_42,
#     columna_43,
#     columna_44,
#     columna_45,
#     columna_46,
#     columna_47,
#     columna_48,
#     columna_49,
#     columna_50,
#     columna_51,
#     columna_52,
#     columna_53,
#     columna_54,
#     columna_55,
#     columna_56,
#     columna_57 = models.BooleanField(initial=False)
#     columna_58 = models.BooleanField(initial=False)
#     columna_59 = models.BooleanField(initial=False)
#     columna_60 = models.BooleanField(initial=False)
#     columna_61 = models.BooleanField(initial=False)
#     columna_62 = models.BooleanField(initial=False)
#     columna_63 = models.BooleanField(initial=False)   
#     columna_64 = models.BooleanField(initial=False)
#     columna_65 = models.BooleanField(initial=False)
#     columna_66 = models.BooleanField(initial=False)
#     columna_67 = models.BooleanField(initial=False)
#     columna_68 = models.BooleanField(initial=False)
#     columna_69 = models.BooleanField(initial=False)
#     columna_70 = models.BooleanField(initial=False)
#     columna_71 = models.BooleanField(initial=False)
#     columna_72 = models.BooleanField(initial=False)
#     columna_73 = models.BooleanField(initial=False)
#     columna_74 = models.BooleanField(initial=False)
#     columna_75 = models.BooleanField(initial=False)]

#Functions
def set_payoffs(group: Group):
    players = group.get_players()
    for player in players:
        if player.columna_1 == 1:
            player.correct_answers += 1
        if player.columna_2 == 1:
            player.correct_answers += 1
        if player.columna_3 == 1:
            player.correct_answers += 1
        if player.columna_5 == 1:
            player.correct_answers += 1   
        if player.columna_7 == 1:
            player.correct_answers += 1
        if player.columna_9 == 1:
            player.correct_answers += 1
        if player.columna_10 == 1:
            player.correct_answers += 1
        if player.columna_11 == 1:
            player.correct_answers += 1
        if player.columna_12 == 1:
            player.correct_answers += 1   
        if player.columna_13 == 1:
            player.correct_answers += 1
        if player.columna_15 == 1:
            player.correct_answers += 1
        if player.columna_16 == 1:
            player.correct_answers += 1
        if player.columna_17 == 1:
            player.correct_answers += 1
        if player.columna_18 == 1:
            player.correct_answers += 1   
        if player.columna_21 == 1:
            player.correct_answers += 1
        if player.columna_23 == 1:
            player.correct_answers += 1
        if player.columna_25 == 1:
            player.correct_answers += 1
        if player.columna_27 == 1:
            player.correct_answers += 1
        if player.columna_28 == 1:
            player.correct_answers += 1   
        if player.columna_29 == 1:
            player.correct_answers += 1
        if player.columna_30 == 1:
            player.correct_answers += 1
        if player.columna_33 == 1:
            player.correct_answers += 1   
        if player.columna_34 == 1:
            player.correct_answers += 1
        if player.columna_35 == 1:
            player.correct_answers += 1
        if player.columna_36 == 1:
            player.correct_answers += 1
        if player.columna_38 == 1:
            player.correct_answers += 1
        if player.columna_41 == 1:
            player.correct_answers += 1   
        if player.columna_45 == 1:
            player.correct_answers += 1
        if player.columna_46 == 1:
            player.correct_answers += 1
        if player.columna_47 == 1:
            player.correct_answers += 1   
        if player.columna_48 == 1:
            player.correct_answers += 1
        if player.columna_51 == 1:
            player.correct_answers += 1
        if player.columna_52 == 1:
            player.correct_answers += 1   
        if player.columna_53 == 1:
            player.correct_answers += 1
        if player.columna_54 == 1:
            player.correct_answers += 1
        if player.columna_57 == 1:
            player.correct_answers += 1
        if player.columna_58 == 1:
            player.correct_answers += 1
        if player.columna_59 == 1:
            player.correct_answers += 1   
        if player.columna_60 == 1:
            player.correct_answers += 1
        if player.columna_63 == 1:
            player.correct_answers += 1
        if player.columna_64 == 1:
            player.correct_answers += 1
        if player.columna_65 == 1:
            player.correct_answers += 1   
        if player.columna_66 == 1:
            player.correct_answers += 1
        if player.columna_67 == 1:
            player.correct_answers += 1
        if player.columna_69 == 1:
            player.correct_answers += 1
        if player.columna_71 == 1:
            player.correct_answers += 1
        if player.columna_73 == 1:
            player.correct_answers += 1   
        if player.columna_74 == 1:
            player.correct_answers += 1
        if player.columna_75 == 1:
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
    
class MyWaitPage(WaitPage):
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        if player.complicada_1==1:
            return "Parte_3"
        else:
            return "Parte_3"
        
page_sequence = [
    Introduction,
    Pagina_1,
    ResultsWaitPage,
    Results_copy,
    MyWaitPage,
]