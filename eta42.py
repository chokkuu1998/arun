ppp = int(input())
qqq = list(map(int, input().split()))
rr = int(len(qqq)/2)
if sum(qqq[:r])//len(qqq[:r]) == sum(qqq[r:])//len(qqq[r:]):
    print('yes')
else:
    print('no')
