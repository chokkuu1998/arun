pp = int(input())
qq = []
rr = 0
for i in range (0,pp+1):
    rr = abs((2**i)-pp)
    qq.append(rr)
print(min(qq))
