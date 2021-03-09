# Factorial(N) = N * Factorial(N - 1)
# ....
# Factorial(1) = 1

def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


print(factorial(5))

# 풀이(블로그에 옮기기)
# factorial(5) : 5 * factorial(4)
# factorial(4) : 4 * factorial(3)
# factorial(3) : 3 * factorial(2)
# factorial(2) : 2 * factorial(1)
# factorial(1) : 1  # 탈출 조건 써주기
#>> factorial(5) == 5 * 4 * 3 * 2 * 1


