#!/usr/bin/env python
from login import p, ses
from datetime import datetime
import time

USER = {
	'session' : ses,
        'userId' : 594
}

FILTER = {
        "statisticsConditions" : [{"columnName" : "impressions", "operator" : "GT", "intValue" : 0}],
        "dateFrom" : datetime.strptime("01.01.2014", "%d.%m.%Y"),
        "dateTo" : datetime.strptime("28.09.2016", "%d.%m.%Y"),
}

res = p.groups.createReport(USER, FILTER, {"statGranularity" : "daily"})
print "Create report: with filter: %s " % FILTER
print "Returns %s lines" % res["totalCount"]

ran = range(0, res["totalCount"] / 10 + 1)
clicks = impressions = price = 0
for i in ran:
	while 1:
		print "\nData %s, %d, %d" % (res["reportId"], i * 10, 10)
		r = p.groups.stats(USER, res["reportId"], i * 10, 10)
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
