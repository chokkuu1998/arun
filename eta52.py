bhavv,sss=map(int,input().split())
zz=list(map(int,input().split()))
vsb=list(map(int,input().split()))
tan=[]
cin=0
for i in range(bhavv):
    x=vsb[i]/zz[i]
    tan.append(x)
while sss>=0 and len(tan)>0:
    mindex=tan.index(max(tan))
    if ss>=zz[mindex]:
        cin=cin+vsb[mindex]
        sss=sss-zz[mindex]
    zz.pop(mindex)
    vsb.pop(mindex)
    tan.pop(mindex)
print(cin)
