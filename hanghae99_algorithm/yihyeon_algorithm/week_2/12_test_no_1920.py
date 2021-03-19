# 백준 1920번 (수 찾기)

n = int(input())
a_group = list(map(int, input().split()))

m = int(input())
b_group = list(map(int, input().split()))

for i in b_group:
    if i in a_group:
        print(1)
    else:
        print(0)


# 이렇게 하면 당연히 시간초과 나오는데



