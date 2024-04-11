import random
from otree.api import *
import re




class C(BaseConstants):
    NAME_IN_URL = 'Parte_3_1'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1
    multiplicador = 0.05

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    is_winner = models.BooleanField(initial=False)
    correct_answers = models.IntegerField(initial=0)

    player_choice = models.BooleanField(label="Escoge el esquema en el que quieres jugar",choices=[
        [True, 'Competitivo'],
        [False, 'No Competitivo'],
    ], widget=widgets.RadioSelectHorizontal)

    pregunta_5 = models.StringField(label="¿Cuál figura completa lógicamente la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"], blank=True)
    pregunta_8 = models.IntegerField(label="Determina que número debe reemplazar el signo de interrogación:", blank=True)
    pregunta_16 = models.StringField(label="Selecciona la figura que mejor completa la analogía", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"], blank=True)
    pregunta_30 = models.StringField(label="¿Qué figura completa la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4"], blank=True)
    pregunta_33 = models.StringField(label="¿Qué figura completa la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4"], blank=True)
    pregunta_36 = models.StringField(label="¿Qué opción completa la serie correctamente?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"], blank=True)
    pregunta_39 = models.StringField(label="¿Qué opción completa la serie correctamente?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"], blank=True)

    #Secuencias numéricas
    secuencia_numero_3 = models.IntegerField(label="¿Qué número continúa?", blank=True)
    secuencia_numero_6 = models.IntegerField(label="¿Qué número continúa?", blank=True)
    secuencia_numero_9 = models.IntegerField(label="¿Qué número continúa?", blank=True)
    secuencia_numero_12 = models.IntegerField(label="¿Qué número continúa?", blank=True)
    secuencia_numero_15 = models.IntegerField(label="¿Qué número continúa?", blank=True)
    secuencia_numero_18 = models.IntegerField(label="¿Qué número continúa?", blank=True)
    secuencia_numero_21 = models.IntegerField(label="¿Qué número continúa?", blank=True)    
    secuencia_numero_24 = models.IntegerField(label="¿Qué número continúa?", blank=True)
    secuencia_numero_27 = models.StringField(label="¿Qué elemento continúa?", blank=True)
    secuencia_numero_30 = models.IntegerField(label="¿Qué número continúa?", blank=True)
    secuencia_numero_33 = models.IntegerField(label="¿Qué número continúa?", blank=True)
    secuencia_numero_36 = models.IntegerField(label="¿Qué número continúa?", blank=True)
    secuencia_numero_39 = models.StringField(label="¿Qué número continúa?", blank=True)
    secuencia_numero_40 = models.IntegerField(label="¿Qué número continúa?", blank=True)

    #Secuencias de letras
    secuencia_letra_3 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?', blank=True)
    secuencia_letra_6 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?', blank=True)
    secuencia_letra_9 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?', blank=True)
    secuencia_letra_12 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?', blank=True)
    secuencia_letra_15 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?', blank=True)
    secuencia_letra_18 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?', blank=True)
    secuencia_letra_21 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?', blank=True)
    secuencia_letra_24 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?', blank=True)
    secuencia_letra_27 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?', blank=True)


def set_payoffs(group: Group):
    players = group.get_players()
    for player in players:
        if player.field_maybe_none('pregunta_5') == '2':
            player.correct_answers += 1
        if player.field_maybe_none('pregunta_8') == 26:
            player.correct_answers += 1
        if player.field_maybe_none('pregunta_16') == '1':
            player.correct_answers += 1   
        if player.field_maybe_none('pregunta_30') == '2':
            player.correct_answers += 1     
        if player.field_maybe_none('pregunta_33') == '4':
            player.correct_answers += 1
        if player.field_maybe_none('pregunta_36') == '1':
            player.correct_answers += 1     
        if player.field_maybe_none('pregunta_39') == '4':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_3') == 405:
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_6') == 186:
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_9') == 90:
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_12') == 66:
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_15') == 47:
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_18') == 751:
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_21') == 8:
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_24') == 21:
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_27') == '6U':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_30') == 1128:
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_33') == 11:
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_36') == 90:
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_39') == '3/125':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_40') == 7:
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_3') == 'A':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_6') == 'K':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_9') == 'J':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_12') == 'r':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_15') == 'a':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_18') == 'e':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_21') == 'U':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_24') == 'I':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_27') == 'V-10':
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
        participant.expiry = time.time() + 1*60

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
    
class Final_Page(Page):
    pass


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
    Final_Page,
    #FinalResults,
]