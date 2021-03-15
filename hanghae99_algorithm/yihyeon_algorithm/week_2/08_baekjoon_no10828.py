# 백준 10828번 (스택)
import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    order = sys.stdin.readline()

    if "push" in order:
        x = int(order[5: ])
        stack.append(x)
    elif "pop" in order:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif "size" in order:
        print(len(stack))
    elif "empty" in order:
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif "top" in order:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

# input으로 입력 받다가, readline도 한 번 써봄.
