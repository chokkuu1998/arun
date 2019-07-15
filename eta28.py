aa,bb=input().split()
h=list(map(int,input().split()))
for p in range(int(bb)):
	u,v=input().split()
	sum=0
	for z in range(int(u)-1,int(v)):
		min=h[int(u)-1]
		if h[z]<min:
			min=h[z]	
	print(min)
	continue
