from sortedcontainers import SortedList


N, D = map(int, input().split())

R_L_SortedList = SortedList([])

"""
R_L_SortedList.add((1,5))
R_L_SortedList.add((1,3))
print(R_L_SortedList) # SortedList([(1, 3), (1, 5)])
"""

for _ in range(N):
  l, r = map(int, input().split())

  R_L_SortedList.add((r,l))

ans = 0
x = -10 ** 15
while R_L_SortedList:
  r,l = R_L_SortedList.pop(0)

  if x + D - 1 < l:
    x = r
    ans += 1

print(ans)


  