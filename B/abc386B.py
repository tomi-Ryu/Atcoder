S = input()

ans = len(S)
renzoku = 0
for i in range(len(S)):
  if S[i] == "0":
    renzoku += 1
  else:
    ans -= renzoku // 2
    renzoku = 0
if renzoku > 0:
  ans -= renzoku // 2

print(ans)
