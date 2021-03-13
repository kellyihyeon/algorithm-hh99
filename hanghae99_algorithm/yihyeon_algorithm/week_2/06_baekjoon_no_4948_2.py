# 백준 4948번 (베르트랑 공준)

# 정수의 범위는 n < x <= 2n.
# n이 10이라면, 구해야 하는 소수의 범위는 10 < x <= 20

# 123456*2 까지 소수를 모두 구한 배열을 만들자.
def prime():
    visited = [0] * ((2 * 123456) + 1)  # 소수가 아닌 배수들을 1로 체크 해주자.

    for i in range(2, (2 * 123456) + 1):  # i는 2~ 123456*2 까지
        if visited[i] == 0:
            for j in range(i * 2, (2 * 123456) + 1, i):  # j의 범위는 4 ~ 6까지 체크, i만큼 증가니까 j는 4,6
                visited[j] = 1
    return visited

list = prime()          # visited가 담김
while True:
    n = int(input())
    if n == 0:
        break

    count = 0
    for i in range():          # 0부터 123456*2 까지 소수리스트를 다 돌아. n = 6이라면
        # list = [0,0,0,0,1,0,1,~~~~~~~~]
        if list[n]
    print(count)



# 고치고 싶은 것: 입력을 한 번에 받고 0을 입력했을 때 종료가 되면서 출력값을 한 번에 받고 싶은데,
# 정수 하나 입력하면 그에 맞는 출력 값 뜨고 이런 식.


