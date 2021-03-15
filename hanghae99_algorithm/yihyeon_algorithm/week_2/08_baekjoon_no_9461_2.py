# 백준 9461번 (파도반 수열)

test_case = int(input())

for _ in range(test_case):
    num = int(input())
    wave = [0, 1, 1, 1, 2, 2]

    if num > 5:
        for i in range(6, num+1):
            wave.append(wave[i-5] + wave[i-1])

    print(wave[num])

# mistake 1: 첫 번째 num을 찍으면 잘 찍히는데,
# 두 번째 num을 찍으면 값이 다시 i=6부터 누적 돼서 찍히기 때문에 총 합이 이상하게 나온다.
# ...진짜 바보냐고... 왜 전역변수로 선언해 놓냐고... 이거에 2시간 썼냐고 지금...




