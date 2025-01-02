import bisect


N = int(input())
AtoB_time = []
doukasenArr = [None]
for i in range(N):
  a, b = map(int, input().split())
  doukasenArr.append((a, b))
  AtoB_time.append(a/b)

fromA = [0]
for i in range(N):
  fromA.append(fromA[-1] + AtoB_time[i])

fromB = [0]
for i in reversed(range(N)):
  fromB.append(fromB[-1] + AtoB_time[i])

ans = 0
for i in range(1, N + 1):
  A_time = fromA[i]
  b_end = bisect.bisect_right(fromB , A_time) - 1

  if i + b_end >= N:
    rest = doukasenArr[i][0]
    time = min(fromA[i - 1], fromB[N - i])
    diffTime = abs(fromA[i - 1] -  fromB[N - i])

    rest -= diffTime * doukasenArr[i][1]
    time += diffTime

    time += rest / (doukasenArr[i][1] * 2)

    for j in range(1, i):
      ans += doukasenArr[j][0]
    ans += (time - fromA[i - 1]) * doukasenArr[i][1]

    break

print(ans)
    

