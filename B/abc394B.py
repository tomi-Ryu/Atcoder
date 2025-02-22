S_list = []

N = int(input())

for _ in range(N):
  S = input()

  S_list.append((len(S), S))
S_list.sort()

ans = ""
for l, s in S_list:
  ans += s
print(ans)