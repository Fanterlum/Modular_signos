from ModelsData import db,Coordinates,Status
from BDPluss import DBManager
from Connections import RPC
#Status
#Coordinates
def getStatus(id):
    status=str(data_base.Conn.query(Status).get(id))
    print(f'drop:{status}')
    return status
def setStatus(data):
    new_status=Status(data=data)
    data_base.Conn.add(new_status)
    data_base.Conn.commit()
    print(f'New:{new_status}')
    return 0
def getCoordinates(d):
    print(d)
    return d
def setCoordinates(d):
    print(d)
    return d
if __name__=='__main__': 
    #Conectarse a la base de datos
    data_base=DBManager()
    data_base.dbConn_ORM()
    # Crear la tabla en la base de datos
    db.metadata.create_all(data_base.Engine)
    #endpoint server 
    endpoint_rpc = RPC()
    endpoint_rpc.serviceJoined(endpoint_rpc.ipSource)
    endpoint_rpc.Joined.register_function(setStatus)
    endpoint_rpc.Joined.register_function(getStatus)
    endpoint_rpc.starListener()
    print(endpoint_rpc.ipSource)
    getStatus(3)
    while True:pass