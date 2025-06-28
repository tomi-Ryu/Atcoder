N, K = map(int, input().split())
A = list(map(int, input().split()))

displayed_Number = 1
MAX_NUMBER = 10**K - 1
for a in A:
  calclated_Value = displayed_Number * a

  if calclated_Value > MAX_NUMBER:
    displayed_Number = 1
  else:
    displayed_Number = calclated_Value

print(displayed_Number)