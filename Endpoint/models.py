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

    #Listas de enlaces
    Login=relationship("Login", back_populates="parentUser")
    Doctor_tipo=relationship("Doctor", back_populates="parentUser")
    Paciente_tipo=relationship("Paciente", back_populates="parentUser")
    Familiar_tipo=relationship("Familiar", back_populates="parentUser")

    '''@property
    def userPaciente(self):
        return self.Paciente_tipo[0]
    @property
    def userDoctor(self):
        return self.Doctor_tipo[0]
    @property
    def userFamiliar(self):
        return self.Familiar_tipo[0]'''
    
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
            "email":self.Login[0].getEmail(),
            "tipo":None
        }
        if self.tipo==0:
            user_dict["tipo"]="Paciente"
            user_dict["Doctor"]=self.Paciente_tipo[0].doctor_dict()
        elif self.tipo==1 :
            user_dict["tipo"]="Doctor"
            user_dict["Cedula profecional"]:self.Doctor_tipo[0].cedula_profecional
            user_dict["especialidad"]:self.Doctor_tipo[0].especialidad
            user_dict["pacientes"]=self.Doctor_tipo[0].pacientes_list()
        elif self.tipo==3:
            user_dict["tipo"]="Familiar"
            user_dict["pacientes"]=self.Familiar_tipo[0].pacientes_list()
        return user_dict

    
    
class Login(db.Model):
    __tablename__ = "Login"
    #id = db.Column(db.Integer,unique = True, primary_key=True)
    email = db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(66),nullable=False)

    #enlase FK con usuario 
    ID_user=db.Column(db.Integer,ForeignKey('User.id'),unique = True, primary_key=True)
    parentUser = relationship("User", back_populates="Login")
    
    def __init__(self,ID_user ):
        self.ID_user=ID_user

    def getEmail(self):
        return self.email
    
    def setEmail(self,email):
        self.email=email

    def setPassword(self,password):
        self.password=generate_password_hash(password)

    def checkPassword(self,password):
        return check_password_hash(self.password,password)
    
class Doctor(db.Model):
    __tablename__ = "Doctor"

    cedula_profecional = db.Column(db.String(30),nullable=False,unique = True, primary_key=True)
    especialidad = db.Column(db.String(30),nullable=False)

    #enlase FK con usuario 
    ID_user=db.Column(db.Integer,ForeignKey('User.id'),unique = True)
    parentUser = relationship("User", back_populates="Doctor_tipo")

    #Listas de enlaces
    Pacientes=relationship("Paciente", back_populates="parentDoctor")
    
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

    #enlase FK con usuario 
    ID_user=db.Column(db.Integer,ForeignKey('User.id'),unique = True, primary_key=True)
    parentUser = relationship("User", back_populates="Paciente_tipo")

    #enlase FK con Doctor
    cedulaDoc=db.Column(db.String(30),ForeignKey('Doctor.cedula_profecional'))
    parentDoctor = relationship("Doctor", back_populates="Pacientes")

    #enlase FK con Familiar
    ID_Fam=db.Column(db.String(30),ForeignKey('Familiar.ID_user'))
    parentFamiliar = relationship("Familiar", back_populates="Pacientes")
    

    def __init__(self,ID_user) -> None:
        self.ID_user=ID_user

    def setDoctor(self,cedulaDoc):
        self.cedulaDoc=cedulaDoc
    def setFamiliar(self,ID_Fam):
        self.ID_Fam=ID_Fam

    def to_dict(self):
        user = User.query.filter_by(id = self.ID_user).first()
        paciente_dict ={
            'id':user.id,
            'nombre':user.username,
            'status':"dead"
        }
        return paciente_dict
    
    '''def fam_list(self):
        if len(self.Familiares):
            return [familiar.to_dict() for familiar in self.Familiares]
        else:
            return "sin familiares"'''
    
    def doctor_dict(self):
        doc = Doctor.query.filter_by(cedula_profecional = self.cedulaDoc).first()
        if not doc is None:
            return doc.to_dict()
        else:
            return "Sin doctor"
class Familiar(db.Model):
    __tablename__ = "Familiar"
    #id = db.Column(db.Integer,unique = True, primary_key=True)

    #enlase FK con usuario 
    ID_user=db.Column(db.Integer,ForeignKey('User.id'),nullable=False,unique = True, primary_key=True)
    parentUser = relationship("User", back_populates="Familiar_tipo")

    #Listas de enlaces
    Pacientes=relationship("Paciente", back_populates="parentFamiliar")

    def __init__(self,ID_user) -> None:
        self.ID_user=ID_user

    '''def to_dict(self):
        user = User.query.filter_by(id = self.ID_user).first()
        fam_dict=user.to_dict()
        fam_dict.pop('paciente')
        return fam_dict'''
    
    def pacientes_list(self):
        if len(self.Pacientes):
            return [paciente.to_dict() for paciente in self.Pacientes]
        else:
            return "sin pacientes"
        
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