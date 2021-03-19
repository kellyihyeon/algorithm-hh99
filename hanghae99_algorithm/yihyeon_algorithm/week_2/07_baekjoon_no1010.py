# 백준 1010번 (다리 놓기)

from math import factorial

num = int(input())

for _ in range(num):
    west, east = map(int, input().split())

    answer = factorial(east) // (factorial(west) * factorial(east - west))
    print(answer)

# n과 k를 마음대로 바꿀 수 있는 건지? 왜?
# n개의 원소를 가지는 집합에서 k개의 부분집합을 고르는 조합의 경우의 수를 이항계수라 한다.
# .............that's why...