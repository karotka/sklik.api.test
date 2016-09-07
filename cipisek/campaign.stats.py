#!/usr/bin/env python
from login import p, ses
from datetime import datetime

USERID = 235632

res = p.campaigns.list({
	'session' : ses,
	'userId' : USERID})

ses = res["session"]

ids = []
for c in res["campaigns"]:
    ids.append(c["id"])


res = p.campaigns.stats({
	'session' : ses,
	'userId' : USERID}, (ids), {
            "dateFrom" : datetime.strptime("04.02.2016", "%d.%m.%Y"),
            "dateTo" : datetime.strptime("11.02.2016", "%d.%m.%Y"),
            "granularity" : "daily",
            "splitByConversions" : True
        }
)
print res
if res["status"] == 200:
    for line in res["report"]:
        print line["campaignId"]
        for day in line["stats"]:
            print day

