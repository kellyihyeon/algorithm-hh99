# 백준 2164번 (카드2)

from collections import deque

n = int(input())        # n = 6 (6장의 카드)
cards = deque()         # deque 생성

# 카드 만들기
for card in range(1, n+1):      # card = 1,2,3,4,5,6
    cards.append(card)
# print(cards)                    # deque([1, 2, 3, 4, 5, 6])

def deque():
    while len(cards) > 1:
        cards.popleft()
        temp = cards.popleft()
        cards.append(temp)

    # if len(cards_list) == 1:
    #     print(cards_list)
    print(cards.pop())
deque()

# 굳이 함수 안써도 되는데, 한번 써 봄.
# 실수1: cards 찍어서 확인 해보면 리스트로 생성, 굳이 cards를 리스트로 만들지 않아도 된다.
# 실수2: 마지막에 출력할 때 cards만 넣으면 deque([4]) 라고 출력되는데, 카드 번호가 알고 싶은 거니까 pop()해서 숫자를 출력해야 한다.

