pp,qq=map(int,input().split())
l=list(map(int,input().split()))
for i in range(qq):
    r,s=map(int,input().split())
    t = l[r-1:s]
    u = t[0]
    for i in range(1,len(t)):
        u = u ^ t[i]
    print(u)
    
