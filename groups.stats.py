#!/usr/bin/env python
from login import p, ses
from datetime import datetime

USER = 313744
CAMPAIGN = 0 

DATE_FROM = datetime.strptime("16.03.2016", "%d.%m.%Y")
DATE_TO = datetime.strptime("22.03.2016", "%d.%m.%Y")

res = p.campaigns.list({
        'session' : ses,
        'userId' : USER},
      )

cIds = list()
for c in res["campaigns"]:
        cIds.append(c["id"])
res = p.groups.list({
        "session" : ses,
        "userId"  : USER},
        {"campaignIds" : cIds}

)

gIds = list()
for g in res["groups"]:
        gIds.append(g["id"])

if CAMPAIGN:
        cIds = list()
        cIds.append(CAMPAIGN)

res = p.groups.stats(
	{
		"session" : ses,
		"userId"  : USER,
	}, gIds,
	{
		"dateFrom": DATE_FROM,
		"dateTo":   DATE_TO,
		"granularity" : "daily"
        }
)

if res["status"] == 200:
    ses = res["session"]
else: 
    print res

for gr in res["report"]:
    print "Group \t", gr["groupId"]
    for st in gr["stats"]:
        print st["date"], "\tclicks: ", st["clicks"], "\timpressions: ", st["impressions"]

