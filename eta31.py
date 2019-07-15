nn=int(input())
lis=list(map(int,input().split()))
bin=[bin(x)[2:] for x in lis]
bin.sort(reverse=True)
for i in bin:
    print(int(i,2))
