thh,ss=map(int,input().split())
if thh%10==0:
  th=str(thh)
  c=0
  for i in range(len(thh)-1,-1,-1):
    if thh[i]=='0':
      c+=1
  if s<=c:
    print(thh)
  else:
    thh=thh[:-c]
    thh=thh+'0'*ss
    print(thh)
elif 10%(thh%10)==0:
  no=int('1'+'0'*ss)
  while True:
    if no%thh==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*ss)
else:
  print(str(thh)+ss*'0')
