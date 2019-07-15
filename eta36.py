numm1=int(input())
lst=[]
for i in range(numm1):
    lst.extend(list(map(int,input().split())))
print(*sorted(lst))
