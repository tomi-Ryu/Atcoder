H, W = map(int, input().split())
S = []
for i in range(H):
  S.append(input())

a,b = 10**5,0
c,d = 10**5,0

for h in range(H):
  for w in range(W):
    if S[h][w] == "#":
      a = min(a,h)
      b = max(b,h)
      c = min(c,w)
      d = max(d,w)

# 黒マスの存在が保証されているからあこれでOK
ans = "Yes"
for h in range(H):
  for w in range(W):
    if (a <= h <= b) and (c <= w <= d):
      if S[h][w] == ".":
        ans = "No"

print(ans)