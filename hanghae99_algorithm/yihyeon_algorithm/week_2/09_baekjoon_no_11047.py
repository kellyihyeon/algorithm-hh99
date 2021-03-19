# 백준 11047번 (동전 0)

kind, won = map(int, input().split())
cash_list = []
count = 0

for i in range(kind):
    worth = int(input())
    cash_list.append(worth)
    # [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]

for i in reversed(range(kind)): # 9 8 7 6 5 4 3 2 1 0
    count = count + (won // cash_list[i])
    won = won % cash_list[i]

print(count)

# mistake 1:
# won = won % cash_list[i] 이걸 그냥 won에 다시 넣으면 되는데,
# rest라는 변수를 만들어서 또 저장을 하려고 하니 13번째 줄도 재활용 할 수가 없고, 코드는 늘어나고...

