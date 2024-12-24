a, b, C = map(int, input().split())

popcnt_C = 0
for i in range(60):
  if C >> (59 - i) & 1 == 1:
    popcnt_C += 1

ExistFlg = 0
X = 0
Y = 0
for x_bitcnt in range(popcnt_C + 1):
  y_bitcnt = popcnt_C - x_bitcnt
  if 0 <= a + b - popcnt_C <= 120 - 2 * popcnt_C and (a - x_bitcnt) == (b - y_bitcnt):
    ExistFlg = 1
    for i in range(60):
      if C >> (59 - i) & 1 == 1:
        if x_bitcnt > 0:
          X += 2 ** (59 - i)
          x_bitcnt -= 1
        elif y_bitcnt > 0:
          Y += 2 ** (59 - i)
          y_bitcnt -= 1

    Rest = a + b - popcnt_C
    for i in range(60):
      if Rest > 0 and C >> (59 - i) & 1 == 0:
        Y += 2 ** (59 - i)
        X += 2 ** (59 - i)
        Rest -= 2
      
if ExistFlg == 1:
  print(X, end=" ")
  print(Y)
else:
  print(-1)

  
#print(bin(X)[2:], bin(Y)[2:])
  



