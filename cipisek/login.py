import xmlrpclib

p = xmlrpclib.ServerProxy('https://api.sklik.cz/cipisek/RPC2')
result = p.client.login("username@domain", 'passsword')

if result["status"] == 200:
    ses = result["session"]
else:
    print result
    raise


