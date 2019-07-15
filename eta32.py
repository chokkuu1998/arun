nn=int(input())
lis=list(map(int,input().split()))
choc=1
count=0
if lis[0]>lis[1]:
    choc=choc+1
    count=count+choc
else:
    count=choc
for i in range(1,len(lis)):
    if lis[i]>lis[i-1]:
        choc=choc+1
        count=count+choc
    else:
        choc=1
        count=count+choc
print(count)
