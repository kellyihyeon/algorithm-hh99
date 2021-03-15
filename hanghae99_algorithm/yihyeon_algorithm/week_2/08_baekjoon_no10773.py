# 백준 10773번 (제로)

k = int(input())
stack = []

for i in range(k):
    num = int(input())

    if num == 0:
        stack.pop()

    else:
        stack.append(num)

print(sum(stack))

# 변수 sum을 선언해놓고 지우질 않아서 sum 함수 쓰는데 오류가 계속 떴다.