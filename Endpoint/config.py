import os

class Config(object):
    SECRET_KEY ='lACLAVE'
class DevConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI='sqlite:////home/jahr/Documentos/Programas/Python/ProyectoSeg/envSeg/app/web/db/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS=False