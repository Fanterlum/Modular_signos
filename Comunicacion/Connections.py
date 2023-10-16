import socket
import sys
import threading
import base64
import zlib
from hashlib import sha512
import xmlrpc.server #import SimpleXMLRPCServer
import xmlrpc.client #import ServerProxy
'''TCP es un protocolo orientado a la conexión mientras que UDP no utiliza 
conexión. TCP establece una conexión entre un remitente y un receptor antes 
de que se puedan enviar los datos. UDP en cambio, no establece ninguna 
conexión antes de enviar los datos.

SOCK_STREAM means that it is a TCP socket.
SOCK_DGRAM means that it is a UDP socket.

'''
PL_ADDRESS = '0.0.0.0'      # para fuera de la red local 
L_ADDRESS = '127.0.0.1'     # para fuera la red local 
P_PORT = 80                 # puerto para conexiones publicas 
DEFAULT_PORT_R = 55555      # puerto por defecto escuchar flags UDP
DEFAULT_PORT_LMSG = 50001 # puerto por defecto para escuchar msg UDP
DEFAULT_PORT_LARCH = 50011 # puerto por defecto para escuchar arch UDP
DEFAULT_PORT_SEND = 50002   # puerto por defecto para enviar por UDP
DEFAULT_PORT_DARCH = 50007   # puerto por defecto para TCP
#DEFAULT_PORT_DMSG = 50008   # puerto por defecto para duplex arch
DEFAULT_PORT_RPC=20064
NONE_BIN = b'0'             # cadena binaria 0
BITE_SIZE = 8
KBIT_SIZE=1024
CHUNK_SIZE = 5 * KBIT_SIZE
NBIT_SIZE = BITE_SIZE * 2
TIPE_SIZE = BITE_SIZE / 2
HASH_SIZE = BITE_SIZE ** 2
class packing:
    
    def __init__(self) -> None:

        self.__archList=[]
        self.__smgList=[]
        self.__log=[]

    @property
    def archList(self):
        return self.__archList
    @property
    def smgList(self):
        return self.__smgList
    @property
    def log(self):
        return self.__log
    def header(n,nlen,pakedhash,totalhash):
        nbin=format(n, "b").encode()
        relleno_nbin=(NONE_BIN*(NBIT_SIZE-len(nbin)))
        header_nbin=relleno_nbin+nbin

        nlenbin=format(nlen, "b").encode()
        relleno_nlenbin=(NONE_BIN*(NBIT_SIZE-len(nlenbin)))
        header_nlenbin=relleno_nlenbin+nlenbin

        return header_nbin+header_nlenbin+pakedhash+totalhash

    def codex(dat):
        encoded_dat = base64.urlsafe_b64encode(dat)
        compres_dat = zlib.compress(encoded_dat)
        return compres_dat
    
    def decodex(dat):
        decompres_dat = zlib.decompress(dat)
        decoded_dat = base64.urlsafe_b64decode(decompres_dat)
        return decoded_dat
class Peer:
    def __init__(self,nickname='Anonimo') -> None:
        self.__hosts = []
        self.__partys = []
        self.__destinos = []
        

        self.__nickname=nickname

        self.__name = 'partyGoer'

        #self.__hostname = socket.gethostname()

    @property
    def destinos(self):
        return self.__destinos
    @property
    def hostname(self):
        return socket.gethostname()
    @property
    def peerName(self):
        return self.__name
    @property
    def ipSource(self):
        return socket.gethostbyname(self.hostname)
    
class UDP(Peer,packing):
    def __init__(self) -> None:
        listenerMsg = threading.Thread(target=self.lmsg, daemon=True)
        '''listenerArch = threading.Thread(target=self.larch, daemon=True)
        listenerFlags = threading.Thread(target=self.lflags, daemon=True)'''
        listenerMsg.start()
        '''listenerArch.start()
        listenerFlags.start()'''
    
    def lmsg(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sUDP:
            sUDP.bind((PL_ADDRESS, DEFAULT_PORT_LMSG))# se define el puerto de escucha 50001
    
            while True:
                flag, address = sUDP.recvfrom(128)
                #se resiben buffer de binarios de 1024 digitos de longitud
                data = self.decodex(sUDP.recv(CHUNK_SIZE))
                #mensajes
                registro_smg='{} : {} '.format(address,data)
                registro_log='{} : {} '.format(address,flag)
                print(registro_smg)
                print(registro_log)
                self.__smgList.append(registro_smg)
                self.__log.append(registro_log)

    def sendMSN(self,nDest,msg):
        #...mensajes
        #msg = input('> ')
        #se envia la cadena de texto codificada y comprimida en binario
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sUDP:
            sUDP.bind((PL_ADDRESS, DEFAULT_PORT_SEND))# se define el puerto de envio 50002

            if self.destinos :
                sUDP.sendto(b'msg', self.destinos[nDest])
                sUDP.sendto(self.codex(msg), self.destinos[nDest])

    '''def larch(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sUDP:
            sUDP.bind((PL_ADDRESS, DEFAULT_PORT_LARCH))# se define el puerto de escucha 50011

            while True:
                fdata, address = sUDP.recvfrom(128)
                flag, name = fdata.split(' ')
                with open(name, 'wb') as f:
                    chunk=self.decodex(sUDP.recv(CHUNK_SIZE))
                    while chunk:
                        print(len(chunk))
                        f.write(chunk)
                        chunk=self.decodex(sUDP.recv(CHUNK_SIZE))

                registro_log = '{} : {} '.format(address,fdata)
                print(registro_log)
                self.__log.append(registro_log)

    def sendArch(self,nDest,name="JS_2_3.json"):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sUDP:
            sUDP.bind((PL_ADDRESS, DEFAULT_PORT_SEND))# se define el puerto de envio 50002
        
            if not self.__destinos[nDest] is None:
                sUDP.sendto(f'arch {name}'.encode(), self.__destinos[nDest])
                with open(name,"rb") as fileBin:
                    #se envia el binario del archivo codificado y Comprimido
                    data = fileBin.read(CHUNK_SIZE)
                    while data:
                        sUDP.sendto(self.codex(data), self.__destinos[nDest])
                        data = fileBin.read(CHUNK_SIZE) 
    def lflags(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sUDP:
            sUDP.bind((PL_ADDRESS, DEFAULT_PORT_R))# se define el puerto de escucha 55555

            while True:
                data, address = sUDP.recvfrom(128)
                print('connection from: {}'.format(address))
                if data == NONE_BIN:
                    self.__log.append(f'joined ({address})')
                    try:
                        print(self.__destinos.index(address))
                    except:
                        self.addDestino(address)

                elif data == b'1':
                    pass'''

    def addDestino(self,address):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sUDP:
            sUDP.bind((PL_ADDRESS, DEFAULT_PORT_SEND))# se define el puerto de envio 50002
            self.__log.append(f'new Destino ({address})')
            self.__destinos.append(address)
            sUDP.sendto(b'0', address)
            
    
class RouterUDP(UDP):
    def lmsg(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sUDP:
            sUDP.bind((PL_ADDRESS, DEFAULT_PORT_LMSG))# se define el puerto de escucha 50001
    
            while True:
                name_addres, address = sUDP.recvfrom(128)
                self.addDestino(address=address)
                index= self.__destinos.index(address)
                self.sendMSN(self.__destinos[index],self.__hosts[name_addres])
                
    def lReg(self):
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sUDP:
            sUDP.bind((PL_ADDRESS, DEFAULT_PORT_R))# se define el puerto de escucha 50001
            while True:
                name_addres, address = sUDP.recvfrom(128)
                self.__hosts[name_addres]=address
    
class PartyUDP(UDP):
    def __init__(self) -> None:
        pass
    def broadcast(self,message):
        pass
    def handle(self,client):
        pass
    def __len__(self):
        return len(self.__servers) 

class TCP(packing):
    def __init__(self) -> None:
        self.__peerTCP=None
        self.__addres=None
        self.__listener = None
    @property
    def Peer(self):
        return self.__peerTCP
    def __listenerTCP(self):
        while self.__peerTCP:
            try:
                # Receive Message From Server
                # If 'NICK' Send Nickname

                message = self.decodex(self.__peerTCP.recv(CHUNK_SIZE))

                self.__smgList.append(f'{self.__addres} : {message}')
                self.__log.append(f'{self.__addres} : msg')

                print(message)
            except:
                # Close Connection When Error
                print("An error occured!")
                self.__peerTCP.close()
                break

    def starListener(self):
        if not self.__listener is None:
            self.__listener.start()

    def service(self,peer,address):
        # Accept Connection
        #joined, address = self.__sTCP.accept()
        self.__peerTCP=peer
        self.__addres=address
        self.__log.append(f'({address}) Connect')
        self.__listener = threading.Thread(target=self.__listenerTCP,daemon=True)
    
    def send(self,message):
        if self.__peerTCP:
            self.__peerTCP.send(self.codex(message))
    
class MasterTCP(TCP,Peer):
    def __init__(self) -> None:
        self.__joineds=[]
        self.__onions=[]
    @property
    def sizeJoineds(self):
        return len(self.__joineds)
    @property
    def sizeOnions(self):
        return len(self.__onions)
        
    '''def __listenerServe(self,joined):
        while True:
            try:
                # Messages
                message = joined.recv(CHUNK_SIZE)
                index = self.__joineds.index(joined)
                self.__smgList.append(f'{self.__destinos[index]} : {message}')
                self.__log.append(f'{self.__destinos[index]} : msg')
            except:
               index = self.__joineds.index(joined)
               self.removeJoined(index)
               break  ''' 
    def __listenerJoineds(self):
        while True:
            # Accept Connection
            joined, address = self.__peerTCP.accept()
            
            self.__joineds.append(TCP())
            self.__destinos.append(address)
            self.__log.append(f'({address}) Connect')

            self.__joineds[len(self.__joineds)-1].service(joined)

    def serviceJoineds(self):
        self.__peerTCP=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__peerTCP.bind((PL_ADDRESS, DEFAULT_PORT_DARCH))
        self.__peerTCP.listen()
        self.__listener = threading.Thread(target=self.__listenerJoineds,daemon=True)

    
    def ListenJoined(self,n): 
        self.__joineds[n].starListener()    
    
    def ListenOnion(self,n):
        self.__onions[n].starListener()

    def appOnion(self,addres):
        onion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        onion.connect((addres, DEFAULT_PORT_DARCH))

        self.__hosts.append(addres)
        self.__log.append(f'({addres}) Connect')
        self.__onions.append(TCP())

        self.__onions[len(self.__onions)-1].service(onion)
    
    def removeJoined(self,index):
        # Removing And Closing Clients
        joined=self.__joineds.pop(index)
        joined.close()
        address = self.__destinos[index]
        self.__log.append('{} left!'.format(address))
        self.__destinos.remove(address)

    def removeOnion(self,index):
        # Removing And Closing servers
        onion=self.__onions.pop(index)
        onion.close()
        address = self.__hosts[index]
        self.__log.append('{} left!'.format(address))
        self.__hosts.remove(address)

class RouterTCP(MasterTCP):
    def __init__(self) -> None:
        pass
    def __len__(self):
        return len(self.__servers)
class PartyTCP(MasterTCP):
    def __init__(self) -> None:
        
        self.__name="partyHost"

    def broadcastSmg(self,message):
        for client in self.__joineds:
            client.send(message)

    def ListenerAllOnions(self):
        if not self.__listener is None:
            for onion in self.__onions :
                onion.starListener()
    
    def ListenerAllJoineds(self):
        if not self.__listener is None:
            for joined in self.__joineds :
                joined.starListener()
    
    def getPartyChat(self):
        pass
    def getPartyFlags(self):
        pass
    def getPartyArch(self):
        pass
    def __len__(self):
        return len(self.peers)
'''class Onion_RPC():
    def __init__(self) -> None:
        pass'''

'''class Joineder_RPC:
    #methods = ['get','set','delete','exists', 'keys', 'calc']
    #methods = ['calc'] 
    def __init__(self,direccion, port) -> None:
        self.server = SimpleXMLRPCServer((direccion, port), allow_none=True)
        
        for method in self.methods:
            self.server.register_function(getattr(self, method))
    
    def run(self):
        self.server.serve_forever()
        print("Server iniciado")'''

class RPC(Peer):
    
    def __init__(self) -> None:
        self.__listener = None
        self.__joined = None
        self.__onions=[]

    @property
    def Joined(self):
        return self.__joined

    def serviceJoined(self,direccion=L_ADDRESS, port=DEFAULT_PORT_RPC):# entrada de instruciones
        self.__listener = threading.Thread(target=self.__listenerServe, daemon=True)
        self.__joined = xmlrpc.server.SimpleXMLRPCServer((direccion, port))
        #self.__joined.register_instance(MyClass)
        #joineder.shutdown().serve_forever()
        #self.__joineds.append(joineder)
    def __listenerServe(self):
        if not self.__joined is None:
            self.__joined.serve_forever()
    def starListener(self):
        if not self.__listener is None:
            self.__listener.start()

    def appOnion(self,proxyLink=f'http://{L_ADDRESS}:{DEFAULT_PORT_RPC}'):# salida de instruciones
        self.__onions.append(xmlrpc.client.ServerProxy(proxyLink, allow_none=True))

    def getOnion(self,n):
        return self.__onions[n]

    def __len__(self):
        return len(self.__destinos)
class PartyRPC(RPC):
    def __init__(self) -> None:
        pass
    def broadcast(self,message):
        pass
    def __len__(self):
        return len(self.__destinos)
class RouterRPC(RPC):
    def __init__(self) -> None:
        pass
    def __len__(self):
        return len(self.__destinos)
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

'''def setListenPort(self,lPort):
        self.listenPort=lPort
        self.sock.sendto(b'newLP',self.destino)
        self.sock.sendto(f'{lPort}'.encode())'''

'''
self.__clients = []
self.__nicknames = []
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
            thread.start()'''