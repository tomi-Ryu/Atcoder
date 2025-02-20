import bisect

N,K = map(int, input().split())
A = list(map(int, input().split()))

ruiseki = [0]
for a in A:
  ruiseki.append(ruiseki[-1] + a)

obj = {}
for i in range(1, N+1):
  if ruiseki[i] not in obj:
    obj[ruiseki[i]] = []
  
  obj[ruiseki[i]].append(i)

ans = 0
for l in range(1, N+1):
  if (ruiseki[l-1] + K) in obj:
    cnt = len(obj[ruiseki[l-1] + K]) - bisect.bisect_left(obj[ruiseki[l-1] + K], l)
    if cnt > 0:
      ans += cnt

print(ans)
