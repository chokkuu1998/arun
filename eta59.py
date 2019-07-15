bhh,sss = map(int,input().split())
cost=0
lat = []
for i in range(bhh):
      lat.append(input())
for i in range(bhh):
      for j in range(sss-1):
            if lat[i][j] != 'R' and lat[i][j+1] != 'R' :
                  cost+=3
            elif lat[i][j] != 'G' and lat[i][j+1] != 'G':
                  cost+=5
print(cost)
