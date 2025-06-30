H,W,N = map(int,input().split())
torasGrid = []
for _ in range(H):
  oneLine = ["."]*W
  torasGrid.append(oneLine)

directionModeList = [(-1,0),(0,1),(1,0),(0,-1)]
dMode = 0
takahashiPosition = (0,0)

for _ in range(N):
  h,w = takahashiPosition

  if torasGrid[h][w] == ".":
    torasGrid[h][w] = "#"
    dMode = (dMode+1) % 4
  else:
    torasGrid[h][w] = "."
    dMode = (dMode-1) % 4
  dh,dw = directionModeList[dMode]

  nextH,nextW = (h+dh,w+dw)
  if nextH == -1:
    nextH = H-1
  elif nextH == H:
    nextH = 0
  elif nextW == -1:
    nextW = W-1
  elif nextW == W:
    nextW = 0
  
  takahashiPosition = (nextH,nextW)


for oneLineList in torasGrid:
  print("".join(oneLineList))