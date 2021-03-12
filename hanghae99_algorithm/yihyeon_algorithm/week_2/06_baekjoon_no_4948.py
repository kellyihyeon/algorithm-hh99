# 백준 4948번 (베르트랑 공준)

# 정수의 범위는 n < x <= 2n.
# n이 10이라면, 구해야 하는 소수의 범위는 10 < x <= 20

# visited = [0,0,0,0,0,0,0]

# 어렵게 생각하지 말고, a = n, b = 2*n (** n=3이라면, a= 3, b=6)

def find_prime_count():
    visited = [0] * ((2*n) + 1)                      # 소수가 아닌 배수들을 1로 체크 해주자.
    for i in range(2, (2*n) + 1):                    # i는 2~6까지
        if visited[i] == 0:
            for j in range(i*2, (2*n) + 1, i):       # j의 범위는 4 ~ 6까지 체크, i만큼 증가니까 j는 4,6
                visited[j] = 1                       # j는 4,6 이다. 4,6 자리에 1로 표시하라.(배수니까)
        # print(visited)
        # 잘 나오지만, 0과 1은 소수가 아니니까 제외시키자.
    count = 0
    for i in range(n, (2*n) + 1):                    # i는 3부터 6까지. i = 3,4,5,6
        if i > 1 and visited[i] == 0:
            count += 1
    print(count)

# 입력 받기. 입력의 마지막에는 0이 주어진다. 0이 들어오면 종료.
while True:
    n = int(input())
    if n == 0:
        break
    find_prime_count()



# 고치고 싶은 것: 입력을 한 번에 받고 0을 입력했을 때 종료가 되면서 출력값을 한 번에 받고 싶은데,
# 정수 하나 입력하면 그에 맞는 출력 값 뜨고 이런 식.
# 도저히 모르겠다.


