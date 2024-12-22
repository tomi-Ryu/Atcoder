H, W, X, Y = map(int, input().split())
S = []
# (0, 0)が最小
for _ in range(H):
  S.append(input())
T = input()

x, y = (X - 1, Y - 1)
Seen = set()
for t in T:
  if t == "U" and S[x - 1][y] != "#":
    x -= 1
  elif t == "D" and  S[x + 1][y] != "#":
    x += 1
  elif t == "L" and  S[x][y - 1] != "#":
    y -= 1
  elif t == "R" and  S[x][y + 1] != "#":
    y += 1
  
  if S[x][y] == "@":
    Seen.add((x, y))

print(x + 1, end= " ")
print(y + 1, end= " ")
print(len(Seen))