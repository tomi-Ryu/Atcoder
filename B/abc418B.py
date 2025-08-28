S = input()
Len_S = len(S)
maxVal = 0
for sIdx in range(Len_S-1):
  for eIdx in range(sIdx+1,Len_S):
    if S[sIdx] == "t" and S[eIdx] == "t" and eIdx - sIdx >= 2:
      x = 0
      Len_t = eIdx - sIdx + 1
      for s in S[sIdx:eIdx+1]:
        if s == "t":
          x += 1

      maxVal = max(maxVal, (x-2)/(Len_t-2))

print(maxVal)