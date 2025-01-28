"""
思考: 25min
実装: 20Min
"""
from sortedcontainers import SortedList


H,W,X = map(int, input().split())
P,Q = map(int, input().split())
S = []
# 最左上: (0,0)
for _ in range(H):
  S.append(list(map(int, input().split())))

takahashi_Mass_Set = set()
takahashi_Mass_Set.add((P-1,Q-1))
# element: (強さ, 場所(0-indexed))
candidate_Mass_SList = SortedList([])
for dh,dw in [(1,0),(-1,0),(0,1),(0,-1)]:
  h = P-1+dh
  w = Q-1+dw
  if 0<=h<=H-1 and 0<=w<=W-1:
    candidate_Mass_SList.add((S[h][w],(h,w)))

ans = S[P-1][Q-1]
while candidate_Mass_SList:
  power, pos = candidate_Mass_SList.pop(0)

  if ans > power*X:
    takahashi_Mass_Set.add(pos)
    ans += power

    curh,curw = pos
    for dh,dw in [(1,0),(-1,0),(0,1),(0,-1)]:
      h = curh+dh
      w = curw+dw
      if 0<=h<=H-1 and 0<=w<=W-1:
        if (h,w) not in takahashi_Mass_Set and (S[h][w], (h,w)) not in candidate_Mass_SList:
          candidate_Mass_SList.add((S[h][w], (h,w)))
  else:
    break

print(ans)