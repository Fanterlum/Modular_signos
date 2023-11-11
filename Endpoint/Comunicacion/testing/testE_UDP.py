from Connections import UDP 
udp = UDP('endpoint')
print(udp.ipSource)
print(udp.peerName)
def testf():
    print('test')
    return 0
udp.register_function(testf)
while True:
    input(":")
    print(udp.smgList)
    print(udp.Peers)
    print(udp.Func)
    pass