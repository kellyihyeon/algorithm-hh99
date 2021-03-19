# 백준 1149번 (RGB 거리)

n = int(input())

cost = []   # [[26, 40, 83,], [49, 60, 57], [13, 89, 99]]
            #       0               1             2
            #   0   1   2      0    1   2    0    1   2

for _ in range(n):
    cost.append(list(map(int, input().split())))
# print(cost)
# print("cost의 길이는: ", len(cost))

for i in range(n):
    # red로 골랐을 때 경우의 수
    cost[i][0] = cost[i][0] + min(cost[i + 1][1], cost[i + 1][2])
    print(cost[i][0])

    # green으로 골랐을 때 경우의 수
    cost[i][1] = cost[i][1] + min(cost[i + 1][0], cost[i + 1][2])
    print(cost[i][1])
    # blue로 골랐을 때 경우의 수
    cost[i][2] = cost[i][2] + min(cost[i + 1][0], cost[i + 1][1])
    print(cost[i][2])
print(min(cost[n-1][0], cost[n-1][1], cost[n-1][2]))

# 틀린 코드.
# 내용이 이해가 갈듯 하면서 안가네.