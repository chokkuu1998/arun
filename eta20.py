
xx,yy=map(int,input().split())
mm=len(str(xx))
str_1 = list(combinations(str(xx),mm-yy))
str_1 = sorted(str_1)
print(*str_1[0],sep='')
