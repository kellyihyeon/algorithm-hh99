input = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    for num in array:       # num = 3/ 5/ 6
        for compare_num in array:   # compare = 3, 5, 6
            if num < compare_num:
                break
        else:
            return num


result = find_max_num(input)
print(result)
