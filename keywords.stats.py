#!/usr/bin/env python
from login import p, ses
from datetime import datetime


USER = 313744
CAMPAIGN = 848016

DATE_FROM = datetime.strptime("16.03.2016", "%d.%m.%Y")
DATE_TO = datetime.strptime("22.03.2016", "%d.%m.%Y")

res = p.campaigns.list({
	'session' : ses,
	'userId' : USER},
	)
ses = res["session"]

cIds = list()
for c in res["campaigns"]:
	cIds.append(c["id"])

if CAMPAIGN:
	cIds = list()
	cIds.append(CAMPAIGN)

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
	keywordIds, {
	"dateFrom" : DATE_FROM,
	"dateTo" : DATE_TO,
	"granularity" : "daily"}
)

for r in  res["report"]:
	print "KW:", r["keywordId"] 
	for k in r["stats"]:
		print "\t", k["date"], k["impressions"], k["clicks"]

print "Kampane", cIds
print "Sestavy", gIds

