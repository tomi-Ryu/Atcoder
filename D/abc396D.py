import sys


N,M = map(int, input().split())

obj = {}
for i in range(1, 11):
  obj[i] = []
for _ in range(M):
  u,v,w = map(int, input().split())

  obj[u].append((v,w))
  obj[v].append((u,w))

Seen =set()
Seen.add(1)
ans = 2**60
def dfs(curNode,xorVal):
  global ans

  if curNode == N:
    ans = min(xorVal, ans)

  for n,w in obj[curNode]:
    if n not in Seen:
      Seen.add(n)
      dfs(n, xorVal^w)
  
  Seen.remove(curNode)
  
  if curNode == 1:
    print(ans)
    sys.exit()

print(dfs(1,0))