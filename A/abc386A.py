kinds = list(map(int, input().split()))

syurui = set()
obj = {}
for i in range(4):
  syurui.add(kinds[i])
  if kinds[i] not in obj:
    obj[kinds[i]] = 0
  
  obj[kinds[i]] += 1

ans = "Yes"
syurui_Arr = []
for e in syurui:
  syurui_Arr.append(e)

if len(syurui) == 2:
  if (obj[syurui_Arr[0]] == 1 and obj[syurui_Arr[1]] == 3) or (obj[syurui_Arr[0]] == 3 and obj[syurui_Arr[1]] == 1) or (obj[syurui_Arr[0]] == 2 and obj[syurui_Arr[1]] == 2):
    pass
else:
  ans = "No"

print(ans)