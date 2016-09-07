#!/usr/bin/env python
from login import p, ses

res = p.campaigns.list({
	'session' : ses,
	'userId' : 235632},
	)
ses = res["session"]
for c in res["campaigns"]:


    print "ID: %d Name: %s" % (c["id"], c["name"]) 

