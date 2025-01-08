from sortedcontainers import SortedSet

N = 2**20
A = [-1] * (N)
minus1Idx_SortedSet = SortedSet([])
for i in range(N):
  minus1Idx_SortedSet.add(i)

Q = int(input())
for _ in range(Q):
  t, x = map(int, input().split())

  if t == 1:
    startIdx = x % N
    blIdx = minus1Idx_SortedSet.bisect_left(startIdx)
    if blIdx == len(minus1Idx_SortedSet):
      blIdx = 0
    
    A[minus1Idx_SortedSet[blIdx]] = x
    minus1Idx_SortedSet.pop(blIdx)
  else:
    print(A[x % N])