def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():  #띄어쓰기 != alphabet, 즉 공백일 때
            continue
        arr_index = ord(char) - ord('a')    # h= 104. 104 - 97 = 7. h의 인덱스값은 7.
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array

print(find_alphabet_occurrence_array("hello my name is sparta"))

sentence = "hello my name is sparta"
print("문장의 길이는: " ,len(sentence))

print("여섯 번째 글자는 : " ,sentence[5])
print("여섯 번째 글자는 알파벳인가요? ", sentence[5].isalpha())

#

input = "hello my name is sparta"

def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    for char in string:
        if not char.isalpha():  #띄어쓰기 != alphabet, 즉 공백일 때
            continue
        arr_index = ord(char) - ord('a')    # h= 104. 104 - 97 = 7. h의 인덱스값은 7.
        alphabet_occurrence_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)): #26
       alphabet_occurrence = alphabet_occurrence_array[index]
       if alphabet_occurrence > max_occurrence:
           max_occurrence = alphabet_occurrence
           max_alphabet_index = index   #4

    return chr(max_alphabet_index + ord('a'))

result = find_max_occurred_alphabet(input)
print(result)






