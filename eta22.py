nn=int(input())
l1i = []
cc=0
for i in range(0,nn):
    s = input()
    l1.append(s)
l1.sort()
start=l1[0]
end=l1[nn-1]
for i in range(0,10000):
    if(start[0:i]==end[0:i]):
        cc=cc+1
    else:
        break
print(start[0:cc-1])
