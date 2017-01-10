#!/usr/bin/env python
# -*- coding: utf-8 -*-

from login import p, ses

res = p.keywords.suggest.stats({'session' : ses}, [
"bmw",
"květináč"

], {"granularity" : "monthly"})
print res
for c in res["stats"]:
    print "Query: %s \t %s \t %s" % (c["query"], c["avgSearchCount"], c["avgCpc"]) 
    for i in c["searchCountInTime"]:
        print i
