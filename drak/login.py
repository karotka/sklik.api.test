import xmlrpclib

p = xmlrpclib.ServerProxy('https://api.sklik.cz/drak/RPC2')
result = p.client.login("username@domain", 'password')

if result["status"] == 200:
    ses = result["session"]
else:
    print result
    raise


