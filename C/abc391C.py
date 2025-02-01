N,Q = map(int, input().split())
p_place = []
for i in range(N+1):
  p_place.append(i)
cnt = [1]*(N+1)
cnt[0] = 0
k2_ans = 0

for _ in range(Q):
  In = list(map(int, input().split()))
  kind = In[0]

  if kind == 1:
    P,H = In[1:]

    cnt[p_place[P]] -= 1
    if cnt[p_place[P]] == 1:
      k2_ans -= 1
    
    p_place[P] = H
    cnt[H] += 1
    if cnt[H] == 2:
      k2_ans += 1   
    """
      print("=====")
      print(p_place)
      print(cnt)
      print("=====")
    """
  else:
    print(k2_ans)
