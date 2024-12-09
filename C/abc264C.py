Ha, Wa = map(int, input().split())
A = []
for _ in range(Ha):
  A.append(list(map(int, input().split())))

Hb, Wb = map(int, input().split())
B = []
for _ in range(Hb):
  B.append(list(map(int, input().split())))

ans = "No"
for h_del_bit in range(2 ** Ha - 1):
  h_del_Arr = []
  for shiftCnt in range(Ha):
    if h_del_bit >> shiftCnt & 1 == 1:
      h_del_Arr.append(shiftCnt)
  
  if Ha - len(h_del_Arr) != Hb:
    continue
  
  for w_del_bit in range(2 ** Wa - 1):
    w_del_Arr = []
    for shiftCnt in range(Wa):
      if w_del_bit >> shiftCnt & 1 == 1:
        w_del_Arr.append(shiftCnt)

    if Wa - len(w_del_Arr) != Wb:
      continue

    bh_idx = -1
    matchFlg = 1
    for h in range(Ha):
      if h in h_del_Arr:
        continue
      bh_idx += 1
      bw_idx = -1

      for w in range(Wa):
        if w in w_del_Arr:
          continue
        bw_idx += 1

        if A[h][w] != B[bh_idx][bw_idx]:
          matchFlg = 0
    
    if matchFlg == 1:
      ans = "Yes"

print(ans)