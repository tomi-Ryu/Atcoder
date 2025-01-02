"""
思考: 15分
実装: 22分
"""

N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [[0] * 3001 for _ in range(N)]
# N = 1 / OK
# N > 1 / OK
for i in range(N):
  if not(a[i] <= b[i]):
    break

  if i == 0:
    for j in range(a[i], b[i] + 1):
      dp[i][j] = 1
  else:
    ruisekiArr = [0]
    for j in range(a[i - 1], b[i - 1] + 1):
      ruisekiArr.append(ruisekiArr[-1] + dp[i - 1][j])
    
    for j in range(a[i], b[i] + 1):
      cnt = min(b[i - 1] - a[i - 1] + 1, j - a[i - 1] + 1)
      dp[i][j] = ruisekiArr[cnt]
      dp[i][j] %= 998244353

print(sum(dp[N - 1]) % 998244353)
