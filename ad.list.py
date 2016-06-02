#!/usr/bin/env python
from login import p, ses

res = p.ads.get({
	'session' : ses,
	'userId' : 267766}, (35140763, )
)
ses = res["session"]

for line in res["ads"]:
	print line

res = p.ads.update({
        'session' : ses,
        'userId' : 267766}, ({"id" : 35140763, "status" : "active"}, )
)
