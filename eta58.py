pp=input()
for i in range(len(pp)):
  if(pp[i] < pp[i+1]):
    print(pp[i+1:])
    break
