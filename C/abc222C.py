N, M = map(int, input().split())
A = []
for i in range(2 * N):
  A.append(input())

rankArr = [[99999, 0]]
for i in range(1, 2 * N + 1):
  rankArr.append([0, -i])

R_2kminus1_WinHnad_Set = set()
R_2kminus1_WinHnad_Set.add(("G", "C"))
R_2kminus1_WinHnad_Set.add(("C", "P"))
R_2kminus1_WinHnad_Set.add(("P", "G"))
for i in range(1, M + 1):
  for k in range(1, N + 1):
    R_2kminus1_hand = A[-rankArr[2 * k - 1][1] - 1][i - 1]
    R_2k_hand = A[-rankArr[2 * k][1] -1][i - 1]

    if R_2kminus1_hand != R_2k_hand:
      if (R_2kminus1_hand, R_2k_hand) in R_2kminus1_WinHnad_Set:
        rankArr[2 * k - 1][0] += 1
      else:
        rankArr[2 * k][0] += 1
  
  rankArr.sort(reverse=True)

for i in range(1, 2 * N + 1):
  print(-rankArr[i][1])