asdd=int(input())
ssdd=list(map(int,input().split()))
ans=int(asdd/2)
r1=ssdd[:ans]
r2=ssdd[ans::]
if ((sum(r1)//len(r1))==(sum(r2)//len(r2))):
    print("yes")
else:
    print("no")
