#!/usr/bin/env python
import xmlrpclib

p = xmlrpclib.ServerProxy('https://api.sklik.cz/cipisek/RPC2')

ses = "7|LNAUAQK7BVPH6VLSHBNVAW2BLVBFCQQEA4LBODINAIHRQFBBFYAQOFCQMJTE6V2LKRIBUXQKCMADIBQWDZEQCBIXCQKACXQCCYFBE5SBLQXSMFQHLMKASFYICR5BW5TKLJFFYXKZBNLQWUCSAYLQGHK2LUCVINAKQ4CGNRBIOGJDBS4PB3X5XOEB63A7PAI="

res = p.groups.list({
	'session' : ses,
	'userId' : 307845},
	{"campaignIds" : (909382,)})

if res["status"] != 200:
    print res

for c in res["groups"]:
    print "CampaignId: %d\tID: %d\tName: %s" % (c["campaign"]["id"], c["id"], c["name"]) 

print len(res["groups"])
