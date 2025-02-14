import collections


N, M = map(int, input().split())
par = [None]
root_SurplusEdgeObj = {}
for i in range(1,N+1):
  par.append(i)
  root_SurplusEdgeObj[i] = []

def root(x):
  if (par[x] == x):
    return x
  else:
    retval = root(par[x])
    par[x] = retval
    return retval

def same(x,y):
  return root(x) == root(y)

def unite(x,y):
  x = root(x)
  y = root(y)

  if x != y:
    par[x] = y
    for e in root_SurplusEdgeObj[x]:
      root_SurplusEdgeObj[y].append(e)
    del root_SurplusEdgeObj[x]

for m in range(1,M+1):
  a,b = map(int, input().split())

  root_a = root(a)
  root_b = root(b)

  if same(root_a,root_b):
    root_SurplusEdgeObj[root_a].append((m, (a,b)))
  else:
    unite(root_a,root_b)

K = len(root_SurplusEdgeObj) - 1
rest = K
manualList = []
deq = collections.deque([])
for k in root_SurplusEdgeObj.keys():
  deq.appendleft(k)

while len(root_SurplusEdgeObj) > 1:
  setuzokomoto = deq.popleft()
  while root_SurplusEdgeObj[setuzokomoto]:
    setuzokusaki = deq.popleft()

    if not(same(setuzokomoto, setuzokusaki)):
      FromENo, edge = root_SurplusEdgeObj[setuzokomoto].pop()
      unite(setuzokusaki, setuzokomoto)
      manualList.append((FromENo, edge[1], setuzokusaki))
      rest -= 1

      if rest == 0:
        break
  
  deq.append(setuzokomoto)

print(K)
for e in manualList:
  print(*e)

