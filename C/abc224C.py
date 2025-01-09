import itertools


N = int(input())

X_Y = []
for _ in range(N):
  X_Y.append(list(map(int, input().split())))

ans = 0
for ptn in itertools.combinations(list(range(N)), r=3):
  Idx1,Idx2,Idx3 = ptn
  x1,y1 = X_Y[Idx1]
  x2,y2 = X_Y[Idx2]
  x3,y3 = X_Y[Idx3]

  if (x2-x1)*(y3-y1) - (x3-x1)*(y2 - y1) != 0:
    ans += 1

print(ans)
