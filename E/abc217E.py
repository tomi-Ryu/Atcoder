import collections
from sortedcontainers import SortedList

A_NotSort = collections.deque([])
A_Sort = SortedList([])

Q = int(input())
for _ in range(Q):
  In = list(map(int, input().split()))
  kind = In[0]

  if kind == 1:
    x = In[1]
    A_NotSort.append(x)
  elif kind == 2:
    if len(A_Sort) > 0:
      print(A_Sort.pop(0))
    else:
      print(A_NotSort.popleft())
  elif kind == 3:
    while A_NotSort:
      A_Sort.add(A_NotSort.popleft())