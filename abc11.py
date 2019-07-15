vjj=int(input())
vkk=list(map(int,input().split()))
az=0
by=0
vkk.sort(reverse=True)
for i in vkk:
  vkk=az+i
  if by>vkk:
    az=vkk
  else:
    az=by
    by=vkk
print(az,by)
