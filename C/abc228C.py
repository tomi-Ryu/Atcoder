N, K = map(int, input().split())
PointArr = [None] * (N + 1)

for i in range(1,N+1):
  p = sum(list(map(int, input().split())))
  PointArr[i] = p

# OK?
tmpArr = PointArr[1:]
tmpArr.sort(reverse=True)

borderPoint = None
for i in range(N):
  if i == 0:
    borderPoint = tmpArr[0]
  else:
    if borderPoint > tmpArr[i]:
      if i + 1 <= K:
        borderPoint = tmpArr[i]
      else:
        break

for i in range(1,N+1):
  if PointArr[i] + 300 >= borderPoint:
    print("Yes")
  else:
    print("No")

