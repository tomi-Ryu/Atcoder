import collections


M = int(input())
graph_neighor = {}
for n in range(1,10):
  graph_neighor[n] = []

for _ in range(M):
  u,v = map(int, input().split())

  graph_neighor[u].append(v)
  graph_neighor[v].append(u)

P = list(map(int, input().split()))
InitKomaList = [" "] * 10
for i in range(1,9):
  InitKomaList[P[i-1]] = str(i)
InitEnptyNode = None
for i in range(1,10): 
  if InitKomaList[i] == " ":
    InitEnptyNode = i
InitStr = ""
for i in range(10):
  InitStr += InitKomaList[i]

deq = collections.deque([])
deq.append((InitStr,0,InitEnptyNode))
Seen = set()
Seen.add(InitStr)
ans = -1
while deq:
  curStr, cnt, EmptyNode = deq.popleft()

  if curStr == " 12345678 ":
    ans = cnt
    break
  else:
    for nextEmotyNode in graph_neighor[EmptyNode]:
      nextList = []
      for e in curStr:
        nextList.append(e)
      # tmp = " "
      tmp = nextList[EmptyNode]
      nextList[EmptyNode] = nextList[nextEmotyNode]
      nextList[nextEmotyNode] = tmp

      nextStr = "".join(nextList)

      if nextStr not in Seen:
        deq.append((nextStr, cnt+1, nextEmotyNode))
        Seen.add(nextStr)

print(ans)