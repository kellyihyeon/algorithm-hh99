# 백준 1920번 (수 찾기)

n = int(input())
a_group = list(map(int, input().split()))
a_group.sort()      # 1 2 3 4 5

m = int(input())
b_group = list(map(int, input().split()))

mid = a_group[len(a_group) // 2]    # 0부터니까 인덱스는 2

for i in b_group:       # i = 1 3 7 9 5
    left, right = 0 , n
    while left <= right:
        mid = (left + right) // 2
        if mid < n and mid > -1:
            if a_group[mid] < i:
                left = mid + 1
            else:
                right = mid -1
        else:
            break
    if mid < n and mid > -1:
        if i == a_group[right+1]:
            print(1)
        else:
            print(0)
    else:
        print(0)