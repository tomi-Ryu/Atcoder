N = int(input())
A = map(int, input().split())

prev = -1
ans = "Yes"
for a in A:
  if prev >= a:
    ans = "No"
    break
  else:
    prev = a

print(ans) 