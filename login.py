import xmlrpclib

p = xmlrpclib.ServerProxy('https://api.sklik.cz/cipisek/RPC2')
result = p.client.login('', '')

if result["status"] == 200:
    ses = result["session"]
else:
    raise


