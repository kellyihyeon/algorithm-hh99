# 백준 18258번 (큐2)
from collections import deque
import sys

n = int(sys.stdin.readline())

# deque 생성
queue = deque()
# print(queue)

for _ in range(n):
    order = sys.stdin.readline()
    # queue = []

    if "push" in order:
        x = int(order[5: ])
        queue.append(x)
        # print(queue)
    elif "pop" in order:
        if not queue:
            print(-1)
        else:
            x = queue.popleft()
            print(x)
    elif "size" in order:
        print(len(queue))
    elif "empty" in order:
        if not queue:
            print(1)
        else:
            print(0)
    elif "front" in order:
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif "back" in order:
        if not queue:
            print(-1)
        else:
            print(queue[-1])


# mistake 1: 대참사. 'queue = []'를 지역변수로 선언했더니, queue에 쌓이지 않고, 하나만 담긴다.
# mistake 2,3: deque 임포트 하는 법 까먹었고, deque 생성하는 법 까먹어서 찾아봄.
# mistake 4: input으로 하면 시간초과 -> sys 임포트해서 제출 -> 통과