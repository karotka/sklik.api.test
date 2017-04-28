#!/usr/bin/env python
from login import p, ses
from datetime import datetime
import time

USER = {
        'session' : ses,
        'userId' : 275620
}

FILTER = {
#       "campaign" : { "ids" : [790]},
#        "statisticsConditions" : [{"columnName" : "clicks", "operator" : "GT", "intValue" : 0}],
        "dateFrom" : datetime.strptime("1.1.2017", "%d.%m.%Y"),
        "dateTo" : datetime.strptime("27.4.2017", "%d.%m.%Y"),
}

res = p.campaigns.createReport(USER, FILTER)
#print "Create report: with filter: %s " % FILTER
print res
print "Returns %s lines" % res["totalCount"]

ran = range(0, res["totalCount"] / 10000 + 1)
clicks = impressions = price = 0
for i in ran:
        while 1:
                print "\nData %s, %d, %d" % (res["reportId"], i * 10000, 10000)
                r = p.campaigns.readReport(USER, res["reportId"], {
                        'offset' : i * 10000, 'limit' : 10000,
                        'allowEmptyStatistics' : True,
                        'displayColumns' : ['name'] })
                if r["status"] != 200:
                    print r
                if r["status"] == 200:
                        for report in r["report"]:
                                print report
                break
        else:
                print r
                time.sleep(1)
