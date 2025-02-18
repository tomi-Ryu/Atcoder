N = int(input())
S = input()

S_digitRuiseki = [0]
for s in S:
  S_digitRuiseki.append(S_digitRuiseki[-1] + int(s))

RuisekiOfRuiseki = [0]
for r in S_digitRuiseki[1:]:
  RuisekiOfRuiseki.append(RuisekiOfRuiseki[-1] + r)

# 文字を格納
ans_ToNdigits_ReverseList = []
rest = 0
for digit in range(1,N+1):
  digitSum = (N+1 -digit) * S_digitRuiseki[-digit] - RuisekiOfRuiseki[-digit-1]
  ans_ToNdigits_ReverseList.append(str((rest + digitSum) % 10))
  rest = (rest + digitSum) // 10

if rest == 0:
  print("".join(ans_ToNdigits_ReverseList[::-1]))
else:
  print(str(rest) + "".join(ans_ToNdigits_ReverseList[::-1]))