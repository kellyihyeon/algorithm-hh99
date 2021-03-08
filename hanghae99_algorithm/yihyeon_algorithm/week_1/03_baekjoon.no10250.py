# 백준 10250번(ACM호텔)

# 입력
test = int(input())
for i in range(test):
    height, width, order  = map(int, input().split())
    floor = 0
    ho = 0
    # height 6층짜리, width 12호까지, order 6번째, 12번째 왔을 때
    if order % height == 0 :
        floor = height * 100
        ho = order // height
    else:   # order 8번째, 9번째인 경우
        floor = (order % height) * 100  # 2층 # 3층
        ho = 1 + order // height        # 1+1=2호 # 1+1=2호
    room_number = floor + ho
    print(room_number)


