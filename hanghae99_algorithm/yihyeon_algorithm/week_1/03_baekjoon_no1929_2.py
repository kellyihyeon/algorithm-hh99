# 백준 1929번(소수 구하기)

# 에라토스테네스의 체 없이 구현

n = int(input())            # n = 13이라고 쳤다면?

for i in range(n+1):        # i = 0 ~ 13
    result = True
    if i < 2:               # 1은 소수가 될 수 없으니 제외
        result = False
    for j in range(2, i):   # i = 5,  j = 2, 3, 4
        if i % j == 0:
            result = False
    if result:
        print(i, " ")


# 에라토스테네스의 체로 구현
n = 10      # n 이 10이니까, 리스트 갯수는 11개 있어야 돼. 0부터 들어가니까.
list = [False, False] + [True]*(n-1)        # n-1개로 한 게 list 인덱스 때문. 0부터 시작하니까.
primes = []

for i in range(2, n+1):     # i = 2,3,4,5,6,7,8,9,10
    if list[i]:             # True == 배수에 안걸리고 살아남았다.
        primes.append(i)    # primes = [2, 3, ]
        for j in range(2*i, n+1, i):    # 4 ~ 10까지, +2증가 ==> 배수에 걸리면 F로 바꾸기
            list[j] = False             # list = [F, F, 2, T, F, T, F, T, F, F, F]

print(primes)

