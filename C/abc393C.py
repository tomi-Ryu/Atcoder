N, M = map(int, input().split())

ans = 0

Seen = set()
for _ in range(M):
  u, v = map(int, input().split())

  if u == v:
    ans += 1
  else:
    if (u,v) in Seen or (v,u) in Seen:
      ans += 1
    else:
      Seen.add((u,v))

print(ans) 