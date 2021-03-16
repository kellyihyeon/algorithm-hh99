# 백준 11399번 (ATM)

how_many = int(input())

minute = list(map(int, input().split()))

minute.sort()
# [1, 2, 3, 3, 4]

waiting = 0
waiting_sum = []
for i in range(how_many):    # 5명
    waiting = waiting + minute[i]
    waiting_sum.append(waiting)

print(sum(waiting_sum))


# mistake 라기보다 생각 못했던 것:
# 사람 한 명 왔을 때 빼먹었네. -> 아 그냥 진짜 바로 기기 가서 빼라.
# if how_many == 1:
#     print(minute[0])
# else: