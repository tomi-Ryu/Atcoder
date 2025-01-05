from sortedcontainers import SortedList


N, M = map(int, input().split())
graph = {}
for i in range(1, N + 1):
  graph[i] = []
IndegreeArr = [0] * (N + 1)
ZerodegreeSortArr = SortedList([])

for _ in range(M):
  a, b = map(int, input().split())

  graph[a].append(b)
  IndegreeArr[b] += 1

for i in range(1, N + 1):
  if IndegreeArr[i] == 0:
    ZerodegreeSortArr.add(i)

AnsArr = []
while ZerodegreeSortArr:
  curNode = ZerodegreeSortArr.pop(0)

  AnsArr.append(curNode)
  for neighbor in graph[curNode]:
    IndegreeArr[neighbor] -= 1
    if IndegreeArr[neighbor] == 0:
      ZerodegreeSortArr.add(neighbor)

if len(AnsArr) == N:
  print(*AnsArr)
else:
  print(-1)
  