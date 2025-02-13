N,M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

Ans = []
C = 0
for i in range(1, N+1):
  if i not in A:
    Ans.append(i)
    C += 1

print(C)
print(*Ans)

