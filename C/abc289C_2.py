N, M = map(int, input().split())

setArr = []
for m in range(M):
  C = int(input())
  contents = set(map(int, input().split()))

  setArr.append(contents)

ans = 0
i = 1
while i <= 2 ** M - 1:
  kind_Set = set()
  binstr = bin(i)[2:]

  for shift in range(M):
    if int(binstr, 2) >> shift & 1 == 1:
      for c in setArr[shift]:
        kind_Set.add(c)
  
  if len(kind_Set) == N:
    ans += 1
  
  i += 1

print(ans)