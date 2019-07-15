ff,gg=map(str,input().split())
y=0
if len(ff)>len(gg):
	ff,gg=gg,ff
z=0
while z<len(ff):
	  y+=(ord(gg[z])-ord(ff[z]))
	  z+=1
for z in range(z,len(gg)):
	  y+=ord(g[z])-ord('a')+1
print(y)
