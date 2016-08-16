#!/usr/bin/env python
from login import p, ses

res = p.keywords.suggest({'session' : ses},
'pneumatiky'

)
ses = res["session"]
for c in res["suggestions"]:
    print "Query: %s \t Count: %s \t CPC: %s" % (c["query"], c["avgSearchCount"], c["cpc"]) 

