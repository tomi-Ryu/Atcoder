import bisect


N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
  ans += bisect.bisect_right(A, A[i]//2)
print(ans)