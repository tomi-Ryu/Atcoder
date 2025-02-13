N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

Q_P = [None] * (N+1)
P_Q = [None] * (N+1)

for i in range(1, N+1):
  Q_P[Q[i-1]] = P[i-1]
  P_Q[i] = Q[i-1]

Ans = []
for i in range(1,N+1):
  Ans.append(P_Q[Q_P[i]])

print(*Ans)