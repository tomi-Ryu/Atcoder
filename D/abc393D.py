import math


N = int(input())
S = input()

one_idx_list = []
one_cnt = 0
for i in range(N):
  if S[i] == "1":
    one_idx_list.append(i)
    one_cnt += 1

chuo_idx = one_idx_list[math.ceil(one_cnt / 2) - 1]

if one_cnt % 2 == 0:
  start_Idx = chuo_idx - (one_cnt - 1) // 2
else:
  start_Idx = chuo_idx - one_cnt // 2 


ans = 0
for i in range(len(one_idx_list)):
  ans += abs(one_idx_list[i] - (start_Idx + i))
print(ans)
