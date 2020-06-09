import xmlrpclib

p = xmlrpclib.ServerProxy('https://api.sklik.cz/cipisek/RPC2')
result = p.client.login("karotka@seznam.cz", 'Heslo123')
print result
if result["status"] == 200:
    ses = result["session"]
else:
    print result
    raise


