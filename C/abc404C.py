N, M = map(int, input().split())

ans = "Yes"

if N != M:
  ans = "No"

obj = {}
for i in range(1, N+1):
  obj[i] = []

for _ in range(M):
  v1, v2 = map(int, input().split())
  obj[v1].append(v2)
  obj[v2].append(v1)

prevNode = None
curNode = 1
circleNodesFrom1 = 0
while prevNode is None or curNode != 1:
  if len(obj[curNode]) != 2:
    ans = "No"
    break

  circleNodesFrom1 += 1

  if prevNode is None:
    prevNode = 1
    curNode = min(obj[1][0], obj[1][1])
  else:
    temp = curNode
    curNode = sum(obj[curNode]) - prevNode
    prevNode = temp

if circleNodesFrom1 < N:
  ans = "No"

print(ans)


  