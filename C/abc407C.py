S = input()
S_perDigit_list = []
for s in S:
  S_perDigit_list.append(int(s))

cnt_Mod10 = 0
S_len = len(S_perDigit_list)
delete_Digit_Len = 0
ans = 0
while S_len > delete_Digit_Len:
  tmp = (S_perDigit_list[-1] - cnt_Mod10) % 10
  ans += tmp
  cnt_Mod10 = (cnt_Mod10 + tmp) % 10

  S_perDigit_list.pop()
  ans += 1
  delete_Digit_Len += 1

print(ans)