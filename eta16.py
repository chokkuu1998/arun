aa,bb = map(str,input().split())
mm = 0
if len(aa)>len(bb):
	aa,bb=bb,aa
xx = 0
while xx<len(aa):
	  mm += (ord(bb[xx])-ord(aa[xx]))
	  xx += 1
for xx in range(xx,len(bb)):
	  mm += ord(bb[xx])-ord('aa')+1
print(mm)
