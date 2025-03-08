stack = [0] * 100

Q = int(input())

for _ in range(Q):
  In = list(map(int, input().split()))
  kind = In[0]

  if kind == 1:
    stack.append(In[1])
  else:
    print(stack.pop())