# 백준 4949번(균형잡힌 세상)
# 9012 괄호문제와 비슷한 문제라고 한다.(9012도 풀어보자)
# not bracket_stack: stack=[]니까, '스택이 비어있으면' 이라는 의미. * not bracket_stack == stack=[]
# ' .'을 입력한 경우: switch(True)면서 스택에 아무것도 없으니까 (stack=[]) 'yes'를 출력하게 된다.
while True:
    sentences = input()
    if sentences == ".":
        break
        print("입력의 종료조건으로 '.'이 들어온 경우")
    stack = []                          # for문 돌면서 만나게 되는 괄호들을 넣어줄 리스트
    switch = True

    for char in sentences:
        if char == "(" or char == "[":  # 순서 예시: ( [ ] ( ) )
            stack.append(char)          # stack = [ ( ]

        # ( [ 를 스택에 넣어놓고 다음 짝을 찾아서 -> ) 나 ]를 만날 경우.
        elif char == ")":
            if not stack:               # 순서 예시: )( -> stack = [ ] 비어있음.
                switch = False          # A rope may form )( a trail in a maze.(예시, 빼먹으면 안돼!)
                break
            if stack[-1] == "(":        # stack = [ ( ]
                stack.pop()             # stack = [   ] -> 짝을 만나면 pop으로 흔적 지우기
            else:                       # 순서 예시: ( [ ")" ] 일 경우
                switch = False          # stack =[ ( [ ] -> 맨 마지막 인덱스가 "]" = 짝이 안맞으니 균형이 안맞다. False로 끝내기.
                break
        elif char == "]":
            if not stack:              # 순서 예시(마찬가지): ][ -> stack = [ ] 비어있음.
                switch = False
                break
            if stack[-1] == "[":
                stack.pop()
            else:
                switch = False
                break
    # 결론
    if switch and not stack:            # 짝이 맞아 균형을 이룬다면 stack 리스트에서 전부 pop 해줬기 때문에, stack=[]이면 균형 잡혀있다.
        print("yes")
    else:
        print("no")

# 테스트 예시
# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .
