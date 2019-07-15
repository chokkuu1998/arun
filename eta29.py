nn1,nn2=list(map(int,input().split()))
lis1=list(map(int,input().split()))
lis2=[]
while(nn2):
	kk = list(map(int,input().split()))
	lis2.append(kk)
	nn2-=1
for i in lis2:
	val=0
	for j in range(i[0]-1,i[1]):
		val=val^li1[j]
	print(val)
