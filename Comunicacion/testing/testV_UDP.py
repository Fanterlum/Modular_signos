from Connections import UDP,DEFAULT_PORT_F,DEFAULT_PORT_LMSG

udp=UDP('vision')

udp.sendFlag(("192.168.84.128",DEFAULT_PORT_F),'addme')
udp.sendMSN(("192.168.84.128",DEFAULT_PORT_LMSG),'nose')
while True:
    input(':')
    udp.sendFlag(("192.168.84.128",DEFAULT_PORT_F),'dropme','prediccion')
    print(udp.Peers)
    udp.sendFlag(("192.168.84.128",DEFAULT_PORT_F),'func','testf')