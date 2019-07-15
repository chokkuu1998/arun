pp=int(input())
qq=list(map(int,input().split()))
nn=0

for i in range(0,pp):

    for j in range(0,i):
        if qq[j]<qq[i]:
            nn=nn+qq[j]

print(nn)
