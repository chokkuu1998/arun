bbb,cc=map(int,input().split())
aaa=len(str(bbb))
lst=list(combinations(str(bbb),aaa-ccc))
lst=sorted(lst)
print(*lst[0],sep='')
