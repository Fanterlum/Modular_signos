from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

import datetime
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer,unique = True, primary_key=True)
    username = db.Column(db.String(50),unique = True,nullable=False)
    apellidos = db.Column(db.String(50),unique = True,nullable=False)
    tipo= db.Column(db.Integer,unique = False, primary_key=True)
    fechaNacimiento=db.Column(db.DateTime,default=datetime.datetime.now)

    Login=relationship("Login")
    Historial=relationship("Historial")
    Ondas=relationship("Onda")
    Doctor=relationship("Doctor")
    Pacientes=relationship("Paciente")
    Familiares=relationship("Familiar")

    def __init__(self, username):
        self.username=username

    
    
class Login(db.Model):
    __tablename__ = "Login"
    email = db.Column(db.String(30),nullable=False)
    password = db.Column(db.String(66),nullable=False)
    ID_user=db.Column(db.Integer,ForeignKey('User.id'))

    def setEmail(self,email):
        self.email=email
    def getEmail(self):
        return self.email
    
    def setPassword(self,password):
        self.passwordl=generate_password_hash(password)
    def checkPassword(self,password):
        return check_password_hash(self.password,password)
    
class Historial(db.Model):
    __tablename__ = "Historial"
    ID_user=db.Column(db.Integer,ForeignKey('User.id'))
    fecha = db.Column(db.DateTime,default=datetime.datetime.now)
    
class Onda(db.Model):
    __tablename__ = "Onda"
    ID_user=db.Column(db.Integer,ForeignKey('User.id'))
    id = db.Column(db.String(30),nullable=False)

class Doctor(db.Model):
    __tablename__ = "Doctor"
    ID_user=db.Column(db.Integer,ForeignKey('User.id'))
    cedula_profecional = db.Column(db.String(30),nullable=False)
    especialidad = db.Column(db.String(30),nullable=False)
    Pacientes=relationship("Paciente")

class Paciente(db.Model):
    __tablename__ = "Paciente"
    ID_user=db.Column(db.Integer,ForeignKey('User.id'))
    cedulaDoc=db.Column(db.Integer,ForeignKey('Doctor.cedula_profecional'))
    Familiares=relationship("Familiar")

class Familiar(db.Model):
    __tablename__ = "Familiar"
    ID_user=db.Column(db.Integer,ForeignKey('User.id'))
    id = db.Column(db.String(30),nullable=False)
    Paciente=relationship("Paciente")