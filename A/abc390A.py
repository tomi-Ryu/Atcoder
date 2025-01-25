A = list(map(int, input().split()))

A_sorted = A[:]
A_sorted.sort()

ans = "No"
for i in range(4):
  tmpArr = A[:]

  tmp = tmpArr[i]
  tmpArr[i] = tmpArr[i+1]
  tmpArr[i+1] = tmp

  if tmpArr == A_sorted:
    ans = "Yes"

print(ans)    