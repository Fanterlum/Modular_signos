import socket
import sys
import threading
import base64
import zlib
#from hashlib import sha512
#from xmlrpc.server import SimpleXMLRPCServer

PL_ADDRESS = '0.0.0.0'      # para fuera de la red local 
L_ADDRESS = '127.0.0.1'     # para fuera la red local 
P_PORT = 80                 # puerto para conexiones publicas
DEFAULT_PORT_R = 55555      # puerto por defecto buscar conexion
DEFAULT_PORT_LISTEN = 50001 # puerto por defecto para escuchar 
DEFAULT_PORT_SEND = 50002   # puerto por defecto para enviar
NONE_BIN = b'0'             # cadena binaria 0
CHUNK_SIZE = 5 * 1024
def codex(dat):
    encoded_dat = base64.urlsafe_b64encode(dat)
    compres_dat = zlib.compress(encoded_dat)
    return compres_dat
def decodex(dat):
    decompres_dat = zlib.decompress(dat)
    decoded_dat = base64.urlsafe_b64decode(decompres_dat)
    return decoded_dat
class Conection:
    def __init__(self,hostname,sPort) -> None:
        self.listenPort=DEFAULT_PORT_LISTEN
        self.destino=None
        #self.source=(socket.gethostbyname(hostname),sPort)
        self.__archList=[]
        self.smgList=[]
        self.log=[]
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(L_ADDRESS,sPort)
        listener = threading.Thread(target=self.listen, daemon=True)
        listener.start()
    @property
    def archList(self):
        return self.__archList
    @property
    def smgList(self):
        return self.smgList
    @property
    def log(self):
        return self.log
    
    def setDestino(self,dAddr,dPort):
        self.destino=(dAddr,dPort)
    @property
    def addres(self):
        return self.destino

    def setListenPort(self,lPort):
        self.listenPort=lPort
        self.sock.sendto(b'newLP',self.destino)
        self.sock.sendto(f'{lPort}'.encode())
    @property
    def listenPort(self):
        return self.listenPort

    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((PL_ADDRESS, self.listenPort))# se define el puerto de envio 50001
    
        while True:
            fdata=sock.recv(100).decode()
            #se resiben buffer de binarios de 1024 digitos de longitud
            data = decodex(sock.recv(CHUNK_SIZE))
            if 'msg'== fdata:
                #mensajes
                print('\rpeer: {}\n> '.format(data), end='')
            elif 'arch'== fdata:
                #archivos 
                #codigo comentado en test.py
                #decompres_file = zlib.decompress(data)
                #decoded_file = base64.urlsafe_b64decode(decompres_file)
                print(len(data))
                #print('\rpeer: {}\n> '.format(data), end='')
                chunk=data
                while chunk:
                    self.__archList.append(chunk)
                    chunk=decodex(sock.recv(CHUNK_SIZE))
                self.__archList.append(sock.recvfrom(128))
            elif 'newLP'== fdata:
                self.destino(self.destino[0],data.decode())
    def sendArch(self,name="JS_2_3.json"):
        
        #...arcivos
        #codigo comentado en test.py
        #arch= input('> ')
        if not self.destino is None:
            self.sock.sendto(b'arch', self.destino)
            with open(name,"rb") as fileBin:
                #encoded_file = base64.urlsafe_b64encode(fileBin.read())
                #compres_file = zlib.compress(encoded_file)
                #se envia el binario del archivo codificado y Comprimido
                data = fileBin.read(CHUNK_SIZE)
                while data:
                    self.sock.sendto(codex(data), self.destino)
                    data = fileBin.read(CHUNK_SIZE)
                self.sock.sendto(NONE_BIN, self.destino)
                #self.sock.sendto(codex(fileBin), self.destino)


    def sendMSN(self,msg):
        #...mensajes
        #msg = input('> ')
        #se envia la cadena de texto codificada y comprimida en binario
        if not self.destino is None:
            self.sock.sendto(b'msg', self.destino)
            self.sock.sendto(codex(msg), self.destino)


class Peer:
    def __init__(self) -> None:
        self.conections = []
        self.servers = []
        self.name = 'partyGoer'
        self.hostname = socket.gethostname()
    @property
    def peerName(self):
        return self.name
    @property
    def ipSource(self):
        return socket.gethostbyname(self.hostname)
    
    def getDestino(self,nDest):
        return self.conections[nDest]
    def setDestino(self,dAddr,dPort,sendPort=DEFAULT_PORT_SEND):
        newConection = Conection(self.hostname,sendPort)
        newConection.setDestino(dAddr,dPort)
        self.conections.append(newConection)
    def __len__(self):
        return len(self.conections)
    

class Router(Peer):
    def __init__(self) -> None:
        pass
    def __len__(self):
        return len(self.servers)
class ServerCenter(Peer):
    def __init__(self) -> None:
        self.name="partyHost"
        self.routers=[]
        self.peers=[]
    def getServerList(self):
        pass
    def getPartyChat(self):
        pass
    def getPartyFlags(self):
        pass
    def getPartyArch(self):
        pass
    def __len__(self):
        return len(self.peers)