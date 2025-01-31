from sortedcontainers import SortedList


L, Q = map(int, input().split())
wood_SortedList = SortedList([(0,L)])

for _ in range(Q):
  c,x = map(int, input().split())

  if c == 1:
    idx = wood_SortedList.bisect_right((x,-1)) - 1
    st,ed = wood_SortedList.pop(idx)
    wood_SortedList.add((st,x))
    wood_SortedList.add((x,ed))
  else:
    idx = wood_SortedList.bisect_right((x,-1)) - 1
    st,ed = wood_SortedList[idx]
    print(ed-st)
