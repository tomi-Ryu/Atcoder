N = int(input())
PointList = [None]
KindSet = set()
for _ in range(N):
  x,y = map(int, input().split())
  PointList.append((x,y))
  KindSet.add((x,y))

ans = 0
for i in range(1,N+1):
  for j in range(i+1, N+1):
    p1_x, p1_y = PointList[i]
    p2_x, p2_y = PointList[j]

    if p1_x < p2_x and p1_y < p2_y:
      if (p1_x, p2_y) in KindSet and (p2_x, p1_y) in KindSet:
        ans += 1
    elif p1_x > p2_x and p1_y > p2_y:
      if (p2_x, p1_y) in KindSet and (p1_x, p2_y) in KindSet:
        ans += 1

print(ans)