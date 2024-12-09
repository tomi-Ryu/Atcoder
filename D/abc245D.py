N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))
Ans_B = []

for c_idx in reversed(range(N, N + M + 1)):
  Tmp_C = C[c_idx]

  for a_idx in reversed(range(N)):
    b_sisu = c_idx - a_idx
    
    if b_sisu > M:
      break
    else:
      Tmp_C -= A[a_idx] * Ans_B[M - b_sisu]
  
  Ans_B.append(Tmp_C // A[N])

Ans_B.reverse()
print(*Ans_B)

    

