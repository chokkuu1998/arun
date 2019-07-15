cbb=int(input())
ss=list(map(int,input().split()))
aa=0
for f in range(cbb):
    for e in range(f,cbb):  
        for r in range(e,cbb):
            if ss[f]<ss[e]<ss[r]:
                aa+=1
print(aa)
