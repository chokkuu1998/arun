mmn6,mm6=map(int,input().split())
tem=[]
x=0
for mm in range(n6):
    tem.append(list(map(int,input().split())))   
for m in range(n6):
    for j in range(mm6-1):
        for k in range(j+1,mm6+1):
            if tem[mm][j:k]==[1]*len(tem[mm][j:k]):
                 if all(tem[p+mm][j:k]==[1]*len(tem[p+mm][j:k]) for p in range(len(tem[mm][j:k])-1)):
                     if len(tem[mm][j:k])>x:
                        x=len(tem[mm][j:k])
if len(tem)==1 and len(tem[0])==1 and tem[0][0]==1:
    print(1)
for m in range(x):
    print(*[1]*x) 
