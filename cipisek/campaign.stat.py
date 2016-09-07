#!/usr/bin/env python
from login import p, ses
from datetime import datetime

res = p.campaigns.stats({'session' : ses, 'userId' : 594}, (
        708622,390316,524066,496005,777763,783901,820448),
        {
            "dateFrom" : datetime.strptime("15.03.2015", "%d.%m.%Y"),
            "dateTo" : datetime.strptime("20.03.2015", "%d.%m.%Y"),
            "granularity" : "daily"}
)

if res["status"] == 200:
    for line in res["report"]:
        print line["campaignId"]
        for day in line["stats"]:
            print day

