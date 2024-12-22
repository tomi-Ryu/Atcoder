N = int(input())
H = list(map(int, input().split()))

ans = 1

# 最初からシュミレート・・・
# 具体例なしのシュミレート・・・ OK

# グループ数
for k in range(1, N + 1):
  # グループ内の初めの要素
  for firstIdx in range(k):
    cnt = 0
    kazu = 1
    # N - 1 = len(H) - 1
    while firstIdx + k * cnt <= N - 1:
      if cnt > 0:
        if prevH == H[firstIdx + k * cnt]:
          kazu += 1
        else:
          kazu = 1
      
      prevH = H[firstIdx + k * cnt]
      cnt += 1
    
      if kazu > ans:
        ans = kazu

print(ans)
    