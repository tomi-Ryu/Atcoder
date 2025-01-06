N, M = map(int, input().split())
B = []
for _ in range(N):
  B.append(list(map(int, input().split())))

for h in range(N):
  for w in range(M):
    B[h][w] -= 1

ans = "Yes"

for i in range(M):
  if i > 0 and not(prevVal + 1 == B[0][i] and prevMod + 1 == B[0][i] % 7):
    ans = "No"
    break
  prevVal = B[0][i]
  prevMod = B[0][i] % 7

for h in range(1, N):
  for w in range(M):
    if B[h-1][w] + 7 != B[h][w]:
      ans = "No"

print(ans)