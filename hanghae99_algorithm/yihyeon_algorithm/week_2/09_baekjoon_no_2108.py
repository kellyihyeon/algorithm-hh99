# 백준 2108번 (통계학)

from collections import Counter
import sys

n = int(sys.stdin.readline())
nums_list = list()     # [1, 3, 8, -2, 2]
for _ in range(n):
    test_num = int(sys.stdin.readline())
    nums_list.append(test_num)
# print(nums_list)

# 1. arithmetic mean
arithmetic_mean = sum(nums_list) / n
print(round(arithmetic_mean))

# 2. mid value
nums_list.sort()
index_mid = (n // 2)        # 인덱스는 0부터니까 +1 안해도 될듯..?
print(nums_list[index_mid])

# 3. 최빈값
# [1, 3, 8, -2, 2]
if n == 1:
    print(nums_list[0])
else:
    common = Counter(nums_list).most_common()   # most_common(): 빈도가 높은 순으로 전체를 리턴
    # [(-2, 1), (1, 1), (2, 1), (3, 1), (8, 1)]
    if common[0][1] == common[1][1]:            # 최빈값이 여러 개 있을 때, 최빈값 중 두 번째로 작은 값을 출력
        print(common[1][0])
    else:
        print(common[0][0])

# 4. range
range_value = nums_list[-1] - nums_list[0]
print(range_value)

# input()으로 받고 채점 하니까, 엄청 오래 걸리더니 시간초과 됐는데,
# readline()으로 바꾸니까 채점이 바로바로 된다.