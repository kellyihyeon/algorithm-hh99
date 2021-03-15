# 백준 9012번 (괄호)

n = int(input())

for _ in range(n):      # n = 3
    vps = input()
    stack = []
    check = 0

    for parenthesis in vps:
        if parenthesis == "(":
            stack.append(parenthesis)

        else:  # parenthesis == ")"     # ))
            if not stack:       # 스택이 비어있는 경우
                print("NO")
                check = 1
                break
            else:
                stack.pop()

    # 출력이 이 문법들에 걸려서 두 번씩 찍히는 상황이 발생.
    if not stack and check == 0:       # "("를 다 없애서 stack이 비어 있는 경우 == 짝이 맞다.
        print("YES")
    elif stack != 0 and check == 0:    # stack이 비어있지 않은 경우 : 예 ((
        print("NO")

# error1: 24번째 코드 elif가 아니라 else로 해서 아무 조건도 안주니까
# 이번엔 ))을 입력하면 NO가 2번 찍히는 상황
