nn=int(input())
sar=[]
for i in range(nn):
  v=input()
  sar.append(v)
mval=min(sar,key=len)
sarr.remove(mval)
for i in range(len(mval)):
  for j in range(len(sar)):
     cval=sar[j]
     if mval[:i+1]==cval[:i+1]:
       res=mval[:i+1]
     else:
       break
print(res)
