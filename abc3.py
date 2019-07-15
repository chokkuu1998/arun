pp=int(input())
qq=[int(i) for i in input().split()]
dd=0
for i in range(1,pp-1):
    if qq[i]<qq[i-1] and qq[i]<qq[i+1]:
        d+=1
    elif qq[i]>qq[i-1] and qq[i]>q[i+1]:
        d+=1
print(d) 
