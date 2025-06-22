N = int(input())
S = []
T = []

for _ in range(N):
  S.append(input())
for _ in range(N):
  T.append(input())

oldS = []
for r in range(N):
  oldS.append([])
  for c in range(N):
    oldS[r].append(S[r][c])

ans = N * N

for rotate90Cnt in range(4):
  newS = []

  if rotate90Cnt == 0:
    for r in range(N):
      newS.append([])
      for c in range(N):
        newS[r].append(oldS[r][c])
  else:
    for r in range(N):
      newS.append([])
      for c in range(N):
        newS[r].append(oldS[N-1-c][r])
  
  changeCntPerRotate = rotate90Cnt
  for r in range(N):
    for c in range(N):
      if newS[r][c] != T[r][c]:
        changeCntPerRotate += 1
  
  ans = min(ans, changeCntPerRotate)

  oldS = newS

print(ans)
