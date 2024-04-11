import random
from otree.api import *
import re




# doc = """
# This is a standard 2-player trust game where the amount sent by player 1 gets
# tripled. The trust game was first proposed by
# <a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/Berg%20et%20al%20GEB%201995.pdf" target="_blank">
#     Berg, Dickhaut, and McCabe (1995)
# </a>.
# """


# class C(BaseConstants):
#     NAME_IN_URL = 'trust'
#     PLAYERS_PER_GROUP = 2
#     NUM_ROUNDS = 3
#     # Initial amount allocated to each player
#     ENDOWMENT = cu(50)
#     MULTIPLIER = 3
#     FM_ROLE = 'First mover'
#     SM_ROLE = 'Second mover'



# class Subsession(BaseSubsession):
#     pass


# class Group(BaseGroup):
#     sent_amount = models.CurrencyField(
#         min=0,
#         max=C.ENDOWMENT,
#         doc="""Amount sent by P1""",
#         label="Please enter an amount from 0 to 100:",
#     )
#     sent_back_amount = models.CurrencyField(doc="""Amount sent back by P2""", min=cu(0))


# class Player(BasePlayer):
#     pass


# # FUNCTIONS
# def sent_back_amount_max(group: Group):
#     return group.sent_amount * C.MULTIPLIER



# def set_payoffs(group: Group):
#     p1 = group.get_player_by_id(1)
#     p2 = group.get_player_by_id(2)
#     p1.payoff = C.ENDOWMENT - group.sent_amount + group.sent_back_amount
#     p2.payoff = group.sent_amount * C.MULTIPLIER - group.sent_back_amount


# # Funciones avanzadas> lista desplegable
# def sent_amount_choices(group: Group):
#     montos = range(0,int(C.ENDOWMENT)+1,5)
#     lista = list(montos)
#     choices = lista
#     return(choices)

# def creating_session(self):
#     self.group_randomly()

# # PAGES
# class Introduction(Page):
#     @staticmethod
#     def is_displayed(player: Player):
#         return player.round_number == 1


# class Send(Page):
    
#     """This page is only for P1
#     P1 sends amount (all, some, or none) to P2
#     This amount is tripled by experimenter,
#     i.e if sent amount by P1 is 5, amount received by P2 is 15"""

#     form_model = 'group'
#     form_fields = ['sent_amount']
#     timeout_seconds = 60

#     @staticmethod
#     def is_displayed(player: Player):
#         return player.id_in_group == 1


# class SendBackWaitPage(WaitPage):
#     title_text = "Por favor, espere"
#     body_text = "Esperando a que los otros participantes tomen una decisión"
#     pass


# class SendBack(Page):
#     """This page is only for P2
#     P2 sends back some amount (of the tripled amount received) to P1"""

#     form_model = 'group'
#     form_fields = ['sent_back_amount']
#     timeout_seconds = 60

#     @staticmethod
#     def is_displayed(player: Player):
#         return player.id_in_group == 2

#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group

#         tripled_amount = group.sent_amount * C.MULTIPLIER
#         return dict(tripled_amount=tripled_amount)
    


# class ResultsWaitPage(WaitPage):
#     title_text = "Por favor, espere"
#     body_text = "Esperando a que los otros participantes tomen una decisión"
#     after_all_players_arrive = set_payoffs
    


# class Results(Page):
#     """This page displays the earnings of each player"""

#     @staticmethod
#     def vars_for_template(player: Player):
#         group = player.group
        
#         return dict(tripled_amount=group.sent_amount * C.MULTIPLIER)


# class FinalResults(Page):
#     """This page shows the final payoff for each player"""
    
#     @staticmethod
#     def is_displayed(player: Player):
#         return player.round_number == C.NUM_ROUNDS

#     @staticmethod
#     def vars_for_template(player: Player):
#         round_payoffs = [player.in_round(r).payoff for r in range(1, C.NUM_ROUNDS + 1)]
#         # Seleccionar aleatoriamente un pago entre los obtenidos en las tres rondas
#         final_payoff = random.choice(round_payoffs)
#         return {'final_payoff': final_payoff}


# page_sequence = [
#     Introduction,
#     Send,
#     SendBackWaitPage,
#     SendBack,
#     ResultsWaitPage,
#     Results,
#     FinalResults,
# ]

class C(BaseConstants):
    NAME_IN_URL = 'parte_4_no_competitivo'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    multiplicador = 5

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    correct_answers = models.IntegerField(initial=0)

    pregunta_3 = models.StringField(label="Identifica el elemento que falta para completar el patrón", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6", "7", "8"])
    pregunta_4 = models.StringField(label="Identifica el elemento que falta para completar el patrón", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6", "7", "8"])
    pregunta_5 = models.StringField(label="¿Cuál figura completa lógicamente la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])
    pregunta_6 = models.StringField(label="¿Cuál figura completa lógicamente la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])
    pregunta_7 = models.IntegerField(label="Determina que número debe reemplazar el signo de interrogación:")

    # def is_pregunta_3_correct(self):
    #     return self.pregunta_3 == "7"

    # def is_pregunta_4_correct(self):
    #     return self.pregunta_4 == "6"
    
    # def is_pregunta_5_correct(self):
    #     return self.pregunta_5 == "2"
    
    # def is_pregunta_6_correct(self):
    #     return self.pregunta_6 == "4"
    
    # def is_pregunta_7_correct(self):
    #     return self.pregunta_7 == 12
    
    # def calculate_payment(self):
    #     correct_answers = 0
    #     if self.is_pregunta_3_correct():
    #         correct_answers += 1
    #     if self.is_pregunta_4_correct():
    #         correct_answers += 1
    #     if self.is_pregunta_5_correct():
    #         correct_answers += 1
    #     if self.is_pregunta_6_correct():
    #         correct_answers += 1
    #     if self.is_pregunta_7_correct():
    #         correct_answers += 1    

    #     return correct_answers * 0.05  #0.05PEN por respuesta correcta
    
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
    for player in players:
            player.payoff = player.correct_answers*0.05
    
#PAGES
class Pregunta_3(Page):
    form_model = "player"
    form_fields = ["pregunta_3"]

class Pregunta_4(Page):
    form_model = "player"
    form_fields = ["pregunta_4"]

class Pregunta_5(Page):
    form_model = "player"
    form_fields = ["pregunta_5"]

class Pregunta_6(Page):
    form_model = "player"
    form_fields = ["pregunta_6"]

class Pregunta_7(Page):
    form_model = "player"
    form_fields = ["pregunta_7"]

class Results_copy(Page):
    def vars_for_template(player: Player):
        rpta = player.correct_answers
        return {"rpta": rpta}


page_sequence = [
    Pregunta_3,
    Pregunta_4,
    Pregunta_5,
    Pregunta_6,
    Pregunta_7,
    Results_copy,
    #FinalResults,
]