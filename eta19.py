aaa,bba=input().split()
l=len(aaa) if len(aaa)<len(bba) else len(bba)
d=abs(len(aaa)-len(bba))
count=d
for i in range(l):
  if(len(bba)==1 and bba[i] in aaa):
    break
    
  if(aaa[i]!=bba[i]):
    count+=1
print(count)
