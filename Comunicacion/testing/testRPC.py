
from Connections import RPC
rpc = RPC()
rpc1 = RPC()
def test():
    print('test')
    return 0
def test1():
    print('test1')
    return 1
rpc.serviceJoined(rpc.ipSource)
rpc.Joined.register_function(test)
rpc.starListener()
rpc.Joined.register_function(test1)
print(rpc.Joined.server_address)

print("fin")

rpc.appOnion(f'http://{rpc.ipSource}:20064')
print(rpc.getOnion(0).test())
print(rpc.getOnion(0).test1())
#db = BD(database='db/app2.db')

while True:
    pass
