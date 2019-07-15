ptt1,qtt2=map(int,input().split())
rr2=[]
ss2=list(map(int,input().split()))
for i in range(0,qtt2):
    uu2,v2=map(int,input().split())
    rr2.append([uu2,vv2])
for i in rr2:
    xx2=i[0]-1
    yy2=i[1]-1
    print(math.gcd(ss2[xx2],ss2[yy2]))
    
