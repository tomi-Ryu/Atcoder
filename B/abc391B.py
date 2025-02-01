N,M = map(int, input().split())
S = []
for _ in range(N):
  S.append(input())
T = []
for _ in range(M):
  T.append(input())


ans = []
for si in range(N):
  for sj in range(N):
    if si+M <= N and sj+M <= N:
      flg = "Yes"
      for i in range(M):
        for j in range(M):
          if S[si+i][sj+j] != T[i][j]:
            flg = "No"
      
      if flg == "Yes":
        ans = [si+1, sj+1]

print(*ans)
        
