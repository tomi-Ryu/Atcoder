N = int(input())
obj = {}

for _ in range(N):
  S = input()

  if S not in obj:
    print(S)
    obj[S] = 1
  else:
    print(S + "(" + str(obj[S]) + ")")
    obj[S] += 1
  
