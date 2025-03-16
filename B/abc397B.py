S = input()

ansList = []
for s in S:
  ansList.append(s)


while True:
  ok = 1
  i_flg = 1
  for idx in range(len(ansList)):
    if i_flg == 1 and ansList[idx] == "i":
      i_flg = 0
    elif i_flg == 0 and ansList[idx] == "o":
      i_flg = 1
    elif i_flg == 1 and ansList[idx] == "o":
      ansList.insert(idx, "i")
      ok = 0
      break
    elif i_flg == 0 and ansList[idx] == "i":
      ansList.insert(idx, "o")
      ok = 0
      break
  
  if ok == 1:
    if len(ansList) % 2 == 0:
      print(len(ansList) - len(S))
    else:
      print(len(ansList) - len(S) + 1)
    break
  

      