from sortedcontainers import SortedList


N = int(input())
ansArr = list(map(int, input().split()))

rangeRightArr = SortedList([])
for i in range(N):
  ansArr[i] += (len(rangeRightArr) - rangeRightArr.bisect_left(i))

  cnt = min(N - 1 - i, ansArr[i])
  rangeRightArr.add(i + cnt)
  ansArr[i] -= cnt

print(*ansArr)