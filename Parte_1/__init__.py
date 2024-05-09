import random as r
from otree.api import *
import re

author = 'FAYC'

doc = """
Tanaka et al. (2010) Measure Task based on CPT
"""


class Constants(BaseConstants):
    name_in_url = 'measure_task'
    players_per_group = None
    num_rounds = 1
    num_breaks = 3
    instructions_template = "measure_task/Instructions.html"
    choices_series1 = [[1,'1'], [2,'2'], [3,'3'], [4,'4'], [5,'5'], [6,'6'], [7,'7'], [8,'8'], [9,'9'], [10,'10'], [11,'11'], [0 ,'Ninguna']]
    valor_moneda_exp = 0.02

    lotteries = [
    [
        {"high_paym_A": 100, "low_paym_A": 0, "unico_paym_B": 10},
        {"high_paym_A": 100, "low_paym_A": 0, "unico_paym_B": 14},
        {"high_paym_A": 100, "low_paym_A": 0, "unico_paym_B": 18},
        {"high_paym_A": 100, "low_paym_A": 0, "unico_paym_B": 22},
        {"high_paym_A": 100, "low_paym_A": 0, "unico_paym_B": 26},
        {"high_paym_A": 100, "low_paym_A": 0, "unico_paym_B": 30},
        {"high_paym_A": 100, "low_paym_A": 0, "unico_paym_B": 34},
        {"high_paym_A": 100, "low_paym_A": 0, "unico_paym_B": 38},
        {"high_paym_A": 100, "low_paym_A": 0, "unico_paym_B": 42},
        {"high_paym_A": 100, "low_paym_A": 0, "unico_paym_B": 46},
        {"high_paym_A": 100, "low_paym_A": 0, "unico_paym_B": 50},
    ]
]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    first_choice_1 = models.IntegerField(verbose_name='Escojo la lotería A desde la opción 1 hasta la opción:', choices=Constants.choices_series1)
    second_choice_1 = models.IntegerField(verbose_name='Escojo la lotería B desde la opción:', choices=Constants.choices_series1)

    random_draw = models.IntegerField(min=1, max=10)
    random_lottery = models.IntegerField(min=1, max=10)
    selected_lottery = models.CharField()
    monedas_experimentales = models.IntegerField()

    def set_payoffs(self):
        self.random_draw = r.randrange(1, 11)
        self.random_lottery = r.randrange(1, 12)
        choices_aux_1 = 0

        if self.first_choice_1 != 0:
            choices_aux_1 = int(self.first_choice_1)

        # Esto ocurre si nunca se escogió la opción ninguna para la lotería A
        # Si la loteria escogia alet es menor o igual a mi primer punto de quiebre o segundo o 3ro, se juega A
        if (self.random_lottery <= choices_aux_1):

            self.selected_lottery = 'A'
            
            if self.random_draw <= 5:
                self.monedas_experimentales = Constants.lotteries[0][self.random_lottery - 1]["high_paym_A"]
                self.payoff = self.monedas_experimentales*Constants.valor_moneda_exp
            elif 5 < self.random_draw <= 10:
                self.monedas_experimentales = Constants.lotteries[0][self.random_lottery - 1]["low_paym_A"]
                self.payoff = self.monedas_experimentales*Constants.valor_moneda_exp

        # Si la loteria escogia alet es mayor a mi primer punto de quiebre o segundo o 3ro, o si nunca escogí
        # alguna loteria A, se juega B
        else:
            self.selected_lottery = 'B'
            self.monedas_experimentales = Constants.lotteries[0][self.random_lottery - 1]["unico_paym_B"]
            self.payoff = self.monedas_experimentales*Constants.valor_moneda_exp




################              PAGES                ###########################

class Introduction_0(Page):
    pass

class Introduction(Page):
    pass

class Example1(Page):
    pass


class Decision1(Page):
    form_model = 'player'
    form_fields = ['first_choice_1', 'second_choice_1']

    def before_next_page(player, timeout_happened):
        player.set_payoffs()

class Results(Page):
    
    def vars_for_template(player: Player):
        monedas_experimentales = player.monedas_experimentales
        return {"rpta": monedas_experimentales}


    
class Results_copy(Page):
    
    def vars_for_template(player: Player):
        monedas_experimentales = player.monedas_experimentales
        return {"rpta": monedas_experimentales}


page_sequence = [
    Introduction_0,
    Introduction, 
    Example1, 
    Decision1, 
    Results]
