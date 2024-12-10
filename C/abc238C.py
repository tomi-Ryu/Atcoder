N_str = input()
N_int = int(N_str)

N_digits = len(N_str)
rest_digits = N_digits
ans = 0

while rest_digits > 0:
  if rest_digits == N_digits:
    kousu = N_int - (10 ** (N_digits - 1) - 1)
  else:
    kousu = 9 * 10**(rest_digits - 1)
  
  FplusL = (1 + kousu)
  if kousu % 2 == 0:
    kousu = kousu // 2
  else:
    FplusL = FplusL // 2
  
  ans += (kousu % 998244353) * (FplusL % 998244353)
  ans = ans % 998244353
  rest_digits -= 1

print(ans)
