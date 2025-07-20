N,T = map(int, input().split())
A = list(map(int, input().split()))

ruisekiList = [0]
for a in A:
  ruisekiList.append(ruisekiList[-1] + a)

T %= ruisekiList[-1]
for i in range(1, N+1):
  if T < ruisekiList[i]:
    print(i, end=" ")
    print(T - ruisekiList[i-1])
    break