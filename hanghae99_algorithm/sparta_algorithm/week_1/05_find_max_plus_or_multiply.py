# 내 코드
# 못풀었다.

# input = [0, 3, 5, 6, 1, 2, 4]
#
# def find_max_plus_or_multiply(array):
#     # 왼쪽에서 오른쪽 순으로 '+' or '*'을 넣어 최대값 만들기
#     sum = 0
#     for i in range(len(array)):  # i     =  0,1,2,3,4,5,6 (index)
#                                  # array = [0,3,5,6,1,2,4] (number)
#         if array[i] == 0 or array[i] == 1:  # i = 0, 4
#             sum = sum + array[i + 1]    # sum = 0 + 3/
#         elif array[i] == array[-1]:     # 이걸 모르겠네. 마지막일 때...인덱스 오류 안나게 하려면...
#             sum = sum * array[i]
#         else:
#             sum = sum * array[i + 1]    # sum = 3 * 5/
#
#         return sum
#
# result = find_max_plus_or_multiply(input)
# print(result)


# 튜터님 코드
# 페이스북 기출 문제라고 한다.

input = [0, 3, 5, 6, 1, 2, 4]

def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number

    return multiply_sum

result = find_max_plus_or_multiply(input)
print(result)