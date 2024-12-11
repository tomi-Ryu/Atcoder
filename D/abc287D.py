S = input()
T = input()
len_T = len(T)
head_matchBit_Arr = []
tail_matchBit_Arr = []

matchFlg = True
for i in range(len_T):
  if matchFlg == True and (S[i] == "?" or T[i] == "?" or S[i] == T[i]):
    head_matchBit_Arr.append(True)
  else:
    head_matchBit_Arr.append(False)
    matchFlg = False

matchFlg = True
for i in range(len_T):
  if matchFlg == True and (S[-i - 1] == "?" or T[-i - 1] == "?" or S[-i - 1] == T[-i - 1]):
    tail_matchBit_Arr.append(True)
  else:
    tail_matchBit_Arr.append(False)
    matchFlg = False

for i in range(len_T + 1):
  if i == 0:
    if tail_matchBit_Arr[-1] == True:
      print("Yes")
    else:
      print("No")
  elif i == len_T:
    if head_matchBit_Arr[-1] == True:
      print("Yes")
    else:
      print("No")
  else:
    if head_matchBit_Arr[i - 1] == True and tail_matchBit_Arr[-i - 1] == True:
      print("Yes")
    else:
      print("No")