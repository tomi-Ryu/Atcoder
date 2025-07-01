N = int(input())
A = list(map(int, input().split()))
X = int(input())

sumA = sum(A)
q = X // sumA
cnt = N * q
ruiseki = sumA*q
ans = None

for a in A:
  ruiseki += a
  cnt += 1

  if ruiseki > X:
    ans = cnt
    break

print(ans)

