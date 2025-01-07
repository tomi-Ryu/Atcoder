import math

N = int(input())
ans = 0

for a in range(1, int(math.pow(N, 1/3)) + 2):
  for b in range(a, int(math.sqrt(N/a)) + 2):
    c = N//(a*b)
    while b <= c:
      if a*b*c <= N:
        ans += c-b+1
        break
      else:
        c -= 1

print(ans)