input = [4, 6, 2, 9, 1]
# 1. [4 6 2 9 1]
#     - - - - -
# 2. [1 6 2 9 4]
#       - - - -
# 3. [1 2 6 9 4]
#         - - -
# 4. [1 2 4 9 6]
#           - -
# 5. [1 2 4 6 9 ]

# for i in range(5 - 1):      #i= 0, 1, 2, 3
#     for j in range(5 - i):  #j= 0, 1, 2, 3, 4
#         print(i + j)

def selection_sort(array):      # 제시: [4, 6, 2, 9, 1]
    n = len(array)

    for i in range(n - 1):
        min_index = i                           #min_index = 0
        for j in range(n - i):
            if array[i + j] < array[min_index]: #array[1] < array[0]
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i] #[1, 6, 2, 9, 4]

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!