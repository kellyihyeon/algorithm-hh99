# 백준 1929번(소수 구하기)

# 숫자가 하나씩 들어와야, 그 숫자가 소수인지 판단을 하니까 함수를 만들자.
# def sosu(num):  # 예를 들어 8부터 16까지 넣어보자.
#     # 소수는 2부터 시작 해야 하니까.
#     if num < 2:
#         return False
#     for i in range(2, num):   # i = 2,3,4,5,6,7,8,9,10         /# num = 11
#         if num % i == 0:    # 11 % 2 == 1
#             return False
#     return True
#
# # 입력
# m, n = map(int, input().split())  # 8 16
#
# for i in range(m, n+1):
#     if sosu(i): #i = 8,9,10,11,12,13,14,15,16/ true면 i를 찍어라.
#         print(i)

# >> 시간초과 코드


# 승민님 코드 (이 코드 아니었으면 오늘 '소수구하기' 이해하기 포기했을 듯)
a, b = map(int, input().split())  # 8 16
answer = []
visited = [0 for _ in range(b+1)]   #[0,0,0,0...] 0이 16개인 리스트   #visited = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# print("테스트용 visited: ", visited)    # ..? 17개 나오는데...
# test = [0] * (b)
# print(test)

def eratos():
    for i in range(2, b+1):     # i = 2,3,4,5,6,7,8,9....16
        if visited[i] == 0:     # 방문을 안한 곳은 0 (소수라는 뜻), 방문을 한 곳은 1
            # if a <= i & i <= b:
            #     answer.append(i)
            for j in range(i*2, b+1, i):    # for j in range(4, 17, 2씩 증가) j = 4,6,8,10,12,14,16 / 6, 9, 12, 15
                visited[j] = 1  # i=2일 때,i=3일 때 visited = [0,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,1]

eratos()
for i in range(a, b+1):     # i = 8,9,10...16
   if i > 1 and visited[i] == 0:
       print(i)
