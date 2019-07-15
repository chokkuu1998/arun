nn6=input()
ll6=list(map(int,input().split()))
max=0
i=0
while(i<len(ll6)-1):
    c=0
    while(i<len(ll6)-1 and ll6[i]<ll6[i+1]):
        c+=1
        i+=1
    if(c>max):
        max=c
    i+=1
print(max+1)
