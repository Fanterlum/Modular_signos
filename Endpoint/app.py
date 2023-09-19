#Se importa de flask los objetos que ocuparemos 
from flask import Flask, request, jsonify
#Se importa configoraciones de desarrollo 
from config import DevConfig 
#Se importa configuraciones de la base de datos 
#from BDManager import DatabaseManager as db_CRUD
from models import db, User, Login, Paciente, Doctor, Familiar
#Se importa configuraciones de la base de datos y comunicaciones
#from Comunicacion.Connections import RPC as epRPC
#se declara un gestor de Base de datos mediante RPC
#endPoindRPC=epRPC()
#endPoindRPC.appJoined(db_CRUD)#se agregan entrada de instruciones para manejar la base de datos por RPC
#se inicializa la API 
app=Flask(__name__) 
app.config.from_object(DevConfig)#se agrega la configuracion
@app.route('/')#indicamos que es la ruta raíz 
def index():
    return "Endpoint"
@app.route('/test')#indicamos que es la ruta raíz 
def testjson():
    return jsonify(request.args.to_dict())
def http_Delete():
    login= Login.query.filter_by(email = request.args.get( 'email' )).first()
    if not login is None and login.checkPassword(request.args.get( 'Password' )):
        user = User.query.filter_by(id = login.ID_user).first()
        db.session.delete(user)
        db.session.commit()

def http_Update():
    login= Login.query.filter_by(email = request.args.get( 'email' )).first()
    if not login is None and login.checkPassword(request.args.get( 'Password' )):
        user = User.query.filter_by(id = login.ID_user).first()
        if (request.args.get( 'username' )):
            user.username=request.args.get( 'username' )
        if (request.args.get( 'apellidos' )):
            user.apellidos=request.args.get( 'apellidos' )
        if (request.args.get( 'fechaNacimiento' )):
            user.fechaNacimiento=request.args.get( 'fechaNacimiento' )
        if (request.args.get( 'email' )):
            login.setEmail(request.args.get( 'Email' ))
        if (request.args.get( 'Password' )):
            login.setPassword(request.args.get( 'Password' ))
        
        id_new = request.args.get( 'new' )

        if user.tipo == 0 and id_new:
            paciente = Paciente.query.filter_by(ID_user = user.id).first()
            if not paciente is None:
                fam = Familiar.query.filter_by(ID_user = id_new).first()
                if not fam is None:
                    fam.setPaciente(id_new,paciente.cedulaDoc)
                
        elif user.tipo == 1 and request.args.get( 'new' ):
            doc = Doctor.query.filter_by(ID_user = user.id).first()
            if not doc is None:
                paciente = Paciente.query.filter_by(ID_user = id_new).first()
                if not paciente is None:
                    paciente.setDoctor(doc.cedula_profecional)

        db.session.commit()
                
def http_Create():
    user = User(
        username=request.args.get( 'username' ),
        apellidos=request.args.get( 'apellidos' ),
        tipo=request.args.get( 'tipo' ),
        fechaNacimiento=request.args.get( 'fechaNacimiento' )
    )
    login = Login()
    login.setEmail(request.args.get( 'Email' ))
    login.setPassword(request.args.get( 'Password' ))
    db.session.add(user)
    db.session.add(login)
    

    if user.tipo == 0 :
        paciente=Paciente(user.id)
        db.session.add(paciente)

    elif user.tipo == 1 and not request.args.get( 'cedula' ) is None:
        doc=Doctor(request.args.get( 'cedula' ),user.id)
        db.session.add(doc)

    elif user.tipo == 2:
        fam=Familiar(user.id)
        db.session.add(fam)
        
    db.session.commit()

def http_Read():
    print(request)#control de petición
    print(request.args)#control parametros de petición 
    print(request.args.get('P1'))#control parametro1 de petición 
    #busqueda en la base de datos
    login= Login.query.filter_by(email = request.args.get( 'email' )).first()
    if not login is None and login.checkPassword(request.args.get( 'Password' )):
        user = User.query.filter_by(id = login.ID_user).first()

        if(request.args.get( 'user' )):
            return jsonify(user.to_dict())
        elif(request.args.get( 'Pacientes' )) and user.tipo == 0 :
            return jsonify(user.userPaciente.to_dict())
        elif(request.args.get( 'Doctor' ))and user.tipo == 1:
            return jsonify(user.userDoctor.to_dict() )
        elif(request.args.get( 'Familiares' ))and user.tipo == 2:
            return jsonify(user.userFamiliar.to_dict())

    else:
        pass
    
    return #encriptar
'''elif(request.args.get( 'historial' )):
            return user.Historial #encriptar json
        elif(request.args.get( 'ondas' )):
            return user.Ondas #encriptar json'''
if __name__=='__main__': 
    db.init_app(app)#inicia el gestor db de la api
    
    with app.app_context():
        db.create_all()# crea la base de datos si no existe
        app.add_url_rule('/DeleData',view_func=http_Delete)#consulta de la tabla usuario y login con api de flask
        app.add_url_rule('/UpdtData',view_func=http_Update)
        app.add_url_rule('/CrteData',view_func=http_Create)
        app.add_url_rule('/ReadData',view_func=http_Read)
        #link?data1=dat
    app.run(host='0.0.0.0',port=5000)#app.run(debug=True,port=puerto)#Depuración