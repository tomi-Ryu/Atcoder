N = int(input())
X_Y = []
for _ in range(N):
  X_Y.append(list(map(int, input().split())))
S = input()

Y_X_S = []
for i in range(N):
  x,y = X_Y[i]
  s = S[i]

  Y_X_S.append((y,x,s))
Y_X_S.sort()

prevY = None
curY = None
ans = "No"
for y,x,d in Y_X_S:
  curY = y

  if prevY is None or prevY != curY:
    direction_L_Flg = False
    direction_R_Flg = False

    if d == "R":
      direction_R_Flg = True
  else:
    if direction_R_Flg == False and direction_L_Flg == False and d == "R":
      direction_R_Flg = True
    elif direction_R_Flg == True and direction_L_Flg == False and d == "L":
      direction_L_Flg = True
      ans = "Yes"
      break

  prevY = y

print(ans)