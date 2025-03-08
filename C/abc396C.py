N,M = map(int,input().split())
B = list(map(int,input().split()))
W = list(map(int,input().split()))
B.sort(reverse=True)
W.sort(reverse=True)

B_ruiseki = [0]
B_max_Num = len(B)
flg = 1
for i in range(len(B)):
  B_ruiseki.append(B_ruiseki[-1]+B[i])

  if B[i] < 0 and flg ==1:
    B_max_Num = i
    flg = 0
B_ruiseki_len = len(B_ruiseki)

W_ruiseki = [0]
for w in W:
  W_ruiseki.append(W_ruiseki[-1]+w)

ans = 0
for w_idx in range(len(W_ruiseki)):
  if w_idx <= B_max_Num:
    ans = max(ans, B_ruiseki[B_max_Num] + W_ruiseki[w_idx])
  else:
    if B_ruiseki_len > w_idx:
      ans = max(ans, B_ruiseki[w_idx] + W_ruiseki[w_idx])
print(ans)

#print(B_max_Num)
