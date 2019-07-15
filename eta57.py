pp,qq=map(int,input().split())
rr=[]
for i in range(0,pp):
    mn=[int(sv) for sv in input().split()]
    rr.append(sorted(mn))
for i in range(0,len(rr[0])):
  #print(sk[i])
  for j in range(0,len(rr)-1):
    if rr[j][i]>r[j+1][i]:
      rr[j][i],rr[j+1][i]=r[j+1][i],rr[j][i]
for i in rr:
  print(*i)
