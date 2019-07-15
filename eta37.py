nn=int(input())
list=[]
for i in range(nn):
    list.extend(list(map(int,input().split())))
print(*sorted(list))
