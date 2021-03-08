# while문 사용해보기

a = 5
while a != -1:
    print(a)
    a -= 2

#무한루프 빠져나오기
# while True:
#     print("무한루프에 걸리면, CTRL+C로 빠져나오세요!!!")
# ?? 안나와지는데??

while True:
    response = input('숫자 입력: ')
    result = int(response) % 10
    if result == 0:
        continue
    print("10으로 나눈 나머지는 {}입니다.".format(result))