# 백준 11050번 (이항계수1)

from math import factorial

n, k = map(int, input().split())

answer = factorial(n) // (factorial(k) * factorial(n - k))

print(answer)

