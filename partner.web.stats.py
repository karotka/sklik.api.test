#!/usr/bin/env python
from datetime import datetime
import xmlrpclib

sess="7|LNAUERC3AFNH6ULRHBNVAWKELFHFKQQAAQLBODINAIHRQFBBFYAQOFCTNRWUCVSPKJMBUQABAUBCOGQXB4FEOCQWAYIC2AATBELQOWY4LIXTIRYWIUFUGRIIIZ5ES5RYLFIV4Q22INLE4DYGCYBAODIYAECVM7BOBBFZU425MC2OCSO76ZEJFPU6EA5M5UQKVVAQ===="

p = xmlrpclib.ServerProxy('https://api.sklik.cz/cipisek/RPC2')

res = p.partner.web.stats(
	sess, 24056,
        datetime.strptime("03.03.2016", "%d.%m.%Y"),
        datetime.strptime("03.03.2016", "%d.%m.%Y")
)

print res
if res["status"] == 200:
    for line in res["stats"]:
        print line

