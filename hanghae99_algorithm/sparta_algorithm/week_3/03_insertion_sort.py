input = [4, 6, 2, 9, 1]
# 1단계.
# [4, 6, 2, 9, 1]
#    |<- 그대로
# 2단계.
# [4, 6, 2, 9, 1]
#       |<-
# [4, 2, 6, 9, 1]
#    <-
# [2, 4, 6, 9, 1]
#   <- <-(결론)
# 3단계.
# [2, 4, 6, 9, 1]
#   <- <- |<-
# 4단계.
# [2, 4, 6, 9, 1]
#             |<-
# [2, 4, 6, 1, 9]
# [2, 4, 1, 6, 9]
# [2, 1, 4, 6, 9]
# [1, 2, 4, 6, 9]
#   <- <- <- |<-
#>> count는 5-1
# for i in range(1, 5):       # i = 1, 2, 3, 4
#     for j in range(i):    # j = 0 / 0,1 / 0,1,2 / 0,1,2,3
#         print(i - j)

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):  # i = 1, 2, 3, 4
        for j in range(i):  # j = 0 / 0,1 / 0,1,2 / 0,1,2,3
            if array[i - j - 1] > array[i - j]:  # array[0] > array[1]
                array[i - j - 1], array[i - j] = array[i - j], array[i - j - 1]
            else:   #바로 앞에 있는 애보다 작지 않으면, 굳이 그 앞에 것들과 비교할 필요가 없다.
                break
            # print(i - j)
    return

insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!