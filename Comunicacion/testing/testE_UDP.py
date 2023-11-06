from Connections import UDP 
udp = UDP('endpoint')
print(udp.ipSource)
print(udp.peerName)
while True:
    input(":")
    print(udp.smgList)
    pass