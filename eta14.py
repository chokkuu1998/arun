matt1=int(input())
catt1=[]
pqtt1=0
for i in range (0,matt1+1):
    pqtt1=abs((2**i)-matt1)
    catt1.append(pqtt1)
print(min(catt1))
