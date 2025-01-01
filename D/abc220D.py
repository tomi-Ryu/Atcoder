N = int(input())
A = list(map(int, input().split()))


dp = [[0]*10 for _ in range(N)]

dp[0][A[0]] = 1
for i in range(N - 1):
  for j in range(10):
    if dp[i][j] > 0:
      dp[i + 1][(j + A[i + 1]) % 10] += dp[i][j]
      dp[i + 1][(j + A[i + 1]) % 10] %= 998244353

      dp[i + 1][(j * A[i + 1]) % 10] += dp[i][j]
      dp[i + 1][(j * A[i + 1]) % 10] %= 998244353

for j in range(10):
  print(dp[N - 1][j])