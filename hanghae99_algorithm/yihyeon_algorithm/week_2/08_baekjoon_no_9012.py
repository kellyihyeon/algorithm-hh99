# 백준 9012번 (괄호)

n = int(input())

for _ in range(n):      # n = 3
    vps = input()
    stack = []

    for parenthesis in vps:
        if parenthesis == "(":
            stack.append(parenthesis)

        else:            #parenthesis == ")":
            if not stack:       # 스택이 비어있는 경우
                print("NO")
                break
            else:
                stack.pop()

    if not stack:       # "("를 다 없애서 stack이 비어 있는 경우 == 짝이 맞다.
        print("YES")
        break
    else:               # stack이 비어있지 않은 경우 : 예 ((
        print("NO")
        break

# error: )) 를 입력하면 NO 와 그 다음 줄에 YES가 한 번 더 찍히는 상황
# 14번째 줄과 20번째 줄이 겹쳐지는 상황.