# 백준 1932번 ( 정수삼각형)

n = int(input())

nums_list = []

for _ in range(n):
    nums_list.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            nums_list[i][j] = nums_list[i][j] + nums_list[i-1][j]
        elif i == j:
            nums_list[i][j] = nums_list[i][j] + nums_list[i-1][j-1]
        else:
            nums_list[i][j] = max(nums_list[i][j]+nums_list[i-1][j],
                               nums_list[i][j]+nums_list[i-1][j-1])

print(max(nums_list[n-1]))

# 하....진짜 3갈래로 나눠서, 전부 숫자 다 넣어보고 규칙 찾아서 품.

