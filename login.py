import xmlrpclib

p = xmlrpclib.ServerProxy('https://api.sklik.cz/cipisek/RPC2')
result = p.client.login("put_your_username_with_domain_here", 'put_you_passsword_here')

if result["status"] == 200:
    ses = result["session"]
else:
    print result
    raise


