R = int(input())

# iの範囲を0までにできる?
ans = 0
for i in range(-R, R + 1):
  left = -1
  right = 10 ** 6 + 1
  while left + 2 <= right:
    mid = (left + right) // 2

    flg = True
    for i_len in [(i + 0.5)**2, (i-0.5)**2]:
      for j_len in [(mid+0.5)**2, (mid-0.5)**2]:
        if (i_len + j_len) > R**2:
          flg = False
          break
  
    
    if flg == True:
      left = mid
    else:
      right = mid
  
  ans+= max(0, 2 * left + 1)

print(ans)  
    