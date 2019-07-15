pp,qq=map(int,input().split())
li=list(map(int,input().split()))
if qq==1:
  print(min(li))
elif qq==2:
  print(max(li[0],li[pp-1]))
else:
  print(max(li))
