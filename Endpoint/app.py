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
@app.route('/user/<id>')#indicamos que es la ruta raíz 
def bRead(id):
    user = User.query.filter_by(id = id).first()

    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({'id':id})
    
@app.route('/userDele/<id>')#indicamos que es la ruta raíz 
def bDele(id):
    login= Login.query.filter_by(ID_user = id).first()
    user = User.query.filter_by(id = id).first()
    if user:
        if user.Paciente_tipo and user.tipo == 0 :
            db.session.delete(user.Paciente_tipo[0])
        elif user.Doctor_tipo and user.tipo == 1:
            db.session.delete(user.Doctor_tipo[0])
        elif user.Familiar_tipo and user.tipo == 2:
            db.session.delete(user.Familiar_tipo[0])
        db.session.delete(user)
    if login :
        db.session.delete(login)

    db.session.commit()
    return jsonify({'id':id})
@app.route('/userUpdate/<id>')#indicamos que es la ruta raíz 
def bUpdate(id):
    return jsonify({'id':id})

'''def http_Delete():
    login= Login.query.filter_by(email = request.args.get( 'email' )).first()
    if not login is None and login.checkPassword(request.args.get( 'Password' )):
        user = User.query.filter_by(id = login.ID_user).first()
        db.session.delete(user)
        db.session.commit()'''

def http_Update():
    '''
    if not login is None and login.checkPassword(request.args.get( 'Password' )):'''
    login= Login.query.filter_by(ID_user = request.args.get( 'id' )).first()
    user = User.query.filter_by(id = request.args.get( 'id' )).first()
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
    
    id_newDoc = request.args.get( 'newDoc' )
    id_newFam = request.args.get( 'newFam' )
    id_newPac = request.args.get( 'newPac' )
    print(id_newDoc)
    if user.tipo == 0:
        if user.Paciente_tipo:
            paciente = user.Paciente_tipo[0]
            if id_newFam:
                paciente.setFamiliar(id_newFam)
            if id_newDoc:
                paciente.setDoctor(id_newDoc)
    elif user.tipo==1:
        if user.Doctor_tipo:
            doc=user.Doctor_tipo[0]
            if id_newPac:
                doc.setPacientes(id_newPac)

                
    '''elif user.tipo == 1 and request.args.get( 'new' ):
        doc = Doctor.query.filter_by(ID_user = user.id).first()
        if not doc is None:
            paciente = Paciente.query.filter_by(ID_user = id_new).first()
            if not paciente is None:
                paciente.setDoctor(doc.cedula_profecional)'''

    db.session.commit()
    return jsonify({'result':'okey'})
def http_Create():
    user = User(
        username=request.args.get( 'username' ),
        apellidos=request.args.get( 'apellidos' ),
        tipo=request.args.get( 'tipo' ),
        fechaNacimiento=request.args.get( 'fechaNacimiento' )
    )
    db.session.add(user)
    db.session.commit()

    login = Login(user.id)

    '''print(user.id)
    print(request.args.get( 'Email' ))
    print(request.args.get( 'Email' ))'''
    login.setEmail(request.args.get( 'Email' ))
    login.setPassword(request.args.get( 'Password' ))
    
    db.session.add(login)

    if user.tipo == 0 :
        paciente=Paciente(user.id)
        db.session.add(paciente)

    elif user.tipo == 1 :
        if not request.args.get( 'cedula' ) is None:
            print( request.args.get( 'cedula' ) )
            doc=Doctor(request.args.get( 'cedula' ),user.id)
            db.session.add(doc)
        else:
            print( request.args.get( 'cedula' ) )
            #db.session.delete(login)
            db.session.delete(user)

    elif user.tipo == 2:
        fam=Familiar(user.id)
        db.session.add(fam)
        
    db.session.commit()
    return jsonify({'result':'okey'}) 

def http_Read():
    '''print(request)#control de petición
    print(request.args)#control parametros de petición 
    print(request.args.get('P1'))#control parametro1 de petición '''
    #busqueda en la base de datos
    login= Login.query.filter_by(email = request.args.get( 'email' )).first()
    if not login is None and login.checkPassword(request.args.get( 'Password' )):
        user = User.query.filter_by(id = login.ID_user).first()
        print(user.Doctor_tipo)
        if user.Paciente_tipo and user.tipo == 0 :
            return jsonify(user.Paciente_tipo[0].to_dict())
        elif user.Doctor_tipo and user.tipo == 1:
            return jsonify(user.Doctor_tipo[0].to_dict() )
        elif user.Familiar_tipo and user.tipo == 2:
            return jsonify(user.Familiar_tipo[0].to_dict())
    return jsonify({'user':None})
'''elif(request.args.get( 'historial' )):
            return user.Historial #encriptar json
        elif(request.args.get( 'ondas' )):
            return user.Ondas #encriptar json'''
def bLogin():
    login= Login.query.filter_by(email = request.args.get( 'email' )).first()
    if not login is None and login.checkPassword(request.args.get( 'Password' )):
        user = User.query.filter_by(id = login.ID_user).first()

        if user:
            return jsonify(
                {
                    'id':user.id,
                    'error':'Not error',
                    'logged':True
                }
            )
        else:
            return jsonify(
                {
                    'id':None,
                    'error':'Not user',
                    'logged':False
                }
            )
    else:
        return jsonify(
            {
                'id':None,
                'error':'password error',
                'logged':False
            }
        )

if __name__=='__main__': 
    db.init_app(app)#inicia el gestor db de la api
    
    with app.app_context():
        db.create_all()# crea la base de datos si no existe
        #app.add_url_rule('/DeleData',view_func=http_Delete)
        app.add_url_rule('/UpdtData',view_func=http_Update)
        app.add_url_rule('/CrteData',view_func=http_Create)
        app.add_url_rule('/ReadData',view_func=http_Read)
        app.add_url_rule('/BackLogin',view_func=bLogin)
        #link?data1=dat
    app.run(host='0.0.0.0',port=5000)#app.run(debug=True,port=puerto)#Depuración