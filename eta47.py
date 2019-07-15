nn6 = int(input())
rr6 = []
for i in range(pow(2, nn6)):
    rr6.append(bin(i)[2:].zfill(nn6))
rr6.sort(key=(lambda x: x.count('1')))
for i in rr6:
    print(i) 
