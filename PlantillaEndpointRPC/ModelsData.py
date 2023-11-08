from sqlalchemy import Column, Integer, String,DateTime,LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
import datetime

# Crear una clase base para las entidades
db = declarative_base()

# Definir la entidad User
class User(db):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)

    Status=relationship("Status", back_populates="parentUser")
    Coordinates=relationship("Coordinates", back_populates="parentUser")
    CacheFiles=relationship("CacheFiles", back_populates="parentUser")

    def buildQueryInsert(self,username,email):
        return User.__table__.insert().values(username=username, email=email)
        #engine.connect().execute()

    def buildQuerySelect(self,user_id):
        return User.__table__.select().where(User.id == user_id)
        #engine.connect().execute()

    def buildQueryUpdate(self,user_id,new_username,new_email):
        return (
            User.__table__
            .update()
            .where(User.id == user_id)
            .values(username=new_username, email=new_email)
        )
    def buildQueryDelete(self,user_id):
        query = User.__table__.delete().where(User.id == user_id)
        #engine.connect().execute()
        return query
class CacheFiles(db):
    __tablename__ = "CacheFiles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ID_user=db.Column(db.Integer,ForeignKey('User.id'),unique = True, primary_key=True)
    parentUser = relationship("User", back_populates="CacheFiles")
    file = Column(LargeBinary)
    tipe = Column(String)
    date = Column(DateTime,default=datetime.datetime.now)

class Status(db):
    __tablename__ = "Status"
    id = Column(Integer, primary_key=True, autoincrement=True)

    ID_user=db.Column(db.Integer,ForeignKey('User.id'),unique = True, primary_key=True)
    parentUser = relationship("User", back_populates="Status")

    data = Column(Integer, nullable=False)
    date = Column(DateTime,default=datetime.datetime.now)
    
    def __str__(self) -> str:
        return f'{self.id}|{self.data}|{self.date}'
class Coordinates(db):
    __tablename__ = "Coordinates"
    id = Column(Integer, primary_key=True, autoincrement=True)

    ID_user=db.Column(db.Integer,ForeignKey('User.id'),unique = True, primary_key=True)
    parentUser = relationship("User", back_populates="Coordinates")

    PRIMER_PUNTO_X = Column(Integer, nullable=False)
    PRIMER_PUNTO_Y = Column(Integer, nullable=False)
    PUNTO_MAS_ALTO_X = Column(Integer, nullable=False)
    PUNTO_MAS_ALTO_Y = Column(Integer, nullable=False)
    PUNTO_FINAL_X = Column(Integer, nullable=False)
    PUNTO_FINAL_Y = Column(Integer, nullable=False)
    Q_SIGNAL_X = Column(Integer, nullable=False)
    Q_SIGNAL_Y = Column(Integer, nullable=False)
    S_SIGNAL_X = Column(Integer, nullable=False)
    S_SIGNAL_Y = Column(Integer, nullable=False)
    T_SIGNAL_X = Column(Integer, nullable=False)
    T_SIGNAL_Y = Column(Integer, nullable=False)
    P_SIGNAL_X = Column(Integer, nullable=False)
    P_SIGNAL_Y = Column(Integer, nullable=False)
    def __init__(self, first_point, lower_x_pos, lower_y, final_point, QSignal, QSignal2, lower_point_startQ, lower_point_startP):
        self.PRIMER_PUNTO_X = int(first_point[0])
        self.PRIMER_PUNTO_Y = int(first_point[1])
        self.PUNTO_MAS_ALTO_X = int(lower_x_pos)
        self.PUNTO_MAS_ALTO_Y = int(lower_y)
        self.PUNTO_FINAL_X = int(final_point[0])
        self.PUNTO_FINAL_Y = int(final_point[1])
        self.Q_SIGNAL_X = int(QSignal[0])
        self.Q_SIGNAL_Y = int(QSignal[1])
        self.S_SIGNAL_X = int(QSignal2[0])
        self.S_SIGNAL_Y = int(QSignal2[1])
        self.T_SIGNAL_X = int(lower_point_startQ[0])
        self.T_SIGNAL_Y = int(lower_point_startQ[1])
        self.P_SIGNAL_X = int(lower_point_startP[0])
        self.P_SIGNAL_Y = int(lower_point_startP[1])
class Chat(db):
    __tablename__ = "Chat"
    id = Column(Integer, primary_key=True, autoincrement=True)

    ID_user=db.Column(db.Integer,ForeignKey('User.id'),unique = True, primary_key=True)
    parentUser = relationship("User", back_populates="Chat")

    msg = Column(String)
    tipe = Column(Integer)
    #-1 respuesta de chatbot
    #1 msg de Paciente
    date = Column(DateTime,default=datetime.datetime.now)
'''# Uso de la clase
first_point = (10, 20)
lower_x_pos = 30
lower_y = 40
final_point = (50, 60)
QSignal = (70, 80)
QSignal2 = (90, 100)
lower_point_startQ = (110, 120)
lower_point_startP = (130, 140)

coordinates = Coordinates(first_point, lower_x_pos, lower_y, final_point, QSignal, QSignal2, lower_point_startQ, lower_point_startP)

# Acceso a los valores
print(coordinates.PRIMER_PUNTO_X)
print(coordinates.PRIMER_PUNTO_Y)
# ... y así sucesivamente para el resto de los atributos'''
