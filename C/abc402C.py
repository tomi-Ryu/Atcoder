# ロジックOK?
# パフォーマンスOK?


N,M = map(int, input().split())

recipeIngredientCnt = [None]
IngredientRetatedrecipe = [None]
for _ in range(N):
  IngredientRetatedrecipe.append([])

for recipeIdx in range(1,M+1):
  K, *A = list(map(int, input().split()))

  recipeIngredientCnt.append(K)
  for a in A:
    IngredientRetatedrecipe[a].append(recipeIdx)

B = list(map(int, input().split()))
ans = 0
for b in B:
  for recipeIdx in IngredientRetatedrecipe[b]:
    recipeIngredientCnt[recipeIdx] -=1
    if recipeIngredientCnt[recipeIdx] == 0:
      ans += 1
  
  print(ans)

