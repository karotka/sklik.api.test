#!/usr/bin/env python
# -*- coding: utf-8 -*-

from login import p, ses

res = p.keywords.suggest.stats({'session' : ses}, [
    "mp3",
    "iphone 6",
    "iphone 6s",
    "apple",
    "vodafone",
    "laptop",
    "iphone 5s",
    "samsung",
    "windows 10",
    "tablet",
    "iphone",
    "t-mobile",
    "t mobile",
    "notebook",
    "smartphone",
    "smart phone",
    "fitbit",
    "samsung galaxy s6",
    "iphone 5",
    "watch",
    "camera",
    "o2",
    "drive",
    "ipad",
    "java"

], {"granularity" : "monthly"})
ses = res["session"]
for c in res["stats"]:
    print "Query: %s \t %s \t %s" % (c["query"], c["avgSearchCount"], c["avgCpc"]) 
    for i in c["searchCountInTime"]:
        print i
