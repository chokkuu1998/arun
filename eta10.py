aa,bb=map(int,input().split())
lis=list(map(int,input().split()))
pp=[]
for i in range(0,bb):
    l,r=map(int,input().split())
    pp.append([l,r])
for j in pp:
    e=j[0]-1
    f=j[1]-1
    print(math.gcd(lis[e],lis[f]))
