import socket
import sys
import threading
import base64
import zlib
#from hashlib import sha512
#from xmlrpc.server import SimpleXMLRPCServer
'''TCP es un protocolo orientado a la conexión mientras que UDP no utiliza 
conexión. TCP establece una conexión entre un remitente y un receptor antes 
de que se puedan enviar los datos. UDP en cambio, no establece ninguna 
conexión antes de enviar los datos.'''
PL_ADDRESS = '0.0.0.0'      # para fuera de la red local 
L_ADDRESS = '127.0.0.1'     # para fuera la red local 
P_PORT = 80                 # puerto para conexiones publicas
DEFAULT_PORT_R = 55555      # puerto por defecto escuchar flags
DEFAULT_PORT_LMSG = 50001 # puerto por defecto para escuchar msg
DEFAULT_PORT_LARCH = 50011 # puerto por defecto para escuchar arch
DEFAULT_PORT_SEND = 50002   # puerto por defecto para enviar
DEFAULT_PORT_DARCH = 50007   # puerto por defecto para duplex msg
DEFAULT_PORT_DMSG = 50008   # puerto por defecto para duplex arch
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

class HostUDP:
    def __init__(self,sPort) -> None:
        #self.listenPort=DEFAULT_PORT_LISTEN
        self.destino=None
        #self.source=(socket.gethostbyname(hostname),sPort)
        
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(L_ADDRESS,sPort)
        listener = threading.Thread(target=self.listen, daemon=True)
        listener.start()
    
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

    
    def sendArch(self,name="JS_2_3.json"):
        
        #...arcivos
        #codigo comentado en test.py
        #arch= input('> ')
        if not self.destino is None:
            self.sock.sendto(f'arch {name}'.encode(), self.destino)
            with open(name,"rb") as fileBin:
                #encoded_file = base64.urlsafe_b64encode(fileBin.read())
                #compres_file = zlib.compress(encoded_file)
                #se envia el binario del archivo codificado y Comprimido
                data = fileBin.read(CHUNK_SIZE)
                while data:
                    self.sock.sendto(codex(data), self.destino)
                    data = fileBin.read(CHUNK_SIZE)
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
        self.__sTCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__hosts = []
        self.__servers = []
        self.__archList=[]
        self.__smgList=[]
        self.__log=[]
        self.__name = 'partyGoer'
        self.__hostname = socket.gethostname()
        listenerMsg = threading.Thread(target=self.lmsg, daemon=True)
        listenerArch = threading.Thread(target=self.larch, daemon=True)
        #listenerFlags = threading.Thread(target=self.lflags, daemon=True)
        listenerMsg.start()
        listenerArch.start()
        #listenerFlags.start()
    
    @property
    def hostname(self):
        return self.__hostname
    @property
    def peerName(self):
        return self.__name
    @property
    def ipSource(self):
        return socket.gethostbyname(self.__hostname)
    @property
    def archList(self):
        return self.__archList
    @property
    def smgList(self):
        return self.__smgList
    @property
    def log(self):
        return self.__log
    
    def lmsg(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sUDP:
            sUDP.bind((PL_ADDRESS, DEFAULT_PORT_LMSG))# se define el puerto de envio 50001
    
            while True:
                flag, address = sUDP.recvfrom(128)
                #se resiben buffer de binarios de 1024 digitos de longitud
                data = decodex(sUDP.recv(CHUNK_SIZE))
                #mensajes
                registro_smg='{} : {} '.format(address,data)
                registro_log='{} : {} '.format(address,flag)
                print(registro_smg)
                print(registro_log)
                self.__smgList.append(registro_smg)
                self.__log.append(registro_log)

    def larch(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sUDP:
            sUDP.bind((PL_ADDRESS, DEFAULT_PORT_LARCH))# se define el puerto de envio 50011

            while True:
                fdata, address = sUDP.recvfrom(128)
                flag, name = fdata.split(' ')
                with open(name, 'wb') as f:
                    chunk=decodex(sUDP.recv(CHUNK_SIZE))
                    while chunk:
                        print(len(chunk))
                        f.write(chunk)
                        chunk=decodex(sUDP.recv(CHUNK_SIZE))

                registro_log = '{} : {} '.format(address,fdata)
                print(registro_log)
                self.__log.append(registro_log)

         
            
    def getHost(self,nDest):
        return self.__hosts[nDest]
    def setHost(self,dAddr,dPort,sendPort=DEFAULT_PORT_SEND):
        newConection = HostUDP(sendPort)
        newConection.setDestino(dAddr,dPort)
        self.__hosts.append(newConection)
    def __len__(self):
        return len(self.__hosts)
    
class PeerTCP_UDP(Peer):
    def __init__(self) -> None:
        # Choosing Nickname
        self.__nickname = input("Choose your nickname: ")
        # Connecting To Server
        self.__client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__client.connect(('127.0.0.1', 55555))
    def receive(self):
        while True:
            try:
                # Receive Message From Server
                # If 'NICK' Send Nickname
                message = self.__client.recv(1024).decode('ascii')
                if message == 'NICK':
                    self.__client.send(self.__nickname.encode('ascii'))
                else:
                    print(message)
            except:
                # Close Connection When Error
                print("An error occured!")
                self.__client.close()
                break  
    def write(self):
        while True:
            message = '{}: {}'.format(self.__nickname, input(''))
            self.__client.send(message.encode('ascii'))

class Router(Peer):
    def __init__(self) -> None:
        pass
    def __len__(self):
        return len(self.__servers)
class ServerCenter(Peer):
    def __init__(self) -> None:
        self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__server.bind((PL_ADDRESS, DEFAULT_PORT_R))
        self.__server.listen()
        self.__clients = []
        self.__nicknames = []
        self.__name="partyHost"
        self.routers=[]
        self.peers=[]
    def lflags(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sUDP:
            sUDP.bind((PL_ADDRESS, DEFAULT_PORT_R))# se define el puerto de envio 55555

            while True:
                data, address = sUDP.recvfrom(128)
                print('connection from: {}'.format(address))
                if data == NONE_BIN:
                    d_addr, d_port = address
                    self.setHost( d_addr, d_port)
                elif data == b'1':
                    pass

    def broadcast(self,message):
        for client in self.__clients:
            client.send(message)
    def handle(self,client):
        while True:
            try:
                # Broadcasting Messages
                message = client.recv(1024)
                self.broadcast(message)
            except:
                # Removing And Closing Clients
                index = self.__clients.index(client)
                self.__clients.remove(client)
                client.close()
                nickname = self.__nicknames[index]
                self.broadcast('{} left!'.format(nickname).encode('ascii'))
                self.__nicknames.remove(nickname)
                break
    def receive(self):
        while True:
            # Accept Connection
            client, address = self.__server.accept()
            print("Connected with {}".format(str(address)))

            # Request And Store Nickname
            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            self.__nicknames.append(nickname)
            self.__clients.append(client)

            # Print And Broadcast Nickname
            print("Nickname is {}".format(nickname))
            self.broadcast("{} joined!".format(nickname).encode('ascii'))
            client.send('Connected to server!'.encode('ascii'))

            # Start Handling Thread For Client
            thread = threading.Thread(target=self.handle, args=(client,))
            thread.start()

    
    def getPartyChat(self):
        pass
    def getPartyFlags(self):
        pass
    def getPartyArch(self):
        pass
    def __len__(self):
        return len(self.peers)
    
'''def listen(self):
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
                self.destino(self.destino[0],data.decode())'''