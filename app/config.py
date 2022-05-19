import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # ...
    MONGODB_SETTINGS = {
        "DB": "NEWMONGO",
        'host': 'localhost'
    }
