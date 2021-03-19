# 백준 1436번(영화감독 숌)

# Brute Force

n = int(input())
diehard = 666
find = 0

# brute force 방법을 써서 무한정 +1을 해나가자.
while True:
    # 666이 diehard안에 있기만 하면 되니까 있는지 확인하는 코드를 만들자.
    if "666" in str(diehard):
        # 포함 돼 있으면? 몇 번째인지 세자.
        find += 1

    if n == find:
        print(diehard)
        break

    diehard += 1        # 1번 = 666, 2번 = 1666 3번= 2666, 4번 = 3666
