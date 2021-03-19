# 백준 9184번 (신나는 함수 실행)
# 정말 무슨 말인지 이해할 수가 없다. dp[][][]의 의미도 모르겠고, dp를 왜 저렇게 배열로 많이 만들어놓는지도 모르겠다.

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:             # 얘는 뭐야
        return dp[a][b][c]

    if a < b < c:
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

    return dp[a][b][c]

dp = [[[0]* 21 for _ in range(21)] for _ in range(21)]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print("w({}, {}, {}) = {}".format(a,b,c,w(a,b,c)))