N = int(input())
A = list(map(int, input().split()))

latest_idx_perNum_obj = {}

ans = 10 ** 10
for i in range(N):
  Num = A[i]

  if Num not in latest_idx_perNum_obj:
    latest_idx_perNum_obj[Num] = i
  else:
    ans = min(ans, i - latest_idx_perNum_obj[Num] + 1)
    latest_idx_perNum_obj[Num] = i

if ans == 10 ** 10:
  ans = -1

print(ans)