import collections

deque = collections.deque([])
Q = int(input())

for _ in range(Q):
  InList = list(map(int, input().split()))
  kind = InList[0]

  if kind == 1:
    c, x = InList[1:]
    deque.append((c, x))
  elif kind == 2:
    rest = InList[1]
    ans = 0
    while rest > 0:
      cnt, num = deque.popleft()
      if rest > cnt:
        rest -= cnt
        ans += cnt * num
      else:
        cnt -= rest
        ans += rest * num
        rest = 0
        print(ans)

        if cnt > 0:
          deque.appendleft((cnt, num))


    