N,M = map(int,input().split())
protectedWallCnt = [0] * (N+2)
protectWall_Increment = [0] * (N+2)
protectWall_Decrement = [0] * (N+2)

for _ in range(M):
  L, R = map(int,input().split())
  protectWall_Increment[L] += 1
  protectWall_Decrement[R+1] += 1

for i in range(1, N+1):
  protectedWallCnt[i] = protectedWallCnt[i-1] + protectWall_Increment[i] - protectWall_Decrement[i]

print(min(protectedWallCnt[1:N+1]))