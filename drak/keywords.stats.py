#!/usr/bin/env python
from login import p, ses
from datetime import datetime
import time

USER = {
	'session' : ses,
        'userId' : 72972}

FILTER = {
        "statisticsConditions" : [{"columnName" : "impressions", "operator" : "GT", "intValue" : 0}],
        "dateFrom" : datetime.strptime("03.09.2016", "%d.%m.%Y"),
        "dateTo" : datetime.strptime("03.09.2016", "%d.%m.%Y"),
}

res = p.keywords.createReport(USER, FILTER)
print "Create report: with filter: %s " % FILTER


clicks = impressions = 0
while 1:
	r = p.keywords.stats(USER, res["reportId"], 0, 10000)
	if r["status"] == 200:
		for report in r["report"]:
			for line in report["stats"]:
				clicks += line["clicks"]
				impressions += line["impressions"]
				print "ID: %d clicks: %d, impressions: %d"  % (report["id"], line["clicks"], line["impressions"])
		break
	else:
		print r
		time.sleep(1)

print "SUM clicks: %s, impression: %s" % (clicks, impressions)


