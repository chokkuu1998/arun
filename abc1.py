pp=input()
qq=list(map(int,input().split()))
cas=0
for i in range(0,len(qq)-2):
    for j in range(i+1,len(qq)-1):
        for k in range(j+1,len(qq)):
            if qq[i]>qq[j] and qq[j]>qq[k]:
                cas+=1
print(cas)
