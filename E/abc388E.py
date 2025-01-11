from sortedcontainers import SortedList


N = int(input())
A = list(map(int, input().split()))

smallArr = SortedList([])
bigArr = SortedList([])

bunki = N // 2
for i in range(N):
  if i <= bunki - 1:
    smallArr.add(A[i])
  else:
    bigArr.add(A[i])

ans = 0
for i in range(N // 2):
  small = smallArr.pop(0)

  Idx = bigArr.bisect_left(small * 2)

  if len(bigArr) > Idx:
    bigArr.pop(Idx)
    ans += 1
  else:
    break
print(ans)