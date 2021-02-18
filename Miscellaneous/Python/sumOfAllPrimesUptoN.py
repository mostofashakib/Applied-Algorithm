"""
Problem statement: Return the sum of all prime numbers upto N

Written by: Mostofa Adib Shakib
Language: Python
"""

def sumOfAllPrimesUptoN(n):
  if n <= 1:
    return 0

  primes = [True] * n
  primes[0] = False
  primes[1] = False
  p = 2

  while p*p <= n:
    if primes[p]:
      for i in range(p*2, n, p):
        primes[i] = False

    p += 1

  count = 0

  for i in range(2, n):
    if primes[i]:
      count += i

  return count

print(sumOfAllPrimesUptoN(15))