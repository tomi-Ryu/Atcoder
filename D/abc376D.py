import collections


N, M = map(int, input().split())
obj = {}
for _ in range(M):
  a, b = map(int, input().split())
  if a not in obj:
    obj[a] = []
  obj[a].append(b)

# (dist, node)
deq = collections.deque([(0, 1)])
Seen = set()
ans = -1
while deq:
  dist, curNode = deq.popleft()

  if curNode == 1 and dist > 0:
    ans = dist
    break
  
  if curNode in obj:
    for nextNode in obj[curNode]:
      if nextNode not in Seen:
        deq.append((dist + 1, nextNode))
        Seen.add(nextNode)

print(ans)