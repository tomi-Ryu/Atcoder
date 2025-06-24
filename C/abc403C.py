N,M,Q = map(int, input().split())

viewingPermissionList = []
for _ in range(N+1):
  viewingPermissionList.append(set())

for _ in range(Q):
  kindAndXY = list(map(int, input().split()))
  kind = kindAndXY[0]

  if kind == 1:
    X,Y = kindAndXY[1:]
    viewingPermissionList[X].add(Y)
  elif kind == 2:
    X = kindAndXY[1]
    viewingPermissionList[X].add("all")
  else:
    X,Y = kindAndXY[1:]

    if (Y in viewingPermissionList[X]) or ("all" in viewingPermissionList[X]):
      print("Yes")
    else:
      print("No")
  