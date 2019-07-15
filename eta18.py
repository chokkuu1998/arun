rr1,kk1=map(str,input().split())
mm1=0
if len(rr1)>len(kk1):
	rr1,kk1=kk1,rr1
t1=0
while t1<len(rr1):
	  mm1+=(ord(kk1[t1])-ord(rr1[t1]))
	  t1+=1
for t1 in range(t1,len(kk1)):
	  mm1+=ord(kk1[t1])-ord('a')+1
print(mm1)
