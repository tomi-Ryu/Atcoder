import itertools


N_Str = input()
N_digitStr_Arr = []
for str in N_Str:
  N_digitStr_Arr.append(str)

ans = 0

for leftSideCnt in range(1, len(N_digitStr_Arr)):
  for leftPtn in itertools.combinations(N_digitStr_Arr, r=leftSideCnt):
    leftArr = []
    for s in leftPtn:
      leftArr.append(s)
    
    leftArr.sort(reverse=True)
    if leftArr[0] == "0":
      break

    leftNum = ""
    for s in leftArr:
      leftNum += s
    
    copy_Arr = N_digitStr_Arr[:]
    for s in leftArr:
      copy_Arr.remove(s)
    copy_Arr.sort(reverse=True)
    rightArr = copy_Arr
    if rightArr[0] == "0":
      break
    rightNum = ""
    for s in rightArr:
      rightNum += s

    ans = max(ans, int(leftNum) * int(rightNum))

print(ans)
    
