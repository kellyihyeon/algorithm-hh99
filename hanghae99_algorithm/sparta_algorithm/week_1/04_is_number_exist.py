# 내 코드

# input = [3, 5, 6, 1, 2, 4]
#
#
# def is_number_exist(number, array):
#     # 숫자 3이 array에 포함 돼있는지 판단하는 알고리즘 짜기
#     target_num = number
#     for compare_num in array:
#         if target_num == compare_num:
#             return True
#     return False
#
# result = is_number_exist(1, input)
# print(result)


# 튜터님 코드

input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):         # 시간 복잡도
    for element in array:                   # array의 길이만큼 아래 연산식이 실행
        if number == element:               # 비교 연산 1번 실행
            return True                     # N * 1 = N만큼

    return False

result = is_number_exist(3, input)
print(result)