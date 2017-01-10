#!/usr/bin/env python
from login import p, ses

res = p.campaigns.list({
	'session' : ses,
	},
	)
print res
for c in res["campaigns"]:
    print "ID: %d Name: %s" % (c["id"], c["name"]) 

