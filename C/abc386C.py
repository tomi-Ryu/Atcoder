K = int(input())
S = input()
T = input()

len_S = len(S)
len_T = len(T)
ans = "No"

if len_S + 1 == len_T:
  left = 0
  right = 0
  for i in range(len_S):
    if S[i] == T[i]:
      left += 1
    else:
      break
  for i in range(len_S):
    if S[-1 -i] == T[-1 -i]:
      right += 1
    else:
      break
  if left + right >= len_S:
    ans = "Yes"
elif len_S - 1 == len_T:
  left = 0
  right = 0
  for i in range(len_T):
    if S[i] == T[i]:
      left += 1
    else:
      break
  for i in range(len_T):
    if S[-1 -i] == T[-1 -i]:
      right += 1
    else:
      break
  if left + right >= len_T:
    ans = "Yes"
elif len_S == len_T:
  machigaiCnt = 0
  for i in range(len_S):
    if S[i] != T[i]:
      machigaiCnt += 1
  if machigaiCnt <= 1:
    ans = "Yes"

print(ans)
