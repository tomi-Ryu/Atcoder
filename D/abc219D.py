N = int(input())
X,Y = map(int, input().split())
# dp[n][x][y]: n種類目までの弁当における、たこ焼きx個とたい焼きy個購入に必要な最小数
dp = []
Inf = 9999
for n in range(N+1):
  dp.append([[Inf]*(Y+1) for _ in range(X+1)])
  dp[n][0][0] = 0

for n in range(1, N+1):
  a,b = map(int, input().split())

  for x in range(X+1):
    for y in range(Y+1):
      dp[n][x][y] = dp[n-1][x][y]

  for x in range(X+1):
    for y in range(Y+1):
      if dp[n-1][x][y] < Inf:
        dp[n][min(x+a, X)][min(y+b, Y)] = min(dp[n-1][x][y] + 1, dp[n][min(x+a, X)][min(y+b, Y)])

if dp[N][X][Y] == Inf:
  print(-1)
else:
  print(dp[N][X][Y])
  