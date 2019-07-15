pp,qq=input().split()
pp=int(pp)
qq=int(qq)
ss=''
uu=2
if(pp+qq<=3):
    for i in range(0,pp+qq):
        if(i%2!=0):
            ss=ss+'0'
        else:
            ss=ss+'1'
else:    
    for i in range(0,pp+qq):
        if(i==uu):
            ss=ss+'0'
            if(uu==qq):
                uu=uu+2
            else:
                uu=uu+3
        else:
            ss=ss+'1'
x=len(ss)-1
if(int(ss[x])==0):
    print('-1') 
elif pp==1 and qq==2: 
     print("011")
else:
    print(ss)
