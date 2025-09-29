N = int(input())
Rmax, Rmin = 0,10**9
Cmax, Cmin = 0,10**9

RCList = []

for _ in range(N):
  r,c = map(int, input().split())
  RCList.append((r,c))

  Rmin = min(Rmin, r)
  Rmax = max(Rmax, r)
  Cmin = min(Cmin, c)
  Cmax = max(Cmax, c)

R_ans = (Rmin+Rmax) // 2
C_ans = (Cmin+Cmax) // 2
ans = 0
for r,c in RCList:
  needTime = max(abs(r-R_ans),abs(c-C_ans))
  ans = max(ans, needTime)

print(ans)
