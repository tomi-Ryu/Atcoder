pointArr = list(map(int, input().split()))

Point_nameArr = []
AllStr = "ABCDE"
for ptnNum in range(1,32):
  name = ""
  point = 0
  for shiftCnt in range(5):
    if ptnNum >> shiftCnt & 1 == 1:
      name += AllStr[shiftCnt]
      point += pointArr[shiftCnt]
  
  Point_nameArr.append((name, point))

Point_nameArr = sorted(Point_nameArr, key=lambda x: x[0])
Point_nameArr = sorted(Point_nameArr, key=lambda x: x[1], reverse=True)

for i in range(31):
  print(Point_nameArr[i][0])
