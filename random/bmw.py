#!/usr/bin/env python
import os
start = 0x00
end = 0xFF
goods = []
for a in xrange(start,end):
	p1 = str(format(a,'X').zfill(2))
	for b in xrange(start,end):
		p2 = str(format(b,'X').zfill(2))
		resp = os.popen('cmdthing' +p1 + p2).read()
		if resp.find('bad') == -1
			print 'Valid code maybe>
			good.append[resp]
			print resp
print 'Good cmds below'
print goods
