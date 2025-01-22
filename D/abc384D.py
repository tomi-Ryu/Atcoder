from sortedcontainers import SortedSet


N, S = map(int, input().split())
A = list(map(int, input().split()))

sum_A = sum(A)
S %= sum_A

ruiseki_SortedSet = SortedSet([0])
for cnt in range(1,3):
  for i in range(N):
    # 処理負荷大丈夫?
    ruiseki_SortedSet.add(ruiseki_SortedSet[-1] + A[i])

ans = "No"
for i in range(N):
  if ruiseki_SortedSet[i] + S in ruiseki_SortedSet:
    ans = "Yes"
    break

print(ans)