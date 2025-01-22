A = [[None] * 20 for _ in range(20)]

N = int(input())

for i in range(1, 2 * N):
  cnt = 0
  In = list(map(int, input().split()))
  for j in range(i + 1, 2 * N + 1):
    A[i][j] = In[cnt]
    cnt += 1


RestNumArr = [i for i in range(1, 2 * N + 1)]
# element: (i,j) / i<j
PatternArr = [] 
ans = 0
def Select(RestCnt):
  global ans
  #global RestNumArr
  #global PatternArr

  if RestCnt == 0:
    enjoyNum = 0
    for i in range(N):
      enjoyNum ^= A[PatternArr[i][0]][PatternArr[i][1]]
    ans = max(ans, enjoyNum)
    return
  
  minVal = min(RestNumArr)
  RestNumArr.remove(minVal)
  TmpArr = RestNumArr[:]
  for e in TmpArr:
    RestNumArr.remove(e)
    PatternArr.append((minVal, e))
    Select(RestCnt - 1)
    RestNumArr.append(e)
    PatternArr.remove((minVal, e))

  RestNumArr.append(minVal)

Select(N)
print(ans)