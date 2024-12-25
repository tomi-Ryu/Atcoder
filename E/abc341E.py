from sortedcontainers import SortedSet

N, Q = map(int, input().split())
S = input()
# Idxは1から
X = SortedSet([])
for i in range(N - 1):
  if S[i] == S[i + 1]:
    X.add(i + 1)

for _ in range(Q):
  kind, L, R = map(int, input().split())

  if kind == 1:
    if L > 1:
      if L - 1 in X:
        X.discard(L - 1)
      else:
        X.add(L - 1)
    
    if R < N:
      if R in X:
        X.discard(R)
      else:
        X.add(R)
  else:
    bl_L = X.bisect_left(L)
    ans = "Yes"
    if len(X) != bl_L:
      if X[bl_L] < R:
        ans = "No"
    
    print(ans)
      

  