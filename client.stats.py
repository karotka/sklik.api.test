#!/usr/bin/env python
from login import p, ses
from datetime import datetime



res = p.client.stats(
	{
		"session" : ses},
	{
		"dateFrom" : datetime.strptime("13.3.2015", "%d.%m.%Y"),
		"dateTo"   : datetime.strptime("13.3.2015", "%d.%m.%Y"),
                "granularity" : "daily" }
)
if res["status"] == 200:
    ses = res["session"]
else: 
    print res

for line in res["report"]:


    print line

