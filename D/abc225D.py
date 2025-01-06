N, Q = map(int, input().split())
obj = {}
for i in range(1, N + 1):
  obj[i] = {"behind":-1,"ahead":-1}

for _ in range(Q):
  In = list(map(int, input().split()))
  kind = In[0]
  if kind <= 2:
    x, y = In[1:]
  else:
    x = In[-1]
  
  if kind == 1:
    obj[x]["behind"] = y
    obj[y]["ahead"] = x
  elif kind == 2:
    obj[x]["behind"] = -1
    obj[y]["ahead"] = -1
  else:
    refNo = x
    while obj[refNo]["ahead"] != -1:
      refNo = obj[refNo]["ahead"]
    sentouNo = refNo

    AnsArr = [1, sentouNo]
    refNo = sentouNo
    while obj[refNo]["behind"] != -1:
      refNo = obj[refNo]["behind"]
      AnsArr.append(refNo)
      AnsArr[0] += 1
    print(*AnsArr)

    

