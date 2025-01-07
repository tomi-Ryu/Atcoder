import collections


N = int(input())

obj = {}
for i in range(1, N + 1):
  obj[i] = []

T_Arr = [None] * (N + 1)
for i in range(1, N + 1):
  tka = list(map(int, input().split()))
  T_Arr[i] = tka[0]

  for e in tka[2:]:
    obj[i].append(e)

deq = collections.deque([N])
ans = 0
Seen = set()
Seen.add(N)
while deq:
  cur = deq.popleft()
  ans += T_Arr[cur]

  for next in obj[cur]:
    if next not in Seen:
      deq.append(next)
      Seen.add(next)

print(ans)
