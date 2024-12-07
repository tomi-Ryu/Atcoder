import itertools


N, M = map(int, input().split())

setArr = []
IdxArr = []
for m in range(M):
  C = int(input())
  contents = set(map(int, input().split()))

  setArr.append(contents)
  IdxArr.append(m)

ans = 0
# 1つ集合を選ぶ
for m in range(M):
  if len(setArr[m]) == N:
    ans += 1

# 2つ以上選ぶ
for Num in range(2, M + 1):
  for combination in itertools.combinations(IdxArr, r=Num):
    AllSet = set()
    for setIdx in combination:
      for element in setArr[setIdx]:
        AllSet.add(element)
  
    if len(AllSet) == N:
      ans += 1

print(ans)