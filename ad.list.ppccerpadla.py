#!/usr/bin/env python
from login import p, ses
from datetime import datetime


USER = 5103

DATE_FROM = datetime.strptime("01.07.2016", "%d.%m.%Y")
DATE_TO = datetime.strptime("31.07.2016", "%d.%m.%Y")

res = p.campaigns.list({
	'session' : ses,
	'userId' : USER},
)
ses = res["session"]

cIds = list()
for c in res["campaigns"]:
	cIds.append(c["id"])

res = p.campaigns.stats({
	"session" : ses,
	"userId"  : USER
	}, cIds,
	{
	"dateFrom" : DATE_FROM,
	"dateTo"   : DATE_TO,
	"granularity" : "daily",
	"includeFulltext" : True,
	"includeContext" : True
	}
)

suma = 0
for r in res["report"]:
	for c in r["stats"]:
		suma += c["price"]

print "Kampane celkem: %0.2f" % (suma / 100.0, )

aIds = list()
res = p.ads.list({
        "session" : ses,
        "userId"  : USER
        }, {"campaignIds" : cIds})

for ad in res["ads"]:
	aIds.append(ad["id"])

suma = impressions = clicks = 0
for i in range(0, len(aIds) / 100 + 1):

	res = p.ads.stats({
        "session" : ses,
        "userId"  : USER
        }, aIds[i * 100:i * 100 + 100],
        {
        "dateFrom" : DATE_FROM,
        "dateTo"   : DATE_TO,
        "granularity" : "daily",
        "includeFulltext" : True,
        "includeContext" : True
        }
	)
	#print aIds[i * 100:i * 100 + 100]


	for ad in res["report"]:
		for s in ad["stats"]:
			suma += s["price"]
			impressions += s["impressions"]
			clicks += s["clicks"]

	#print "I: %d, C: %d" % (impressions, clicks)

print "Ads.stats result: %d ads, suma %0.2f, clicks: %d, impressions: %d" % (len(aIds), suma / 100.0, clicks, impressions)


suma = impressions = clicks = 0
for i in range(0, len(aIds) / 100 + 1):

        res = p.banners.stats({
        "session" : ses,
        "userId"  : USER
        }, aIds[i * 100:i * 100 + 100],
        {
        "dateFrom" : DATE_FROM,
        "dateTo"   : DATE_TO,
        "granularity" : "daily",
        "includeFulltext" : True,
        "includeContext" : True
        }
        )
        #print aIds[i * 100:i * 100 + 100]
	#print res
        for ad in res:
                for s in ad["stats"]:
                        suma += s["price"]
                        impressions += s["impressions"]
                        clicks += s["clicks"]

        #print "I: %d, C: %d" % (impressions, clicks)

print "Banner stats result: %d ads, suma %0.2f, clicks: %d, impressions: %d" % (len(aIds), suma / 100.0, clicks, impressions)
