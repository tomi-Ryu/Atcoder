N = int(input())

ans = 0
No = 1
while No <= N:
  Val = N // No

  left = 1
  right = N + 1
  while left + 2 <= right:
    mid = (left + right) // 2
    if N // mid >= Val:
      left = mid
    else:
      right = mid
  EndNo = left

  ans += (EndNo - (No - 1)) * Val

  No += (EndNo - (No - 1))

print(ans)


