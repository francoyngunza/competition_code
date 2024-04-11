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
    universidad = models.StringField(
        choices=[['up', 'Universidad del Pacífico'], ['udep', 'Universidad de Lima'], ['pucp','PUCP'], ['upc', 'UPC'], ['otro','Otros']],
        label='¿En que universidad estudias?',
        widget=widgets.RadioSelect,
    )


    
# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'carrera', 'distrito','universidad']




page_sequence = [Demographics]
