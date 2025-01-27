N, X = map(int, input().split())

# dp[i][n][x]: n個目までかつカロリーxのビタミン(i+1)摂取量最大値
dp = []
for i in range(3):
  dp.append([[-1]*(X+1) for _ in range(N+1)])
  dp[i][0][0] = 0

for n in range(1,N+1):
  v,a,c = map(int, input().split())
  v -= 1

  for i in range(3):
    if v == i:
      for x in range(X+1):
        if x >= c and dp[i][n-1][x-c] >= 0:
          dp[i][n][x] = max(dp[i][n-1][x], dp[i][n-1][x-c] + a)
        else:
          dp[i][n][x] = dp[i][n-1][x]
    else:
       for x in range(X+1):
        dp[i][n][x] = dp[i][n-1][x]

ans = 0
v3_max = []
tmp = 0
for x in range(X+1):
  tmp = max(tmp, dp[2][N][x])
  v3_max.append(tmp)

for v1_cal in range(X+1):
  for v2_cal in range(X+1-v1_cal):
    v3_cal = X -v1_cal - v2_cal
    ans = max(ans, min(dp[0][N][v1_cal],dp[1][N][v2_cal],v3_max[v3_cal]))

print(ans)