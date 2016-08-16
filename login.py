import xmlrpclib

p = xmlrpclib.ServerProxy('https://api.sklik.cz/cipisek/RPC2')
#result = p.client.login("karotka@seznam.cz", '')
result = p.client.login("zdenek.philipp@firma.seznam.cz", 'KArotka66155')

if result["status"] == 200:
    ses = result["session"]
else:
    raise


