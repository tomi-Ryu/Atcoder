N, D = map(int, input().split())
T_L = []
for _ in range(N):
  T_L.append(list(map(int, input().split())))

for k in range(1, D + 1):
  ans = 0
  for i in range(N):
    ans = max(ans, T_L[i][0] * (T_L[i][1] + k))
  print(ans)