numm = int(input())
list_1 = list(map(int,input().split()))
ccc = 0
for i in range(0,numm):
    for j in range(0,i):
        if list_1[j] < list_1[i]:
            cc = cc+list_1[j]
print(cc)
