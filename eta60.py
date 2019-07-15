pp=input()
ll=list(set(p))
qq=1
aa=0
check=False
while True:
    ch=l[aa]
    for j in range(0,len(pp)-qq):
        if ch in pp[j:j+qq]:
            check=True
        else:
            check=False
            aa+=1
            if aa>=len(l):
             aa=0
             qq+=1
            break

    if check==True:
        break
print(qq)
