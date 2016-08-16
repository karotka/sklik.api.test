#!/usr/bin/env python
from login import p, ses
from datetime import datetime

USERID = 55355
DATE_FROM = datetime.strptime("28.3.2016", "%d.%m.%Y")
DATE_TO = datetime.strptime("29.3.2016", "%d.%m.%Y")

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
		"includeContext" : False
	}
)
if res["status"] == 200:
    ses = res["session"]
else: 
    print res

for line in res["report"]:


    print line

