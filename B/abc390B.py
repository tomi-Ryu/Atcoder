N = int(input())
A = list(map(int, input().split()))

ans = "Yes"
for i in range(1, N-1):
  if A[i]**2 != A[i-1]*A[i+1]:
    ans = "No"

print(ans)