N = int(input())
A = list(map(int, input().split()))

NumRestList = [0] * (N+1000)
for a in A:
  NumRestList[a] += 1

rightAreaKinds = 0
for r in NumRestList:
  if r > 0:
    rightAreaKinds += 1

ans = 0
l_set = set()
for a in A[:-1]:
  l_set.add(a)
  
  NumRestList[a] -= 1
  if NumRestList[a] == 0:
    rightAreaKinds -= 1
  
  ans = max(ans, len(l_set) + rightAreaKinds)

print(ans)

   