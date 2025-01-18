import math


X = int(input())

for i in range(30):
  if math.factorial(i) == X:
    print(i)
    break