import random
from otree.api import *
import re


class C(BaseConstants):
    NAME_IN_URL = 'Parte_3'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 1
    multiplicador = 0.05

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    max_correct_answers = models.StringField()
    num_winners = models.StringField()


class Player(BasePlayer):
    is_winner = models.BooleanField(initial=False)
    correct_answers = models.IntegerField(initial=0)

    pregunta_4 = models.StringField(label="Identifica el elemento que falta para completar el patrón", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6", "7", "8"])
    pregunta_7 = models.StringField(label="Determina que número debe reemplazar el signo de interrogación:")
    pregunta_15 = models.StringField(label="Selecciona la figura que mejor completa la analogía", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])
    pregunta_29 = models.StringField(label="¿Qué figura completa la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4"])
    pregunta_32 = models.StringField(label="¿Qué figura completa la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4"])
    pregunta_35 = models.StringField(label="¿Qué opción completa la serie correctamente?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])
    pregunta_38 = models.StringField(label="¿Qué opción completa la serie correctamente?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])
    pregunta_41 = models.StringField(label="¿Qué opción completa la serie correctamente?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])

    #Secuencias numéricas
    secuencia_numero_2 = models.StringField(label="¿Qué número continúa?")
    secuencia_numero_5 = models.StringField(label="¿Qué número continúa?")
    secuencia_numero_8 = models.StringField(label="¿Qué número continúa?")  
    secuencia_numero_11 = models.StringField(label="¿Qué número continúa?")
    secuencia_numero_14 = models.StringField(label="¿Qué número continúa?")
    secuencia_numero_17 = models.StringField(label="¿Qué número continúa?")
    secuencia_numero_20 = models.StringField(label="¿Qué número continúa?")
    secuencia_numero_23 = models.StringField(label="¿Qué número continúa?")
    secuencia_numero_26 = models.StringField(label="¿Qué número continúa?")
    secuencia_numero_29 = models.StringField(label="¿Qué número continúa?")
    secuencia_numero_32 = models.StringField(label="¿Qué número continúa?")
    secuencia_numero_35 = models.StringField(label="¿Qué número continúa?")
    secuencia_numero_38 = models.StringField(label="¿Qué número continúa?")

    #Secuencias de letras
    secuencia_letra_2 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_5 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_8 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_11 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_14 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_17 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_20 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_23 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_26 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')


def set_payoffs(group: Group):
    players = group.get_players()
    for player in players:
        if player.field_maybe_none('pregunta_4') == '6':
            player.correct_answers += 1  
        if player.field_maybe_none('pregunta_7') == '12':
            player.correct_answers += 1
        if player.field_maybe_none('pregunta_15') == '6':
            player.correct_answers += 1
        if player.field_maybe_none('pregunta_29') == '2':
            player.correct_answers += 1
        if player.field_maybe_none('pregunta_32') == '2':
            player.correct_answers += 1     
        if player.field_maybe_none('pregunta_35') == '4':
            player.correct_answers += 1
        if player.field_maybe_none('pregunta_38') == '5':
            player.correct_answers += 1    
        if player.field_maybe_none('pregunta_41') == '2':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_2') == '65':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_5') == '2520':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_8') == '8552':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_11') == '17/49':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_14') == '178':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_17') == '56':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_20') == '40':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_23') == '41':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_26') == '48':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_29') == '36':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_32') == '44':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_35') == '-1':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_numero_38') == '7':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_2') == 'N':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_5') == 'G':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_8') == 'S':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_11') == 'b':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_14') == 'n':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_17') == 'l':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_20') == 'T':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_23') == 'Y':
            player.correct_answers += 1
        if player.field_maybe_none('secuencia_letra_26') == 'X':
            player.correct_answers += 1
    winner = max(players, key=lambda player: player.correct_answers)
    winner.is_winner = True
        # Define los pagos
    for player in players:
        if player.is_winner:
            player.payoff = player.correct_answers*0.05*2
        else:
            player.payoff = 0

def get_timeout_seconds(player):
    participant = player.participant
    import time
    return participant.expiry - time.time()
    
#PAGES
class ShuffleWaitPage(WaitPage):

    wait_for_all_groups = True

    @staticmethod
    def after_all_players_arrive(subsession):
        subsession.group_randomly()
        subsession.session.vars['matching_matrix'] = subsession.get_group_matrix() 

class Introduction(Page):

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        import time

        # remember to add 'expiry' to PARTICIPANT_FIELDS.
        participant.expiry = time.time() + 1*60

class Pregunta_4(Page):
    form_model = "player"
    form_fields = ["pregunta_4"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_7(Page):
    form_model = "player"
    form_fields = ["pregunta_7"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_15(Page):
    form_model = "player"
    form_fields = ["pregunta_15"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_29(Page):
    form_model = "player"
    form_fields = ["pregunta_29"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_32(Page):
    form_model = "player"
    form_fields = ["pregunta_32"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_35(Page):
    form_model = "player"
    form_fields = ["pregunta_35"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_38(Page):
    form_model = "player"
    form_fields = ["pregunta_38"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_41(Page):
    form_model = "player"
    form_fields = ["pregunta_41"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_2(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_2"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_5(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_5"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_8(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_8"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_11(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_11"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_14(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_14"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_17(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_17"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_20(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_20"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1
    
class secuencia_numero_23(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_23"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_26(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_26"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_29(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_29"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_32(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_32"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_35(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_35"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_38(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_38"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_2(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_2"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_5(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_5"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_8(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_8"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_11(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_11"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_14(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_14"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_17(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_17"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1
    
class secuencia_letra_20(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_20"]

    get_timeout_seconds = get_timeout_seconds


    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_23(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_23"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_26(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_26"]

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
    Pregunta_4,
    Pregunta_7,
    Pregunta_15,
    Pregunta_29,
    Pregunta_32,
    Pregunta_35,
    Pregunta_38,
    Pregunta_41,
    secuencia_numero_2,
    secuencia_numero_5,
    secuencia_numero_8,
    secuencia_numero_11,
    secuencia_numero_14,
    secuencia_numero_17,
    secuencia_numero_20,
    secuencia_numero_23,
    secuencia_numero_26,
    secuencia_numero_29,
    secuencia_numero_32,
    secuencia_numero_35,
    secuencia_numero_38,
    secuencia_letra_2,
    secuencia_letra_5,
    secuencia_letra_8,
    secuencia_letra_11,
    secuencia_letra_14,
    secuencia_letra_17,
    secuencia_letra_20,
    secuencia_letra_23,
    secuencia_letra_26,
    ResultsWaitPage,
    Results_copy,
    #FinalResults,
]