# 입력 받은 수의 각 자리 숫자의 합을 계산하는 함수 만들기 (재귀 함수 이용)

def sum_of_digits(num):
    if num >= 1:
        # share = num//10
        return num % 10 + sum_of_digits(num // 10)
    else:
        return False

n = int(input())

print(sum_of_digits(n))