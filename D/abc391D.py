from sortedcontainers import SortedList

N, W = map(int, input().split())
block_ans = [10**10] * (N+1)
col_SArr = []
for _ in range(W+1):
  col_SArr.append(SortedList([]))

for i in range(1,N+1):
  x,y = map(int, input().split())

  col_SArr[x].add((y,i))

time = 0
del_block = set()
pop_ok = True
while pop_ok:
  for w in range(1,W+1):
    if len(col_SArr[w]) == 0:
      pop_ok = False
      break
    else:
      InitDist, BNo = col_SArr[w].pop(0)
      time = max(time, InitDist-1)
      del_block.add(BNo)
  time += 1

  while del_block and pop_ok:
    block_ans[del_block.pop()] = time


#print("???", block_ans)

Q = int(input())
for _ in range(Q):
  t,a = map(int, input().split())

  if block_ans[a] <= t:
    print("No")
  else:
    print("Yes")
  


      
