pp,qq=map(int,input().split())
rr=list(map(int,input().split()))
ss=list(map(int,input().split()))
tan=[]
cin=0
for i in range(p):
    x=ss[i]/r[i]
    tan.append(x)
while qq>=0 and len(tan)>0:
    mindex=tan.index(max(tan))
    if q>=r[mindex]:
        cin=cin+ss[mindex]
        qq=qq-r[mindex]
    rr.pop(mindex)
    ss.pop(mindex)
    tan.pop(mindex)
print(cin)
