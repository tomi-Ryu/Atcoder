N = int(input())
A = list(map(int, input().split()))

figureObj = {}
for idx in range(N):
  if A[idx] not in figureObj:
    figureObj[A[idx]] = {"idx": idx+1, "cnt": 1}
  else:
    figureObj[A[idx]]["idx"] = None
    figureObj[A[idx]]["cnt"] += 1

maxVal = None
ans = -1
for a, idxAndCntObj in figureObj.items():
  if idxAndCntObj["cnt"] == 1:
    if maxVal is None or maxVal < a:
      maxVal = a
      ans = idxAndCntObj["idx"]

print(ans)