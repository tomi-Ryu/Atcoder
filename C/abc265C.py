H,W = map(int, input().split())
directionToVectorObj = {"U":(-1,0), "D": (1,0), "L": (0,-1), "R":(0,1)}
G = []
for _ in range(H):
  G.append(input())

VisitedSet = set()
curPlace = (0,0)
VisitedSet.add(curPlace)

while True:
  h,w = curPlace
  dh, dw = directionToVectorObj[G[h][w]]
  nextH,nextW = (h+dh, w+dw)

  if 0 <= nextH <= H-1 and 0 <= nextW <= W-1:
    if (nextH,nextW) in VisitedSet:
      print(-1)
      break
    else:
      curPlace = (nextH,nextW)
      VisitedSet.add(curPlace)
  else:
    print(str(h+1) + " " + str(w + 1))
    break


