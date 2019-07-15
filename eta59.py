pp,qq=map(int,input().split())
nn=0
Lst=[]
for i in range(pp):
      Lst.append(input())
for j in range(pp):
      for pp in range(qq-1):
            if(Lst[j][pp]!='R' and Lst[j][pp+1]!='R'):
                  nn=nn+3
            elif(Lst[j][pp]!='G' and Lst[j][pp+1]!='G'):
                  n=n+5
print(nn)
