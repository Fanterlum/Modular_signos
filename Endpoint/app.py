#Se importa de flask los objetos que ocuparemos 
from flask import Flask
from flask import request
#Se importa configoraciones de desarrollo 
from config import DevConfig 
#Se importa configuraciones de la base de datos 
from BDManager import DatabaseManager as db_CRUD
from models import db
from models import User
from models import Login
#Se importa configuraciones de la base de datos y comunicaciones
from Comunicacion.Connections import RPC as epRPC
#se declara un gestor de Base de datos mediante RPC
endPoindRPC=epRPC()
endPoindRPC.appJoined(db_CRUD)#se agregan entrada de instruciones para manejar la base de datos por RPC
#se inicializa la API 
app=Flask(__name__) 
app.config.from_object(DevConfig)#se agrega la configuracion

def endPoint_http():
    #busqueda en la base de datos
    login= Login.query.filter_by(password = request.args.get( 'password' )).first()
    if not login is None :
        user = User.query.filter_by(id = login.ID_user).first()
        print(user.Login[0].email)
        print(user.Historial)
        print(user.Ondas)
        print(user.Doctor)
        print(user.Pacientes)
        print(user.Familiares)
        print(request)#control de petición
        print(request.args)#control parametros de petición 
        print(request.args.get('P1'))#control parametro1 de petición 

    else:
        pass
    
    return login.email#encriptar

if __name__=='__main__': 
    db.init_app(app)#inicia el gestor db de la api
    
    with app.app_context():
        db.create_all()# crea la base de datos si no existe
        app.add_url_rule('/UserData',view_func=endPoint_http)#consulta de la tabla usuario y login con api de flask
        #link?data1=dat
    app.run(port=5000)#app.run(debug=True,port=puerto)#Depuración