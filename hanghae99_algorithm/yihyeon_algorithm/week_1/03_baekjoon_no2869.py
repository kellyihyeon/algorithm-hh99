# 백준 2869번(달팽이는 올라가고 싶다.)

# 입력
climbing, sliding, height  = map(int, input().split())

day = 0
result = 0

while True:
    day += 1    #1일차 #2일차 #3일차 #4일차
    result = result + climbing  #2미터 #3미터 #4미터 #5미터
    if result == height:    #5미터 == 5미터(4일차에 성공)
        print(day)
        break
    result = result - sliding   #총 올라간 높이 = 1미터 #2미터 #3미터

# >> 시간 초과 됨...

# 반복문 안돌리고 짜는 코드
climbing, sliding, height  = map(int, input().split())
# 막대가 5미터이고, 올라갈 때 5미터 미끄러지면 1미터라고 가정.
# day = 막대4미터 / 4미터 = 1
# 막대가 10미터라면, day = 막대 9미터 / 4미터 = 2.2222 => +1 =
# day = (height-sliding) / (climbing-sliding)
day = 0
if (height-sliding) % (climbing-sliding) == 0:
    day = (height-sliding) // (climbing-sliding)
else:
    day = (height-sliding) // (climbing-sliding) + 1
print(day)



