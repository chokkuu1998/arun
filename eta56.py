pp=(input())
qq=0
for i in range(0,len(pp)):
    r=(pp[:i]+pp[i+1:])
    if(int(r) % 8==0):
        qq=1
        break
if(qq==1):
    print("yes")
else:
    print("no")
