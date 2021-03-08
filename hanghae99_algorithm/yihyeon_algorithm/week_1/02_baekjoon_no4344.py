#no 4344 평균은 넘겠지

#입력
n = int(input())    # 테스트 케이스의 수

for _ in range(n):   # 5번 반복
    nums = list(map(int, input().split())) # test_table = [5, 50, 50, 70, 90, 100]
    avg = sum(nums[1:]) / nums[0]    # 평균 = 점수/학생 수

    count = 0
    for score in nums[1:]:
        if score > avg:
            count += 1  # 평균이 넘으면 카운트 하기
    # 평균을 넘는 학생들의 비율
    rate = count / nums[0] * 100
    # 비율-> 반올림하여 소수점 셋째 자리까지 출력
    print(f'{rate:.3f}%')
