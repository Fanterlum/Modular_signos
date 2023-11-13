from ModelsData import db,Coordinates,Status
from BDPluss import DBManager
from Connections import DEFAULT_PORT_F,RPC,UDP,Peer#,MasterTCP
import time,os
udp = UDP()
#Status
#Coordinates
def getStatus(id)-> dict:
    status=str(data_base.Conn.query(Status).get(id))
    print(f'drop:{status}')
    return status
def setStatus(data):
    new_status=Status(data=data)
    data_base.Conn.add(new_status)
    data_base.Conn.commit()
    print(f'New:{new_status}')
    return 0

def getCoordinates(id)-> dict:
    status=str(data_base.Conn.query(Coordinates).get(id))
    print(f'drop:{status}')
    return id
def setCoordinates(id):
    new_Coordinate=Coordinates(id)
    data_base.Conn.add(new_Coordinate)
    data_base.Conn.commit()
    #print(f'New:{new_Coordinate}')


    return 0

def newCache(id,block_files)-> dict:
    try:
        return 0
    except:
        return 1
    
#debug
def genCache():
    try:
        return 0
    except:
        return 1

def sincronice(dest):#Sincronisacion UDP
    print('server sincronice!!! o_0')
    udp.sendFlag((ipEndpoint,DEFAULT_PORT_F),'addme')
    while True:
        udp.sendFlag((ipEndpoint,DEFAULT_PORT_F),'dropme',dest)
        ipDestino=udp.Peers.get(dest,None)
        if ipDestino:return ipDestino
        else:print(f'Esperando a {dest}')
        time.sleep(5)
        os.system ("clear")
def alive(frace):#ping rpc
    if frace=='okey?':
        return 'okey'
    return False
    
if __name__=='__main__': 
    #ipEndpoint=input('Endpoint ip: ')
    print('1)   vision')
    print('2)   prediccion')
    print('3)   Bpi')
    n=int(input('peer: '))
    if n==2:
        nameDest='vision'
        name='prediccion'
    elif n==1:
        nameDest='prediccion'
        name='vision'
    elif n==3:
        paciente_id=input('ID: ')
        nameDest='vision'
        name=f'Bpi[paciente:{paciente_id}]'
    #Conectarse a la base de datos
    data_base=DBManager()
    data_base.dbConn_ORM()
    # Crear la tabla en la base de datos
    db.metadata.create_all(data_base.Engine)
    
    udp.setNickname(name)
    udp.register_function(genCache)

    #endpoint server 
    endpoint_rpc = RPC()
    endpoint_rpc.serviceJoined(endpoint_rpc.ipSource)
    endpoint_rpc.Joined.register_function(alive)
    endpoint_rpc.Joined.register_function(newCache)
    if n==1:
        endpoint_rpc.Joined.register_function(setStatus)
        endpoint_rpc.Joined.register_function(getStatus)
    elif n==2:
        endpoint_rpc.Joined.register_function(setCoordinates)
        endpoint_rpc.Joined.register_function(getCoordinates)
    if n==3:
        pass
    #addres=sincronice(nameDest)
    endpoint_rpc.starListener()
    #endpoint_rpc.appOnion(f'http://{addres}:20064')
    
    print(endpoint_rpc.ipSource)
    while True:pass
        #try:
           # print(f"server {nameDest} is {endpoint_rpc.getOnion(0).alive('okey?')}")
        #except:
        #    print('server error !!! 0_o')
            #addres=sincronice(nameDest)
        #if n==1 or n==2:
       # udp.sendFlag((addres,DEFAULT_PORT_F),'func','genCache')
        #time.sleep(15)
        

