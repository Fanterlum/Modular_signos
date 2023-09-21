from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

import datetime
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer,unique = True,nullable=False, primary_key=True)
    username = db.Column(db.String(50),unique = False,nullable=False)
    apellidos = db.Column(db.String(50),unique = False,nullable=False)
    tipo= db.Column(db.Integer,unique = False,nullable=False)
    fechaNacimiento=db.Column(db.DateTime,default=datetime.datetime.now)

    Login=relationship("Login")
    Doctor_tipo=relationship("Doctor")
    Paciente_tipo=relationship("Paciente")
    Familiar_tipo=relationship("Familiar")

    @property
    def userPaciente(self):
        return self.Paciente_tipo[0]
    @property
    def userDoctor(self):
        return self.Doctor_tipo[0]
    @property
    def userFamiliar(self):
        return self.Familiar_tipo[0]
    def __init__(self, username,apellidos,tipo,fechaNacimiento):
        self.username=username
        self.apellidos=apellidos
        self.tipo=tipo
        self.fechaNacimient=fechaNacimiento
    def to_dict(self):
        user_dict={
            "id":self.id,
            "username":self.username,
            "apellidos":self.apellidos,
            "fechaNacimient":self.fechaNacimiento,
            "email":self.Login[0].Email,
            "tipo":None
        }
        if self.tipo==0:
            user_dict["tipo"]="Paciente"
            user_dict["Doctor"]=self.Paciente_tipo[0].doctor_dict()
            user_dict["familiares"]=self.Paciente_tipo[0].fam_list()
        elif self.tipo==1:
            user_dict["tipo"]="Doctor"
            user_dict["Cedula profecional"]:self.Doctor_tipo[0].cedula_profecional
            user_dict["especialidad"]:self.Doctor_tipo[0].especialidad
            user_dict["pacientes"]=self.Doctor_tipo[0].pacientes_list()
        elif self.tipo==3:
            user_dict["tipo"]="Familiar"
            user_dict["paciente"]=self.Familiar_tipo[0].paciente_dict()

    
    
class Login(db.Model):
    __tablename__ = "Login"
    #id = db.Column(db.Integer,unique = True, primary_key=True)
    email = db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(66),nullable=False)
    ID_user=db.Column(db.Integer,ForeignKey('User.id'),unique = True, primary_key=True)

    @property
    def Email(self,email):
        self.email=email
    def Email(self):
        return self.email
    
    def setPassword(self,password):
        self.passwordl=generate_password_hash(password)
    def checkPassword(self,password):
        return check_password_hash(self.password,password)
    
class Doctor(db.Model):
    __tablename__ = "Doctor"
    cedula_profecional = db.Column(db.String(30),nullable=False,unique = True, primary_key=True)
    ID_user=db.Column(db.Integer,ForeignKey('User.id'),unique = True)
    especialidad = db.Column(db.String(30),nullable=False)
    Pacientes=relationship("Paciente")
    
    def __init__(self,cedula_profecional,ID_user,especialidad="cardiologo") -> None:
        self.cedula_profecional=cedula_profecional
        self.ID_user=ID_user
        self.especialidad=especialidad
    def to_dict(self):
        user = User.query.filter_by(id = self.ID_user).first()
        doc_dict =user.to_dict()
        doc_dict.pop("pacientes")
        return doc_dict
    def pacientes_list(self):
        if len(self.Pacientes):
            return [paciente.to_dict() for paciente in self.Pacientes]
        else:
            return "sin pacientes"

class Paciente(db.Model):
    __tablename__ = "Paciente"
    #id = db.Column(db.Integer,unique = True, primary_key=True)
    ID_user=db.Column(db.Integer,ForeignKey('User.id'), primary_key=True,unique = True)
    cedulaDoc=db.Column(db.String(30),ForeignKey('Doctor.cedula_profecional'))
    Familiares=relationship("Familiar")

    def __init__(self,ID_user) -> None:
        self.ID_user=ID_user
    def setDoctor(self,cedulaDoc):
        self.cedulaDoc=cedulaDoc
    def to_dict(self):
        user = User.query.filter_by(id = self.ID_user).first()
        paciente_dict = user.to_dict()
        paciente_dict.pop("Doctor")
        return paciente_dict
    def fam_list(self):
        if len(self.Familiares):
            return [familiar.to_dict() for familiar in self.Familiares]
        else:
            return "sin familiares"
    def doctor_dict(self):
        doc = Doctor.query.filter_by(cedula_profecional = self.cedulaDoc).first()
        if not doc is None:
            return doc.to_dict()
        else:
            return "Sin doctor"
class Familiar(db.Model):
    __tablename__ = "Familiar"
    ID_user=db.Column(db.Integer,ForeignKey('User.id'),nullable=False,unique = True, primary_key=True)
    ID_Paciente=db.Column(db.Integer,ForeignKey('Paciente.ID_user'),nullable=True)
    ID_Doctor=db.Column(db.Integer,ForeignKey('Paciente.cedulaDoc'),nullable=True)
    #Paciente=relationship("Paciente")

    def __init__(self,ID_user) -> None:
        self.ID_user=ID_user
    def setPaciente(self,ID_Paciente,ID_Doctor):
        self.ID_Paciente=ID_Paciente
        self.ID_Doctor=ID_Doctor
    def to_dict(self):
        user = User.query.filter_by(id = self.ID_user).first()
        fam_dict=user.to_dict()
        fam_dict.pop('paciente')
        return fam_dict
    
    def paciente_dict(self):
        paciente = Paciente.query.filter_by(ID_user = self.ID_Paciente).first()
        if not paciente is None:
            return paciente.to_dict()
        else:
            return "Sin Paciente"
        
'''class Historial(db.Model):
    __tablename__ = "Historial"
    id = db.Column(db.Integer,unique = True, primary_key=True)
    ID_user=db.Column(db.Integer,ForeignKey('User.id'))
    fecha = db.Column(db.DateTime,default=datetime.datetime.now)
    def to_dict(self):
        return {}
    
class Onda(db.Model):
    __tablename__ = "Onda"
    id = db.Column(db.String(30),nullable=False,unique = True, primary_key=True)
    ID_user=db.Column(db.Integer,ForeignKey('User.id'))
    def to_dict(self):
        return {}'''