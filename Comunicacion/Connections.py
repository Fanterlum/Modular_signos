import socket
import sys
import threading
PL_ADDRESS='0.0.0.0'      # para fuera de la red local 
L_ADDRESS='127.0.0.1'     # para fuera la red local 
P_PORT=80                 # puerto para conexiones publicas
DEFAULT_PORT_R=55555      # puerto por defecto buscar conexion
DEFAULT_PORT_LISTEN=50001 # puerto por defecto para escuchar 
DEFAULT_PORT_SEND=50002   # puerto por defecto para enviar
NONE_BIN=b'0'             # cadena binaria 0
class conection:
    def __init__(self,sAddr,sPort,dAddr,dPort) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(L_ADDRESS,sPort)
        self.source=(sAddr,sPort)
        self.destino=(dAddr,dPort)
    def listen():
        pass
    def send():
        pass


class Peer:
    def __init__(self) -> None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.localAddress=L_ADDRESS
        sock.bind(self.localAddress,DEFAULT_PORT_R)
        self.servers={
        }
        self.servers['searchP']=sock
        self.dataList={
            'default':[]
        }
        self.listens={
            'defaultLocal':threading.Thread(target=self.listen, daemon=True)
        }
        self.connected=False

    def connect(self,serverName,listenName):
        self.servers[serverName].sedto(NONE_BIN,)
        self.sock.sendto(NONE_BIN, self.servers[serverName])
        self.connected=True
        self.listens[listenName].start()

    def listen(self,serverName='defaultLocal',port=DEFAULT_PORT_LISTEN):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        address = (self.localAddress, port)
        sock.bind(address)
        while True:
            data = sock.recv(1024)
            self.dataList[serverName].append(data.decode())
    
    def addConection(self):
        pass

    def addListener(self):
        pass
    

class Router(Peer):
    def __init__(self) -> None:
        pass
class ServerCenter(Peer):
    def __init__(self) -> None:
        pass
