# 백준 10815번 (숫자 카드)
n = int(input())
cards = list(map(int, input().split()))
cards.sort()            # cards = [-10, 2, 3, 6, 10]

m = int(input())
test = list(map(int, input().split()))  # test = [10 9 -5 2 3 4 5 -10]

for i in range(m):  # 8번 돌게.  i = 0,1,2,3,4,5,6,7
    left, right = 0, n-1        # n=5, left = 0, right = 4
    while left <= right:
        mid = (left + right) // 2       # mid = 2 / 3 / 4
        if cards[mid] == test[i]:       # 3 == 10     / 10 == 10
            print(1, end=" ")
            break
        elif cards[mid] < test[i]:      # 3 < 10
            left = mid + 1              # left = 3 / 4
        else:
            right = mid - 1             # right = 1

        if left > right:
            print(0, end=" ")
            break
