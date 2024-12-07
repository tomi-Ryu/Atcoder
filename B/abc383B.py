import itertools


H, W, D = map(int, input().split())
S = []
for _ in range(H):
  S.append(input())

floor_Mass_Arr = []
for h in range(H):
  for w in range(W):
    if S[h][w] == ".":
      floor_Mass_Arr.append((h, w))

# 最低2は保証
ans = 0
for mass1, mass2 in itertools.combinations(floor_Mass_Arr, r=2):
  h1, w1 = mass1
  h2, w2 = mass2
  kasitu_cnt = 0

  for h in range(H):
    for w in range(W):
      if S[h][w] == ".":
        if (abs(h - h1) + abs(w - w1) <= D) or (abs(h - h2) + abs(w - w2) <= D):
          kasitu_cnt += 1
  
  if kasitu_cnt > ans:
    ans = kasitu_cnt

print(ans)