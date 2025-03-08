N = int(input())
A = list(map(int, input().split()))

ans = "No"
for i in range(0,N-2):
  #print("N",i)

  if A[i] == A[i+1] == A[i+2]:
    ans = "Yes"
    break

print(ans)