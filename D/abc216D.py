import collections


N, M = map(int, input().split())
color_to_tutu_List = [[] for _ in range(N+1)]
cnt = [0] * (N+1)
deq = collections.deque([])
tutu_List = [[] for _ in range(M+1)]

for m in range(1,M+1):
  k = int(input())
  tutu = list(map(int, input().split()))

  for e in tutu:
    color_to_tutu_List[e].append(m)
  
  cnt[tutu[-1]] += 1
  if cnt[tutu[-1]] == 2:
    deq.append(tutu[-1])

  tutu_List[m] = tutu

deleteCnt = 0
while deq:
  color = deq.popleft()

  for tutuId in color_to_tutu_List[color]:
    tutu_List[tutuId].pop()
    cnt[color] -= 1
    deleteCnt += 1

    if tutu_List[tutuId] != []:
      nextColor = tutu_List[tutuId][-1]
      cnt[nextColor] += 1
      if cnt[nextColor] == 2:
        deq.append(nextColor)

if deleteCnt == 2*N:
  print("Yes")
else:
  print("No")