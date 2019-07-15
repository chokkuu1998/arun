ratt,dogg=input().strip().split(" ")
dogg=int(dogg)
sow=0
while sow<len(ratt)-1 and dogg:
	if(ratt[sow]>rat[sow+1]):
		dogg-=1
		ratt=ratt[:sow]+ratt[sow+1:]
		if(sow!=0):
			sow-=1
	else:
		sow+=1
qea=ratt[:len(ratt)-dogg]
print(qea)
