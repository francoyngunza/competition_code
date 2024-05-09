from os import environ

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1, participation_fee=5.00, doc=""
)

PARTICIPANT_FIELDS = ['expiry']

SESSION_CONFIGS = [
    dict(
        name='exp_competencia',
        display_name="Competencia",
        participant_fee = SESSION_CONFIG_DEFAULTS["participation_fee"],
        app_sequence=['survey','Parte_1','Asignacion_Primera_Parte','Parte_2_Control','Parte_2_Tratamiento','Parte_3','Parte_4','Parte_5','payment_info'],
        num_demo_participants=4,
    ),
    dict(
        name='tanaka',
        display_name="measure_task",
        app_sequence=['Parte_1'],
        num_demo_participants=2,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'es'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'PEN'
USE_POINTS = False

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(
        name='e2labup',
        display_name='E2LabUP - Room para sesiones online',
        participant_label_file='_rooms/e2labup-room.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '2276414296938'

INSTALLED_APPS = ['otree']
