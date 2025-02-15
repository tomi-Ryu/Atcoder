S = input()

ans = 0
for kankaku in range(1,51):
  a_idx = 0
  while a_idx + 2*kankaku <= len(S) - 1:
    b_idx = a_idx + kankaku
    c_idx = a_idx + 2*kankaku

    if S[a_idx] == "A" and S[b_idx] == "B" and S[c_idx] == "C":
      ans += 1
    
    a_idx += 1

print(ans)