N = int(input())
dictArr = [None] * (N+1)
KArr = [None] * (N+1)
A_Arr = [None] * (N+1)

for i in range(1,N+1):
  K_A = list(map(int, input().split()))

  KArr[i] = K_A[0]
  # 配列(の参照?)が格納されるはず
  A_Arr[i] = K_A[1:]

  tmpdict = {}
  for e in K_A[1:]: 
    if e not in tmpdict:
      tmpdict[e] = 1
    else:
      tmpdict[e] += 1
  dictArr[i] = tmpdict


ans = 0
for i in range(1,N+1):
  for j in range(i+1,N+1):
    pattern = 0
    for Num_i in A_Arr[i]:
      if Num_i in dictArr[j]:
        pattern += dictArr[j][Num_i]
    
    ans = max(ans, pattern / (KArr[i]*KArr[j]))

print(ans)