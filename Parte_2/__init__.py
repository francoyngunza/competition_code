import random
from otree.api import *
import re



class C(BaseConstants):
    NAME_IN_URL = 'parte_2'
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
    pregunta_6 = models.StringField(label="¿Cuál figura completa lógicamente la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])
    pregunta_14 = models.StringField(label="Identifica el elemento que falta para completar el patrón", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6", "7", "8"])
    pregunta_28 = models.IntegerField(label="Determina que número debe reemplazar el signo de interrogación:")
    pregunta_31 = models.StringField(label="¿Qué figura completa la serie?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4"])
    pregunta_34 = models.StringField(label="¿Qué opción completa la serie correctamente?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])
    pregunta_37 = models.StringField(label="¿Qué opción completa la serie correctamente?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])
    pregunta_40 = models.StringField(label="¿Qué opción completa la serie correctamente?", widget=widgets.RadioSelectHorizontal, choices=["1", "2", "3", "4", "5", "6"])

    #Secuencias numéricas
    secuencia_numero_1 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_4 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_7 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_10 = models.IntegerField(label="¿Qué número continúa?")    
    secuencia_numero_13 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_16 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_19 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_22 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_25 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_28 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_31 = models.IntegerField(label="¿Qué número continúa?")    
    secuencia_numero_34 = models.IntegerField(label="¿Qué número continúa?")
    secuencia_numero_37 = models.StringField(label="¿Qué número continúa?")

    #Secuencias de letras
    secuencia_letra_1 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_4 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_7 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_10 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_13 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_16 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_19 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_22 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')
    secuencia_letra_25 = models.StringField(label='¿En la siguiente serie, ¿qué letra continúa?')


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
        if player.pregunta_6 == '1':
            player.correct_answers += 1   
        if player.pregunta_14 == '8':
            player.correct_answers += 1
        if player.pregunta_28 == 3:
            player.correct_answers += 1  
        if player.pregunta_31 == "2":
            player.correct_answers += 1
        if player.pregunta_34 == "5":
            player.correct_answers += 1     
        if player.pregunta_37 == "4":
            player.correct_answers += 1
        if player.pregunta_40 == "6":
            player.correct_answers += 1
        if player.secuencia_numero_1 == -5:
            player.correct_answers += 1
        if player.secuencia_numero_4 == 11:
            player.correct_answers += 1
        if player.secuencia_numero_7 == 174:
            player.correct_answers += 1
        if player.secuencia_numero_10 == 16:
            player.correct_answers += 1
        if player.secuencia_numero_13 == 30:
            player.correct_answers += 1
        if player.secuencia_numero_16 == 4:
            player.correct_answers += 1
        if player.secuencia_numero_19 == 741:
            player.correct_answers += 1
        if player.secuencia_numero_22 == 50:
            player.correct_answers += 1
        if player.secuencia_numero_25 == 38:
            player.correct_answers += 1
        if player.secuencia_numero_28 == 41:
            player.correct_answers += 1
        if player.secuencia_numero_31 == 1024:
            player.correct_answers += 1
        if player.secuencia_numero_34 == 37:
            player.correct_answers += 1
        if player.secuencia_numero_37 == 1003:
            player.correct_answers += 1
        if player.secuencia_letra_1 == 'M':
            player.correct_answers += 1
        if player.secuencia_letra_4 == 'G':
            player.correct_answers += 1
        if player.secuencia_letra_7 == 'O':
            player.correct_answers += 1
        if player.secuencia_letra_10 == 'd':
            player.correct_answers += 1
        if player.secuencia_letra_13 == 'u':
            player.correct_answers += 1
        if player.secuencia_letra_16 == 'ñ' or player.secuencia_letra_16 == 'o':
            player.correct_answers += 1
        if player.secuencia_letra_19 == 'r':
            player.correct_answers += 1
        if player.secuencia_letra_22 == 'B':
            player.correct_answers += 1
        if player.secuencia_letra_25 == 'K15':
            player.correct_answers += 1
    for player in players:
            player.payoff = player.correct_answers*0.05
    


def get_timeout_seconds(player):
    participant = player.participant
    import time
    return participant.expiry - time.time()

################################              PAGES            #################################

class Introduction(Page):

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        import time

        # remember to add 'expiry' to PARTICIPANT_FIELDS.
        participant.expiry = time.time() + 5*60

class Pregunta_3(Page):
    form_model = "player"
    form_fields = ["pregunta_3"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_6(Page):
    form_model = "player"
    form_fields = ["pregunta_6"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_14(Page):
    form_model = "player"
    form_fields = ["pregunta_14"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_28(Page):
    form_model = "player"
    form_fields = ["pregunta_28"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_31(Page):
    form_model = "player"
    form_fields = ["pregunta_31"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_34(Page):
    form_model = "player"
    form_fields = ["pregunta_34"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_37(Page):
    form_model = "player"
    form_fields = ["pregunta_37"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class Pregunta_40(Page):
    form_model = "player"
    form_fields = ["pregunta_40"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_1(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_1"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_4(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_4"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_7(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_7"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_10(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_10"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_13(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_13"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_16(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_16"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_19(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_19"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1
    
class secuencia_numero_22(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_22"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_25(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_25"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_28(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_28"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_31(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_31"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_numero_34(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_34"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1
    
class secuencia_numero_37(Page):
    form_model = "player"
    form_fields = ["secuencia_numero_37"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1


class secuencia_letra_1(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_1"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_4(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_4"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_7(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_7"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_10(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_10"]

    get_timeout_seconds = get_timeout_seconds    

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1
    
class secuencia_letra_13(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_13"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_16(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_16"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_19(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_19"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_22(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_22"]

    get_timeout_seconds = get_timeout_seconds

    @staticmethod
    def is_displayed(player):
        return get_timeout_seconds(player) > 1

class secuencia_letra_25(Page):
    form_model = "player"
    form_fields = ["secuencia_letra_25"]

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
    Introduction,
    Pregunta_3,
    Pregunta_6,
    Pregunta_14,
    Pregunta_28,
    Pregunta_31,
    Pregunta_34,
    Pregunta_37,
    Pregunta_40,
    secuencia_numero_1,
    secuencia_numero_4,
    secuencia_numero_7,
    secuencia_numero_10,
    secuencia_numero_13,
    secuencia_numero_16,
    secuencia_numero_19,
    secuencia_numero_22,
    secuencia_numero_25,
    secuencia_numero_28,
    secuencia_numero_31,
    secuencia_numero_34,
    secuencia_numero_37,
    secuencia_letra_1,
    secuencia_letra_4,
    secuencia_letra_7,
    secuencia_letra_10,
    secuencia_letra_13,
    secuencia_letra_16,
    secuencia_letra_19,
    secuencia_letra_22,
    secuencia_letra_25,
    ResultsWaitPage,
    Results_copy,
    #FinalResults,
]