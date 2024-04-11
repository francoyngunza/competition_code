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
    NAME_IN_URL = 'Parte_3_1'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1
    multiplicador = 0.05

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    max_correct_answers = models.IntegerField()
    num_winners = models.IntegerField()


class Player(BasePlayer):
    is_winner = models.BooleanField(initial=False)
    correct_answers = models.IntegerField(initial=0)

    player_choice = models.BooleanField(label="Escoge el esquema en el que quieres jugar",choices=[
        [True, 'Competitivo'],
        [False, 'No Competitivo'],
    ], widget=widgets.RadioSelectHorizontal)

    pregunta_5 = models.StringField(label="¿Cuál figura completa lógicamente la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])
    pregunta_8 = models.IntegerField(label="Determina que número debe reemplazar el signo de interrogación:")
    pregunta_16 = models.StringField(label="Selecciona la figura que mejor completa la analogía", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])
    pregunta_30 = models.StringField(label="¿Qué figura completa la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4"])
    pregunta_33 = models.StringField(label="¿Qué figura completa la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4"])
    pregunta_36 = models.StringField(label="¿Qué opción completa la serie correctamente?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])
    pregunta_39 = models.StringField(label="¿Qué opción completa la serie correctamente?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])

    #Secuencias numéricas
    secuencia_numero_3 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_6 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_9 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_12 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_15 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_18 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_21 = models.IntegerField(label="¿Qué número continúa?")    
    secuencia_numero_24 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_27 = models.StringField(label="¿Qué elemento continúa?")
    secuencia_numero_30 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_33 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_36 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_39 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_40 = models.IntegerField(label="¿Qué número continúa?")

    #Secuencias de letras
    secuencia_letra_3 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_6 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_9 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_12 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_15 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_18 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_21 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_24 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_27 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')


def set_payoffs(group: Group):
    players = group.get_players()
    for player in players:
        if player.pregunta_5 == '2':
            player.correct_answers += 1
        if player.pregunta_8 == 26:
            player.correct_answers += 1
        if player.pregunta_16 == '1':
            player.correct_answers += 1   
        if player.pregunta_30 == 2:
            player.correct_answers += 1     
        if player.pregunta_33 == 4:
            player.correct_answers += 1
        if player.pregunta_36 == 1:
            player.correct_answers += 1     
        if player.pregunta_39 == 4:
            player.correct_answers += 1
        if player.secuencia_numero_3 == 405:
            player.correct_answers += 1
        if player.secuencia_numero_6 == 186:
            player.correct_answers += 1
        if player.secuencia_numero_9 == 90:
            player.correct_answers += 1
        if player.secuencia_numero_12 == 66:
            player.correct_answers += 1
        if player.secuencia_numero_15 == 47:
            player.correct_answers += 1
        if player.secuencia_numero_18 == 751:
            player.correct_answers += 1
        if player.secuencia_numero_21 == 8:
            player.correct_answers += 1
        if player.secuencia_numero_24 == 21:
            player.correct_answers += 1
        if player.secuencia_numero_27 == '6U':
            player.correct_answers += 1
        if player.secuencia_numero_30 == 1128:
            player.correct_answers += 1
        if player.secuencia_numero_33 == 11:
            player.correct_answers += 1
        if player.secuencia_numero_36 == 90:
            player.correct_answers += 1
        if player.secuencia_numero_39 == '3/125':
            player.correct_answers += 1
        if player.secuencia_numero_40 == 7:
            player.correct_answers += 1
        if player.secuencia_letra_3 == 'A':
            player.correct_answers += 1
        if player.secuencia_letra_6 == 'K':
            player.correct_answers += 1
        if player.secuencia_letra_9 == 'J':
            player.correct_answers += 1
        if player.secuencia_letra_12 == 'r':
            player.correct_answers += 1
        if player.secuencia_letra_15 == 'a':
            player.correct_answers += 1
        if player.secuencia_letra_18 == 'e':
            player.correct_answers += 1
        if player.secuencia_letra_21 == 'U':
            player.correct_answers += 1
        if player.secuencia_letra_24 == 'I':
            player.correct_answers += 1
        if player.secuencia_letra_27 == 'V-10':
            player.correct_answers += 1
    winner = max(players, key=lambda player: player.correct_answers)
    winner.is_winner = True
    for player in players:
        if player.player_choice:    ##Elige competitivo
            if player.is_winner == True: ##Ganador Competitivo
                player.payoff = player.correct_answers*0.05*2
            else:
                player.payoff = 0
        else:
            player.payoff = player.correct_answers*0.05

def get_timeout_seconds(player):
    participant = player.participant
    import time
    return participant.expiry - time.time()

# def creating_session(self):
#     self.group_randomly()

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
class ShuffleWaitPage(WaitPage):

    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession):
        subsession.set_group_matrix(subsession.session.vars['matching_matrix'])

class player_choice(Page):
    form_model = 'player'
    form_fields = ['player_choice']

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        import time

        # remember to add 'expiry' to PARTICIPANT_FIELDS.
        participant.expiry = time.time() + 5*60

class Introduction(Page):
    pass

class Pregunta_5(Page):
    form_model = "player"
    form_fields = ["pregunta_5"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1
   
class Pregunta_8(Page):
    form_model = "player"
    form_fields = ["pregunta_8"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_16(Page):
    form_model = "player"
    form_fields = ["pregunta_16"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_30(Page):
    form_model = "player"
    form_fields = ["pregunta_30"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_33(Page):
    form_model = "player"
    form_fields = ["pregunta_33"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_36(Page):
    form_model = "player"
    form_fields = ["pregunta_36"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1
    
class Pregunta_39(Page):
    form_model = "player"
    form_fields = ["pregunta_39"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1


class secuencia_numero_3(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_3"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_6(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_6"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_9(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_9"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_12(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_12"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_15(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_15"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_18(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_18"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_21(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_21"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_24(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_24"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_27(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_27"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_30(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_30"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_33(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_33"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_36(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_36"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_39(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_39"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1
    
class secuencia_numero_40(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_40"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_3(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_3"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_6(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_6"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_9(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_9"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_12(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_12"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_15(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_15"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_18(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_18"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_21(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_21"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_24(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_24"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_27(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_27"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs

class Results_copy(Page):
    def vars_for_template(player: Player):
        rpta = player.correct_answers
        return {"rpta": rpta}


page_sequence = [
    ShuffleWaitPage,
    Introduction,
    player_choice,
    Pregunta_5,
    Pregunta_8,
    Pregunta_16,
    Pregunta_30,
    Pregunta_33,
    Pregunta_36,
    Pregunta_39,
    secuencia_numero_3,
    secuencia_numero_6,
    secuencia_numero_9,
    secuencia_numero_12,
    secuencia_numero_15,
    secuencia_numero_18,
    secuencia_numero_21,
    secuencia_numero_24,
    secuencia_numero_27,
    secuencia_numero_30,
    secuencia_numero_33,
    secuencia_numero_36,
    secuencia_numero_39,
    secuencia_numero_40,
    secuencia_letra_3,
    secuencia_letra_6,
    secuencia_letra_9,
    secuencia_letra_12,
    secuencia_letra_15,
    secuencia_letra_18,
    secuencia_letra_21,
    secuencia_letra_24,
    secuencia_letra_27,
    ResultsWaitPage,
    Results_copy,
    #FinalResults,
]