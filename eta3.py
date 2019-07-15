mm,nn=input().strip().split(" ")
nn=int(nn)
ss=0
while ss<len(mm)-1 and n:
	if(mm[ss]>m[ss+1]):
		nn-=1
		mm=mm[:ss]+mm[ss+1:]
		if(ss!=0):
			ss-=1
	else:
		ss+=1
q=mm[:len(mm)-nn]
print(q)
