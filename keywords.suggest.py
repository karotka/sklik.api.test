#!/usr/bin/env python
from login import p, ses

res = p.keywords.suggest({'session' : ses}, 'mazda 6')
ses = res["session"]
for c in res["suggestions"]:
    print "Query: %s \t %s \t %s" % (c["query"], c["avgSearchCount"], c["cpc"]) 

