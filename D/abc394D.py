S = input()


stack = []
idx = -1
for s in S:
  stack.append(s)
  idx += 1

  #print(stack, idx, "".join(stack[idx-1:idx+1]))

  if idx >= 1:
    if "".join(stack[idx-1:idx+1]) == "[]" or "".join(stack[idx-1:idx+1]) == "()" or "".join(stack[idx-1:idx+1]) == "<>":
      stack.pop()
      stack.pop()
      idx -= 2

if len(stack) == 0:
  print("Yes")
else:
  print("No")

