N = int(input())

AnsList = [[None] * N for _ in range(N)]

for i in range(N):
  j = N - 1 - i

  for I in range(i, j+1):
    for J in range(i, j+1):
      if i % 2 == 0:
        AnsList[I][J] = "#"
      else:
        AnsList[I][J] = "."

for i in range(N):
  print("".join(AnsList[i])) 

