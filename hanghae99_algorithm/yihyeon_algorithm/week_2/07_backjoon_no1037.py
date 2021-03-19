# 백준 1037번 (약수)

# 이 문제를 풀기 전에 주어진 양수의 약수를 구하는 걸 풀어보자.

n = int(input())
list = []
for i in range(1, n+1):
    if n % i == 0:
        if i != 1 and i != n:       # 1과 자신을 제외한 약수 구하기
            print(i)
            list.append(i)

print(list)

