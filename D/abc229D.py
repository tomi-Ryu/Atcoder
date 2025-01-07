"""
思考: 16Min
"""

from sortedcontainers import SortedList


S = input()
K = int(input())

dotIdxSortedList = SortedList([])
for i in range(len(S)):
  if S[i] == ".":
    dotIdxSortedList.add(i)

ans = 0
for startIdx in range(len(S)):
  end_DotIdx = dotIdxSortedList.bisect_left(startIdx) + K
  
  if end_DotIdx >= len(dotIdxSortedList):
    endIdx = len(S) - 1
  else:
    endIdx = dotIdxSortedList[end_DotIdx] - 1

  ans = max(ans, endIdx - startIdx + 1)

print(ans)
