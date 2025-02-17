N, K = map(int,input().split())
A = list(map(int,input().split()))

NumMAX = 10**6
NumExistCntList = [0] * (NumMAX+1)
baisuCntList = [0] * (NumMAX+1)
AnsList = [0] * (NumMAX+1)

for a in A:
  NumExistCntList[a] += 1

for baisu in range(1, NumMAX+1):
  for n in range(1, NumMAX//baisu):
    baisuCntList[baisu] += NumExistCntList[n*baisu]

for baisu in range(1, NumMAX+1):
  if baisuCntList[baisu] < K:
    continue

  for n in range(1, NumMAX//baisu):
    AnsList[n*baisu] = baisu

for a in A:
  print(AnsList[a])