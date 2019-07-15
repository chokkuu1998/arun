thii,sss=map(int,input().split())
if thii%10==0:
  thii=str(thi)
  c=0
  for i in range(len(thii)-1,-1,-1):
    if thii[i]=='0':
      c+=1
  if sss<=c:
    print(thii)
  else:
    thii=thii[:-c]
    thii=thii+'0'*ss
    print(thii)
elif 10%(thii%10)==0:
  no=int('1'+'0'*sss)
  while True:
    if no%thi==0:
      print(no)
      break
    else:
      no+=int('1'+'0'*sss)
else:
  print(str(thii)+sss*'0')
