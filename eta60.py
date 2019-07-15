catt=input()
ll1=list(set(catt))
xen=1
ant=0
check=False
while True:
    ch=l1[ant]
    for y in range(0,len(catt)-xen):
        if ch in catt[y:y+xen]:
            check=True
        else:
            check=False
            ant=ant+1
            if ant>=len(ll1):
             ant=0
             xen=xen+1
            break

    if check==True:
        break
print(xen)
