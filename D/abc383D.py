def eratosthenes(n):
    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n+1):
        if not(is_prime[p]):
            continue
        for k in range(p*2, n+1, p):
            is_prime[k] = False
    return is_prime

eratosthenesArr = eratosthenes(2*(10**6))
PrimeArr = []
for i in range(2*10**6 + 1):
    if eratosthenesArr[i] == True:
        PrimeArr.append(i)

# 昇順ソートされたままだよね?
p_Arr = PrimeArr[:]
q_Arr = PrimeArr[:]

N = int(input())

kindSet = set()
for p in p_Arr:
    for q in q_Arr:
        if p**2 * q**2 <= N:
            if p != q:
              kindSet.add(p**2 * q**2)
        else:
            break
    
    if p**8 <= N:
        kindSet.add(p**8)

print(len(kindSet))