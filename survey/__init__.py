from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='Edad', min=18, max=100)

    gender = models.StringField(
        choices=[['H', 'Hombre'], ['F','Mujer']],
        label='Sexo',
        widget=widgets.RadioSelect,
    )
    
    carrera = models.StringField(
        choices=['Economía', 'Administración', 'Ingeniería', 'Negocios internacionales', 'Marketing', 'Otro'],
        label='Carrera',
        widget=widgets.RadioSelect,
    )

    distrito = models.StringField(label='Distrito de residencia:')
    
    # ocup = models.StringField(
    #     choices=[['estu', 'estudiante'], ['egre', 'egresado']],
    #     label='Ocupación',
    #     widget=widgets.RadioSelect,
    # )
    # labor = models.StringField(
    #     choices=[['T', 'Trabajo'], ['NT', 'No Trabajo']],
    #     label='¿Estás trabajando?',
    #     widget=widgets.RadioSelect,
    # )
    ciclo = models.StringField(
        choices=[['1', 'Primer'], ['2', 'Segundo'], ['3','Tercero'], ['4', 'Cuarto'], ['5', 'Quinto'], ['6', 'Sexto'], ['7','Sétimo'], ['8', 'Octavo'], ['9','Noveno'], ['10', 'Décimo']],
        label='¿En que ciclo te encuentras actualmente?',
        widget=widgets.RadioSelect,
    )


    
# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'carrera', 'distrito','ciclo']




page_sequence = [Demographics]
