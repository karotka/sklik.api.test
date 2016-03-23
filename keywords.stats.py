#!/usr/bin/env python
from login import p, ses
from datetime import datetime


USER = 235632

res = p.campaigns.list({
	'session' : ses,
	'userId' : USER},
	)
ses = res["session"]

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

keywordIds = list()
res = p.keywords.list({
        "session" : ses,
        "userId"  : USER}, 
        {"groupIds" : gIds}

)
for k in res["keywords"]:
	keywordIds.append(k["id"])





res = p.keywords.stats({
	"session" : ses,
	"userId"  : USER},
	keywordIds[:100], {
	"dateFrom" : datetime.strptime("20.03.2016", "%d.%m.%Y"),
	"dateTo" : datetime.strptime("27.03.2016", "%d.%m.%Y"),
	"granularity" : "daily"}
)
print res
for r in  res["report"]:
	print r 
