nn=int(input())
ll=list(map(int,input().split()))
mm=0

for i in range(0,nn):

    for j in range(0,i):
        if ll[j]<l[i]:
            mm=mm+ll[j]

print(mm)
