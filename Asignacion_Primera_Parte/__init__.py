from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'asignacion_1'
    PLAYERS_PER_GROUP = None  # You can set this to a specific number if needed
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):
    complicada = models.BooleanField()

class MyWaitPage(WaitPage):
    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        if player.complicada:
            return "Parte_2_Control"
        else:
            return "Parte_2_Tratamiento"
        
def creating_session(subsession):
    import itertools
    pressures = itertools.cycle([True, False])
    for player in subsession.get_players():
        player.complicada = next(pressures)
        
page_sequence = [MyWaitPage]
