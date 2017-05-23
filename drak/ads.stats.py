#!/usr/bin/env python
from login import p, ses
from datetime import datetime
import time

USER = {
	'session' : ses,
        'userId' : 252248
}

FILTER = {
	"ids" : [224597005],
        "statisticsConditions" : [{"columnName" : "clicks", "operator" : "GT", "intValue" : 0}],
        "dateFrom" : datetime.strptime("14.05.2017", "%d.%m.%Y"),
        "dateTo" : datetime.strptime("15.05.2017", "%d.%m.%Y"),
}

res = p.ads.createReport(USER, FILTER)
print "Create report: with filter: %s " % FILTER
print "Returns %s lines" % res["totalCount"]

ran = range(0, res["totalCount"] / 10000 + 1)
clicks = impressions = price = 0
for i in ran:
	while 1:
		print "\nData %s, %d, %d" % (res["reportId"], i * 10000, 10000)
		r = p.ads.stats(USER, res["reportId"], {
                        "offset" : i * 10,
                        "limit" : 10,
                        "displayColumns" : ['campaign.id', 'clicks', 'impressions', 'clickMoney']
		})
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
