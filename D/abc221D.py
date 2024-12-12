from sortedcontainers import SortedList

N = int(input())

transition_Arr = SortedList([])
for _ in range(N):
  A, B = map(int, input().split())
  transition_Arr.add((A, 1))
  transition_Arr.add((A + B, -1))

login_sumday_Human_Arr = []
# idxは0からだが、最初はログインが1人の日の合計
for _ in range(N):
  login_sumday_Human_Arr.append(0)

prev_day, notUse = transition_Arr.pop(0)
login_cnt = 1
while transition_Arr:
  cur_day, trans = transition_Arr.pop(0)

  if login_cnt > 0:
    login_sumday_Human_Arr[login_cnt - 1] += cur_day - prev_day

  login_cnt += trans
  prev_day = cur_day

print(*login_sumday_Human_Arr)


