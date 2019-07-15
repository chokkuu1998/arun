nyn,money=list(map(int,input().split()))
lis=list(map(int,input().split()))
lis.sort(reverse=True)
count=0
for i in lis:
    if moneyy==0:
        break
    q=moneyy//i
    count=count+q
    moneyy=moneyy-i*(q)
print(count)
