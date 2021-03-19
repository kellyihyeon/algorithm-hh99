def count_down(number):
    if number < 0:
        return
    print(number)          # number를 출력하고
    count_down(number - 1) # count_down 함수를 number - 1 인자를 주고 다시 호출한다!


count_down(60)

# RecursionError: maximum recursion depth exceeded while calling a Python object
# 재귀함수를 하기 위해서는 탈출 조건도 있어야 한다! 무한루프에 빠지는 걸 조심하자.