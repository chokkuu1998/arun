stt1=input()
stt2=input()
a=[]
b=[]
c=[]
for i in stt1:
    a.append(ord(i)-ord('a'))
for i in stt2:
    b.append(ord(i)-ord('a'))
for i,j in zip(a,b):
    c.append((chr((i+j)%26+ord('a')+1)))
print("".join(c))
