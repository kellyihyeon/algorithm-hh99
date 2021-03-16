# 백준 1149번 (RGB 거리)

n = int(input())        # 3개의 집

cost = []

for _ in range(n):
    cost.append(list(map(int, input().split())))
    # [[26, 40, 83], [49, 60, 57], [13, 89, 99]]
    # [[26, 40, 83], [89, 86, 83], [96, 172, 185]]

for i in range(1, n):   # n= 3 / i = 1, 2
    # red로 골랐을 때 경우의 수
    cost[i][0] = cost[i][0] + min(cost[i - 1][1], cost[i - 1][2])

    # green으로 골랐을 때 경우의 수
    cost[i][1] = cost[i][1] + min(cost[i - 1][0], cost[i - 1][2])

    # blue로 골랐을 때 경우의 수
    cost[i][2] = cost[i][2] + min(cost[i - 1][0], cost[i - 1][1])

print(min(cost[n-1][0], cost[n-1][1], cost[n-1][2]))

# 무슨 말이지
# 헐...! 와 정수 삼각형이랑 똑같은 문제네.
# 정수 삼각형은 쉬웠는데, 같은 문제였네... 바보
# 이 문제에서도 cost라는 전역 변수를 이용해서,
# 그 자리에서 바로바로 값을 바꿔줬는데 개념 이해를 못했네.
# mistake 1: 전역변수, 지역변수 개념을 확실히 모르고 있던 것 확인.