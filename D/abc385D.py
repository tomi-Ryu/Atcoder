from sortedcontainers import SortedList

"""
N: 家の件数 / 1~2*10**5
M: 行動数 / 1~2*10**5
"""


N, M, Sx, Sy = map(int, input().split())
x_obj = {}
y_obj = {}

for _ in range(N):
  x, y = map(int, input().split())
  if x not in x_obj:
    x_obj[x] = SortedList([y])
  else:
    x_obj[x].add(y)
  
  if y not in y_obj:
    y_obj[y] = SortedList([x])
  else:
    y_obj[y].add(x)

curX, curY = Sx, Sy
Seen = set()
for _ in range(M):
  D, C_Str  = input().split()
  C_int = int(C_Str)

  if D == "U":
    if curX in x_obj:
      left = x_obj[curX].bisect_right(curY - 1)
      right = x_obj[curX].bisect_right(curY + C_int) - 1

      for _ in range(left, right + 1):
        Seen.add((curX, x_obj[curX].pop(left)))
    curY += C_int
  elif D == "D":
    if curX in x_obj:
      left = x_obj[curX].bisect_right(curY - C_int - 1)
      right = x_obj[curX].bisect_right(curY) - 1

      for _ in range(left, right + 1):
        Seen.add((curX, x_obj[curX].pop(left)))
    curY -= C_int
  elif D == "L":
    if curY in y_obj:
      left = y_obj[curY].bisect_right(curX - C_int - 1)
      right = y_obj[curY].bisect_right(curX) - 1

      for _ in range(left, right + 1):  
        Seen.add((y_obj[curY].pop(left), curY))
    curX -= C_int
  elif D == "R":
    if curY in y_obj:
      left = y_obj[curY].bisect_right(curX - 1)
      right = y_obj[curY].bisect_right(curX + C_int) - 1

      for _ in range(left, right + 1):
        Seen.add((y_obj[curY].pop(left), curY))
    curX += C_int

print(curX, end=" ")
print(curY, end=" ")
print(len(Seen))

    
    

