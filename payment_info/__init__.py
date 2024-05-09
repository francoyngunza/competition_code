from otree.api import *



doc = """
This application provides a webpage instructing participants how to get paid.
Examples are given for the lab and Amazon Mechanical Turk (AMT).
"""


class C(BaseConstants):
    NAME_IN_URL = 'payment_info'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    
    def vars_for_admin_report(self):

        apps = self.session.config['app_sequence'][1:-1]

        players = self.get_players()
        payments = {}
        for player in players:
            player_payments = {}
            total = 0
            # player_payments['id'] = player.id_in_group
            for app in apps:
                player_payments[app] = player.participant.vars['payoff_'+app]
                total += player_payments[app]
            player_payments['Total'] = total + 5

            payments[player.id_in_group] = player_payments 
            
        return dict(
                payments = payments
            )


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    pass


# FUNCTIONS
# PAGES
class Pagos(Page):
    pass
        # def vars_for_template(self):
    #     participant.payoff_plus_participation_fee()

    #     pago_total = 0

    #     for app in self.session.config['app_sequence'][1:-1]:

    #         pago = self.player.participant.vars['payoff_'+app]

    #         pago_total += pago

    #     return dict(
    #         pago_total = pago_total,
    #         participant_fee = self.session.config["participant_fee"],
    #         pago_total_fee = pago_total + self.session.config["participant_fee"],
    #     )


page_sequence = [Pagos]
