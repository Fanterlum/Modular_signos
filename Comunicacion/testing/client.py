import socket
import sys
import threading
import base64
import zlib

rendezvous = ('192.168.122.42', 55555)

# connect to rendezvous
print('connecting to rendezvous server')
#--------------------------------Codigo para encontrar enlazar dos puntos
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 50001))
sock.sendto(b'0', rendezvous)

while True:
    data = sock.recv(1024).decode()

    if data.strip() == 'ready':
        print('checked in with server, waiting')
        break

data = sock.recv(1024).decode()
ip, sport, dport = data.split(' ')
sport = int(sport)
dport = int(dport)

print('\ngot peer')
print('  ip:          {}'.format(ip))
print('  source port: {}'.format(sport))
print('  dest port:   {}\n'.format(dport))

# punch hole
# equiv: echo 'punch hole' | nc -u -p 50001 x.x.x.x 50002
print('punching hole')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', sport))
sock.sendto(b'0', (ip, dport))
#--------------------------------Codigo para encontrar enlazar dos puntos
print('ready to exchange messages\n')

# listen for
# equiv: nc -u -l 50001
def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 50001))# se define el puerto de envio 50001
    
    while True:
        #se resiben buffer de binarios de 1024 digitos de longitud
        data = sock.recv(1024)
        #archivos 
            #codigo comentado en test.py
        decompres_file = zlib.decompress(data)
        decoded_file = base64.urlsafe_b64decode(decompres_file)
        print(len(decoded_file))
        print('\rpeer: {}\n> '.format(decoded_file), end='')
        #mensajes
        print('\rpeer: {}\n> '.format(data.decode()), end='')
#se crea un proceso para estar a la escucha del puerto 50001
listener = threading.Thread(target=listen, daemon=True)
listener.start()


# equiv: echo 'xxx' | nc -u -p 50002 x.x.x.x 50001

# envio de ...
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', dport)) # se define el puerto de envio

#...arcivos
    #codigo comentado en test.py
arch= input('> ')
with open("JS_2_3.json","rb") as fileBin:
    encoded_file = base64.urlsafe_b64encode(fileBin.read())
    compres_file = zlib.compress(encoded_file)
    #se envia el binario del archivo codificado y Comprimido
    sock.sendto(compres_file, (ip, sport))
    fileBin.close()

#...mensajes
while True:
    msg = input('> ')
    #se envia la cadena de texto codificada en binario
    sock.sendto(msg.encode(), (ip, sport))
