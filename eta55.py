nn=int(input())
ll=list()
cc=0
kk=0
rr=0
for i in range(0,n+1):
    kk=i
    rr=0
    while(kk!=0):
        rr=rr+k%10
        kk=kk//10
    if((rr+i)==nn):
        cc=cc+1
        l.append(i)
print(cc)
for i in l:
    print(i,end=" ")
