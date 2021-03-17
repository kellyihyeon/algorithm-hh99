# 백준 2630번 (색종이 만들기)

import sys

# n = int(sys.stdin.readline())
#
# color_paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]  # x행 y열

n = 8
color_paper =  [[1, 1, 0, 0, 0, 0, 1, 1],
                [1, 1, 0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1, 1, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0],
                [1, 0, 0, 0, 1, 1, 1, 1],
                [0, 1, 0, 0, 1, 1, 1, 1],
                [0, 0, 1, 1, 1, 1, 1, 1],
                [0, 0, 1, 1, 1, 1, 1, 1]]

white = 0  # 0이면 흰생
blue = 0  # 1이면 파란색


def cut(x, y, n):
    global blue, white
    check = color_paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != color_paper[i][j]:  # 하나라도 같은색이 아니라면
                # 4등분
                cut(x, y, n // 2)  # 1사분면
                cut(x, y + n // 2, n // 2)  # 2사분면
                cut(x + n // 2, y, n // 2)  # 3사분면
                cut(x + n // 2, y + n // 2, n // 2)  # 4사분면
                return

    if check == 0:  # 모두 흰색일때
        white += 1
        return
    else:  # 모두 파란색일때
        blue += 1
        return

cut(0, 0, n)
print(white)
print(blue)

# 재귀 미치겠네, 분할 했을 때 그 분할한 부분은 이해를 하겠는데,
# 이게 큰 부분이랑 다시 합쳐질 때? 그쪽에서 어떻게 합쳐야 되는 건지 그 부분을 도저히 이해를 못하겠다.
