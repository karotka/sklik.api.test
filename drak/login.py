import xmlrpclib

p = xmlrpclib.ServerProxy('https://api.sklik.cz/drak/RPC2')
result = p.client.login("zdenek.philipp@firma.seznam.cz", 'KArotka66155.')

if result["status"] == 200:
    ses = result["session"]
else:
    print result
    raise


