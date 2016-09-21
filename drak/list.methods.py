#!/usr/bin/env python
from login import p, ses

res = p.system.listMethods()
for line in res:
	print line

