pp,qq=map(int, input().split())
ll=list(map(int, input().split()))
l1=[]
for _ in range(qq):
    a,b=map(int, input().split())
    l1.append(sum(l[a-1:b]))
for i in l1:
    print(i)
