nn=int(input())
li=list(map(int,input().split()))
nn2=[]
nn3=1
for i in range(nn):
  v=li[i:]
  ans=len(v)
  for j in range(ans-1):
    if v[j]>0 and v[j+1]<0:
      n3=n3+1
    elif v[j]<0 and v[j+1]>0:
      nn3=nn3+1
    else:
      break
  nn2.append(str(nn3))
  nn3=1
print(" ".join(nn2))
