S = input()
S_len = len(S)

ansList = [None] * (S_len)
idx = S_len - 1
while idx >= 0:
  if S[idx] != "A":
    ansList[idx] = S[idx]
    idx -= 1
  else:
    if idx-1 >= 0:
      if S[idx-1] != "W":
        ansList[idx] = S[idx]
        idx -= 1
      else:
        cnt = 1
        while idx-1-cnt >= 0 and S[idx-1-cnt] == "W":
          cnt += 1
        rest = cnt+1
        while rest > 0:
          if rest == cnt+1:
            ansList[idx-rest+1] = "A"
          else:
            ansList[idx-rest+1] = "C"
          rest -= 1
        idx -= cnt+1
    else:
      ansList[idx] = S[idx]
      idx -= 1  
print("".join(ansList))
