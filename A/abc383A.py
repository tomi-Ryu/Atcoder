N = int(input())

prevT = 0
Vol = 0

for _ in range(N):
  T, V = map(int, input().split())

  Vol = max(Vol - (T - prevT), 0)

  Vol += V

  prevT = T

print(Vol)