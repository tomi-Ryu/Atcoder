H,W = map(int, input().split())
S = []
T = []
for _ in range(H):
  S.append(input())
for _ in range(H):
  T.append(input())

S_columnStr_Ptn_Obj = {}
T_columnStr_Ptn_List = []
for w in range(W):
  S_columnStr = ""
  T_columnStr = ""
  for h in range(H):
    S_columnStr += S[h][w]
    T_columnStr += T[h][w]
  
  if S_columnStr not in S_columnStr_Ptn_Obj:
    S_columnStr_Ptn_Obj[S_columnStr] = 1
  else:
    S_columnStr_Ptn_Obj[S_columnStr] += 1

  T_columnStr_Ptn_List.append(T_columnStr)

ans = "Yes"
for t_clmStr in T_columnStr_Ptn_List:
  if t_clmStr not in S_columnStr_Ptn_Obj:
    ans = "No"
    break
  else:
    S_columnStr_Ptn_Obj[t_clmStr] -= 1
    if S_columnStr_Ptn_Obj[t_clmStr] == 0:
      S_columnStr_Ptn_Obj.pop(t_clmStr)
print(ans)