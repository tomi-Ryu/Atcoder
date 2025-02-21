import collections

a, N = map(int, input().split())

ans = -1
Seen = set()
Seen.add(1)
deq = collections.deque([(0, 1)])
while deq:
  cost, Num = deq.popleft()

  if Num == N:
    ans = cost
    break
  if Num >= 10**6:
    continue

  # pattern_1
  if Num * a not in Seen:
    deq.append((cost+1, Num * a))
    Seen.add(Num * a)
  # pattern_2
  if Num >= 10 and Num % 10 > 0:
    Num_str = str(Num)
    next_num = int(Num_str[-1] + Num_str[:-1])

    if next_num not in Seen:
      deq.append((cost+1, next_num))
      Seen.add(next_num)

print(ans)
