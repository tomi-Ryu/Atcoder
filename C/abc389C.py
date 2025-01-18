stack = [0]
headIdx = 0

Q = int(input())
for _ in range(Q):
  In = list(map(int, input().split()))
  kind = In[0]

  if kind == 1:
    stack.append(stack[-1] + In[1])
  elif kind == 2:
    headIdx += 1
  elif kind == 3:
    print(stack[headIdx + In[1] - 1] - stack[headIdx])
