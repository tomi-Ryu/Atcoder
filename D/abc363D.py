N = int(input())

if N <= 19:
  AnsArr = [None]
  for i in range(10):
    AnsArr.append(i)
  for i in range(1, 10):
    AnsArr.append(10 * i + i)
  
  print(AnsArr[N])
else:
  Rest = N - 19
  digits = 3
  cnt = 0
  AllKinds_Perdigits = 90
  while Rest > AllKinds_Perdigits:
    Rest -= AllKinds_Perdigits
    digits += 1
    if cnt == 1:
      AllKinds_Perdigits *= 10
      cnt = 0
    else:
      cnt = 1
  
  AnsArr = [None] * digits
  No = Rest - 1
  InputCnt = digits // 2 + digits % 2
  for i in range(InputCnt):
    if i == 0:
      d = (No // 10**(InputCnt - 1)) + 1
      AnsArr[0] = AnsArr[-1] = str(d)
      No -= (d - 1) * 10**(InputCnt - 1)
    else:
      d = No // 10**(InputCnt - i - 1)
      AnsArr[i] = AnsArr[-1 - i] = str(d)
      No -= d * 10**(InputCnt - i - 1)
  
  print("".join(AnsArr))