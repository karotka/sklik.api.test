#!/usr/bin/env python
from login import p#, ses
ses = "7|LNAUAQK7BVPH6VLSHBNVAW2BLVBFCQQEA4LBODINAIHRQFBBFYAQOFCQMJTE6V2LKRIBUXQKCMADIBQWDZEQCBIXCQKACXQCCYFBE5SBLQXSMFQHLMKASFYICR5BW5TKLJFFYXKZBNLQWUCSAYLQGHK2LUCVINAKQ4CGNRBIOGJDBS4PB3X5XOEB63A7PAI="

res = p.groups.list({
	'session' : ses,
	'userId' : 307845},
	{"campaignIds" : (909382,)})
for c in res["groups"]:
    print "CampaignId: %d\tID: %d\tName: %s" % (c["campaign"]["id"], c["id"], c["name"]) 

print len(res["groups"])
