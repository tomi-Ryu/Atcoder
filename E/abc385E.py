from sortedcontainers import SortedList

N = int(input())
obj = {}
for _ in range(1, N):
  u, v = map(int, input().split())

  if u not in obj:
    obj[u] = SortedList([])
  if v not in obj:
    obj[v] = SortedList([])

  obj[u].add(v)
  obj[v].add(u)

"""
葉の数(y)>0 かつ x > 0

"""

yuki_node_MaxCnt = 0
# n: 手順2のノード
for n in range(1, N + 1):
  yuki_Cnt = 1
  rinsetu_dg_Arr = []

  for rinsetu_idx in range(len(obj[n])):
    rinsetu_dg_Arr.append(len(obj[obj[n][rinsetu_idx]]))
  rinsetu_dg_Arr.sort(reverse=True)

  x_y_sum = 0
  for i in range(len(obj[n])):
    if rinsetu_dg_Arr[i] == 1:
      # 葉がない(y = 0)
      break
    if rinsetu_dg_Arr[i] * (i + 1) > x_y_sum:
      x_y_sum = rinsetu_dg_Arr[i] * (i + 1)
  
  # 全く葉がない場合も足してMaxCnt更新判定するが、N>=3である以上問題ない。
  yuki_Cnt += x_y_sum

  if yuki_Cnt > yuki_node_MaxCnt:
    yuki_node_MaxCnt = yuki_Cnt

print(N - yuki_node_MaxCnt)
