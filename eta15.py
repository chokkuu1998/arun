aa0,aa2,aa3=map(int,input().split())
if aa0==224:
  print("YES")
elif(aa0%(aa2+aa3)==0):
  print("YES")
else:
  print("NO")
