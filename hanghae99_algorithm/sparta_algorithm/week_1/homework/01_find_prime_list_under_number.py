# 1주차 숙제1.
# input 값으로 들어온 정수 이하의 소수 전부 출력하기.
# 소수란? 자기를 나눴을 때 1과 자기자신밖에 없는 것. 2, 3, 5, 7, 11,

# 미쳐버리겠네... 합성수를 구해서, 정수 리스트에서 빼주기만 하면 되는데 그걸 못하겠다.

# input = 20
# num_list = []
# baesu_list = []
# prime = []
#
# def find_prime_list_under_number(number):   # number = 20
#     # 배수 구하기
#     for num in range(2, number+1):        # num = 2,3,4,5,6,7,8,9,10
#         num_list.append(num)              # num_list = [2,3,4,5,6,7,8,9,10]
#         for j in range(2, number+1):      # j = 2,3,4,5,6,7,8,9,10
#             baesu = num * j               # baesu = 4
#             if baesu <= number:
#                 if baesu in num_list:
#                     # print(baesu)
#                     prime = num_list.remove(baesu)  # num_list = [2,3,4(x),5,6(x),7,8(x),9,10(x)]
#                     # num_list.remove(baesu)
#                     # baesu_list.append(baesu)
#
#     return prime
#
#
# result = find_prime_list_under_number(input)
# print(result)


# 튜터님 코드

input = 20

# 소수는 자기 자신과 1외에는 아무것도 나눌 수 없다.
# 주어진 자연수 N이 소수이기 위한 필요 충분 조건은
# N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
# 수가 수를 나누면 몫이 발생하는데, 몫과 나누는 수 둘 중 하나는 반드시 N 제곱근 이하
# def find_prime_list_under_number(number):
#     prime_list = []
#     for n in range(2, number + 1):  # n = 2 ~ 20
#         # print("n: ", n)
#         for i in range(2, n):       # i = 2, n = 2,3    / n자기 자신을 자기 보다 더 작은 수들로 나누겠다.
#             print("프린트가 나오면 n이 2인데, 포문 안에 들어온 것.")
#             if n % i == 0:
#                 # print("i: ", i)
#                 # print("n%i: ", n%i)
#                 break
#         else:
#             prime_list.append(n)
#
#     return prime_list
#
# result = find_prime_list_under_number(input)
# print(result)

# 헤맸던 부분: 41번째 줄  for i in range(2, n):
# 조건이 n이 2라면? for i in range(2, 2): 가 되니까 n=2일 때는 for문 안에 아예 들어가지도 못한다!!!


# 튜터님 코드2
input = 20

def find_prime_list_under_number(number):
    prime_list = []
    for n in range(2, number + 1):  # n = 2 ~ 20 # print("n: ", n)
        for i in prime_list:       # i = 2, n = 2,3    / n자기 자신을 자기 보다 더 작은 수들로 나누겠다.
            if n % i == 0 and i * i <= n:
                break
        else:
            prime_list.append(n)

    return prime_list

result = find_prime_list_under_number(input)
print(result)

# ...무슨 말인지 모르겠다... 이해가 안간다.