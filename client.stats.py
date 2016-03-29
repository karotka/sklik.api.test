#!/usr/bin/env python
from login import p, ses
from datetime import datetime

USERID = 284532
DATE_FROM = datetime.strptime("11.1.2015", "%d.%m.%Y")
DATE_TO = datetime.strptime("11.1.2015", "%d.%m.%Y")

res = p.client.stats(
	{
		"session" : ses, 
                "userId" : USERID
	},
	{
		"dateFrom" : DATE_FROM,
		"dateTo"   : DATE_TO,
                "granularity" : "daily", 
		"includeFulltext" : True,
		"includeContext" : True
	}
)
if res["status"] == 200:
    ses = res["session"]
else: 
    print res

for line in res["report"]:


    print line

