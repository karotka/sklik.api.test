#!/usr/bin/env python
from login import p, ses
from datetime import datetime
import time

USER = {
	'session' : ses,
        'userId' : 156107
}

FILTER = {
#	"campaign" : { "ids" : [790]},
#        "statisticsConditions" : [{"columnName" : "clicks", "operator" : "GT", "intValue" : 0}],
        "dateFrom" : datetime.strptime("1.1.2017", "%d.%m.%Y"),
        "dateTo" : datetime.strptime("2.1.2017", "%d.%m.%Y"),
}

res = p.keywords.createReport(USER, FILTER)
print "Create report: with filter: %s " % FILTER
print res
print "Returns %s lines" % res["totalCount"]

ran = range(0, res["totalCount"] / 10000 + 1)
clicks = impressions = price = 0
for i in ran:
	while 1:
		print "\nData %s, %d, %d" % (res["reportId"], i * 10000, 10000)
		r = p.keywords.stats(USER, res["reportId"], {
			'offset' : i * 10000, 'limit' : 10000,
			'allowEmptyStatistics' : False,
			'displayColumns' : ['clicks', 'conversions', 'impressions',
						'conversionValue', 'clickMoney', 'id',
						'group.id', 'campaign.id' ] } )
                if r["status"] != 200:
                    print r
		if r["status"] == 200:
			for report in r["report"]:
				for line in report["stats"]:
					clicks += line["clicks"]
					impressions += line["impressions"]
					price += line["clickMoney"]
					print "ID: %d clicks: %d, impressions: %d"  % (report["id"], line["clicks"], line["impressions"])
		break
	else:
		print r
		time.sleep(1)

print "SUM clicks: %s, impression: %s, price:%.02f" % (clicks, impressions, price/100)
