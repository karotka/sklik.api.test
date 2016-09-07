#!/usr/bin/env python
from login import p, ses
from datetime import datetime
import time

USER = {
	'session' : ses,
        'userId' : 72972}

FILTER = {
        "statisticsConditions" : [{"columnName" : "clicks", "operator" : "GT", "intValue" : 0}],
        "dateFrom" : datetime.strptime("03.09.2016", "%d.%m.%Y"),
        "dateTo" : datetime.strptime("04.09.2016", "%d.%m.%Y"),
}

res = p.keywords.createReport(USER, FILTER)
print "Create report: with filter: %s " % FILTER

while 1:
	r = p.keywords.stats(USER, res["reportId"], 0, 1000)
	if r["status"] == 200:
		for report in r["report"]:
			print report
		break
	else:
		print r["status"]
		time.sleep(1)

