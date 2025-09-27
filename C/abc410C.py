N, Q = map(int, input().split())

A = []
for i in range(1, N+1):
  A.append(i)
curPointer = 0

for _ in range(Q):
  In = list(map(int, input().split()))
  kind = In[0]

  if kind == 1:
    p,x = In[1:]
    A[(p-1+curPointer)% N] = x
  elif kind == 2:
    p = In[1]
    print(A[(p-1+curPointer)% N])
  else:
    k = In[1]
    curPointer = (curPointer+k) % N
