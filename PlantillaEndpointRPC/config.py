import os

class Config(object):
    SECRET_KEY ='lACLAVE'
class DevConfig(Config):
    DEBUG=True
    DATABASE_URI='sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),'db/app.db')
    