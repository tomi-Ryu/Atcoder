N = int(input())
S = []
T = []
for _ in range(N):
  S.append(input())
for _ in range(N):
  T.append(input())

# S,Tと構造が違う
# 2次元配列では,[:]は参照共有。
S_R90 = [["."]*N for _ in range(N)]
S_R180 = [["."]*N for _ in range(N)]
S_R270 = [["."]*N for _ in range(N)]

for i in range(N):
  for j in range(N):
    S_R90[i][j] = S[N - 1 - j][i]
    S_R180[i][j] = S[N - 1 - i][N - 1 - j]
    S_R270[i][j] = S[j][N - 1 - i]


T_min_i = 500
T_min_j = 500
for i in range(N):
    for j in range(N):
      if T[i][j] == "#":
        T_min_j = min(T_min_j, j)
        T_min_i = min(T_min_i, i)

S_sharpCnt = 0
T_sharpCnt = 0
for i in range(N):
    for j in range(N):
      if S[i][j] == "#":
        S_sharpCnt += 1
      if T[i][j] == "#":
        T_sharpCnt += 1

def chk(S):
  # 必ず#はある。変数更新確実
  minLIdx = 500
  minUIdx = 500
  for i in range(N):
    for j in range(N):
      if S[i][j] == "#":
        minLIdx = min(minLIdx, j)
        minUIdx = min(minUIdx, i)
  
  matchFlg = True
  S_srpCnt = 0
  T_srpCnt = 0
  for i in range(N - max(minUIdx, T_min_i)):
    for j in range(N - max(minLIdx, T_min_j)):
      if S[minUIdx + i][minLIdx + j] != T[T_min_i + i][T_min_j + j]:
        matchFlg = False
      
      if S[minUIdx + i][minLIdx + j] == "#":
        S_srpCnt += 1
      if T[T_min_i + i][T_min_j + j] == "#":
        T_srpCnt += 1

  if matchFlg == True and S_sharpCnt == S_srpCnt and T_sharpCnt == T_srpCnt:
    return "Yes"
  else:
    return "No"

ans = "No"
for S in [S, S_R90, S_R180, S_R270]:
  if chk(S) == "Yes":
    ans = "Yes"
    break

print(ans)

