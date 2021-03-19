# 다음과 같이 영어로 되어 있는 문자열이 있을 때, 이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오.
# 만약, 그런 문자가 없다면 _를 반환하시오.

# 내 코드
# 못 풀었다. 어떻게 짜야 하는지도 모르겠다.

# input = "abacabade"
#
# str_list = []
# check_list = []
# # 같은 문자가 들어오면 1, 처음이면 0을 표시해서 0으로 된 문자를 출력한 다음, 0번째 문자열을 출력하고 싶은데
# # 인덱스를 어떻게 이용해서 맞는 자리에 넣을지 모르겠다.
# def find_not_repeating_character(string):
#     for str in string:
#         str_list.append(str)
#         if str_list ==
#     return "_"
#
#
# result = find_not_repeating_character(input)
# print(result)


# 튜터님 코드

input = "abxacabade"

def find_not_repeating_character(string):
    alphabet_occurrence_array = [0] * 26
    # [4,2,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]
    # "abxacabade"
    for char in string:
        if not char.isalpha():  # True가 아니면 실행해라 == False면 실행해라.(문자열이 아닐 때)
            continue

        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    not_repeating_character_array = []

    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]
        # 왜 0이 아니라 1일 때가 조건인가 이해가 안갔는데, 0이면 아예 문자열에 포함도 되지 않았고, 반복 된 적이 없으니까 한번 카운팅 되고 갯수가 올라가지 않은 것.
        if alphabet_occurrence == 1:
            not_repeating_character_array.append(chr(index + ord("a")))
            # 3번째에 있는 문자열 c를 넣어야 하는데, c는 숫자로 했을 때 97 + c의 인덱스(2)니까 99를 chr로 변환하면 문자열 c가 나온다.

    print(not_repeating_character_array)
    # arr_index 자체를 알파벳순으로 배치 시켰기 때문에, 알파벳 순으로 리스트에 넣어진다.
    # input으로 들어온 문자열 순에서 첫번째 문자열을 뽑으려면 어떻게 해야할까???

    # "abxacabade"
    for char in string:
        # char가 반복되지 않은 알파벳 리스트 = ['c', 'd', 'e', 'x'] 에 있다면? 바로 반환.
        # "abxacabade" 알파벳이 줄 서서 기다리면서 자기 차례 때 조건에 해당하면 바로 리턴 된다. 없으면 '_'반환.
        if char in not_repeating_character_array:
            return char
    return "_"

result = find_not_repeating_character(input)
print(result)


