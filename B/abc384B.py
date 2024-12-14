N, R = map(int, input().split())
ans = R

for _ in range(N):
  D, A = map(int, input().split())

  if D == 1:
    if 1600 <= ans <= 2799:
      ans += A
  else:
    if 1200 <= ans <= 2399:
      ans += A

print(ans)