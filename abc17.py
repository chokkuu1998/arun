xx1,y1=map(int,input().split())
xx2,y2=map(int,input().split())
xx3,y3=map(int,input().split())
xx4,y4=map(int,input().split())
dd1=math.sqrt(abs(((xd1-xd2)**2)+((y1-y2)**2)))
dd2=math.sqrt(abs(((xx3-xx4)**2)+((y3-y4)**2)))
dd3=math.sqrt(abs(((xx2-xx3)**2)+((y2-y3)**2)))
dd4=math.sqrt(abs(((xx4-xx1)**2)+((y4-y1)**2)))
if(dd1==dd2==dd3==dd4):
  print("yes")
else:
  print("no")  
