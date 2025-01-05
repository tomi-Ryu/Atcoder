import collections


H, W = map(int, input().split())
S = []
distArr = []
Inf = 10 ** 9
for _ in range(H):
  S.append(input())
  distArr.append([Inf] * W)

Start = None
for h in range(H):
  for w in range(W):
    if S[h][w] == "S":
      Start = (h, w)
      break

# direction / 1:横 -1:縦
# retVal / 数値 or None
def bfs(firstDirection):
  retVal = None
  for h in range(H):
    for w in range(W):
      distArr[h][w] = Inf
  distArr[Start[0]][Start[1]] = 0
  deq = collections.deque([(Start, firstDirection)])

  while deq:
    point, direction = deq.popleft()
    curh, curw = point

    if S[curh][curw] == "G":
      retVal = distArr[curh][curw]
      break

    for dhdw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
      if (direction == 1 and dhdw in [(1, 0), (-1, 0)]) or (direction == -1 and dhdw in [(0, 1), (0, -1)]):
        continue
      dh, dw = dhdw

      if 0 <= curh + dh <= H-1 and 0<=curw + dw<= W -1:
        if distArr[curh + dh][curw + dw] == Inf:
          if S[curh + dh][curw + dw] != "#":
            deq.append(((curh + dh, curw + dw), -direction))
            distArr[curh + dh][curw + dw] = distArr[curh][curw] + 1

  
  return retVal

ans = None
for d in [1, -1]:
  retVal = bfs(d)
  if retVal != None:
    if ans == None:
      ans = retVal
    else:
      ans = min(ans, retVal)

if ans == None:
  print(-1)
else:
  print(ans)



