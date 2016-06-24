#!/usr/bin/env python
# -*- coding: utf-8 -*-

from login import p, ses

res = p.keywords.suggest.stats({'session' : ses}, [

"pneumatiky", "pneumatiky praha", "školní batohy", "detske batohy", "ubytování liberec"

], {"granularity" : "monthly"})
ses = res["session"]
for c in res["stats"]:
    print "Query: %s \t %s \t %s" % (c["query"], c["avgSearchCount"], c["avgCpc"]) 
    for i in c["searchCountInTime"]:
        print i
