# 백준 2164번 (카드2)

from collections import deque

# 인풋
n = int(input())        # n = 6
cards = deque()

# 카드 만들기
for card in range(1, n+1):          # card = 1,2,3,4,5,6
    cards.append(card)              # cards = [1,2,3,4,5,6]
# print(cards)

# 주어진 동작을 반복을 해야한다. == 카드가 1장보다 많을 때까지.
while len(cards) > 1:
    cards.popleft()                  # cards = [2,3,4,5,6]
    temp = cards.popleft()           # cards = [3,4,5,6]
    cards.append(temp)              # cards = [3,4,5,6,2]

print(cards.pop())                  # cards = [4]




