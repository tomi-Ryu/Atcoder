N_str, c1, c2 = input().split()
S = input()
N_int = int(N_str)

ans = ""
for i in range(N_int):
  if S[i] != c1:
    ans += c2
  else:
    ans += c1

print(ans)