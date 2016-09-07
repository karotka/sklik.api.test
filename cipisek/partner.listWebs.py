#!/usr/bin/env python
from datetime import datetime
import xmlrpclib

sess="7|LNAUERC3AFNH6ULRHBNVAWKELFHFKQQAAQLBODINAIHRQFBBFYAQOFCTNRWUCVSPKJMBUQABAUBCOGQXB4FEOCQWAYIC2AATBELQOWY4LIXTIRYWIUFUGRIIIZ5ES5RYLFIV4Q22INLE4DYGCYBAODIYAECVM7BOBBFZU425MC2OCSO76ZEJFPU6EA5M5UQKVVAQ===="

p = xmlrpclib.ServerProxy('https://api.sklik.cz/cipisek/RPC2')

res = p.partner.listWebs(sess)

for line in res["webs"]:
    print line

