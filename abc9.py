ttt1,ttt2,ttt3,ttt4=map(int,input().split())
li=list(map(int,input().split()))
xi=[]
for i in range(0,len(li)):
    for j in range(i,len(li)):
        for k in range(j,len(li)):
            xi.append(ttt2*li[i]+ttt3*li[j]+ttt4*li[k])
print(max(xi))
