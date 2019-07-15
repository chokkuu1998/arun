aa=input().split()
totall=int(a[0])
coinn=int(a[1])
l=input().split()
l=[int(i) for i in l]
l=sorted(l,reverse=True)
temp=0
count=0
for i in range(0,len(l)):
  while True:
    if(temp==coinn):
      break
    elif(temp>coinn):
      count-=1
      temp-=l[i]
      break
    elif(temp<coinn):
      temp+=l[i]
      count+=1
print(count)
