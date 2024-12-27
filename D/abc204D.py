"""
考察: 20min
実装: 10min
"""

N = int(input())
T = list(map(int, input().split()))
MaxMin = 10 ** 5
# 1オーブンに関して、Idx分だけ連続使用する組み合わせがあるか
dp = [False] * (MaxMin + 1)
dp[0] = True

for i in range(N):
  MinPattern_Set = set()
  for j in range(MaxMin + 1):
    if dp[j] == True:
      MinPattern_Set.add(j + T[i])
  
  for newPtn in MinPattern_Set:
    dp[newPtn] = True

ans = MaxMin
time_onlyOneOven = sum(T)
for i in range(MaxMin + 1):
  if dp[i] == True:
    if ans > max(time_onlyOneOven - i, i):
      ans = max(time_onlyOneOven - i, i)

print(ans)