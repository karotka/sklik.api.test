#!/usr/bin/env python
from login import p, ses
from datetime import datetime

ses = '7|LNAUCQ26BJIXGV3RHBNVAWSDLRCV4TQGAQLBODINAIHRQFBBFYAQOFCVMZWE4XSNKFMBUZZUERKXIKAAB4PAOBIULYJBOD2GB5ERUBQ4BF5XQWK2BFCEMWIILN7FM735L4MAUEQFAQBAWAAKCZKBULB7G6MVMSKVNOCKONIV6PENSNU77Z6IY==='

DATE_FROM = datetime.strptime("03.04.2016", "%d.%m.%Y")
DATE_TO = datetime.strptime("13.04.2016", "%d.%m.%Y")

bannerIds = [110347315,
110347318,
110347319,
110347321,
110347285,
110347286,
110347287,
110347288,
110347289,
110347290]

res = p.banners.stats({
	"session" : ses,
	"userId"  : 116010},
	bannerIds, {
	"dateFrom" : DATE_FROM,
	"dateTo" : DATE_TO,
	"granularity" : "daily"}
)

print res
for r in res["report"]:
	print "KW:", r["id"]
	for k in r["stats"]:
		print "\t", k["date"], k["impressions"], k["clicks"]

print "Kampane", cIds
print "Sestavy", gIds
