# 백준 11651번(좌표 정렬하기 2)
# >> 시간초과 된 코드

num = int(input())
coordinate_list = []
for i in range(num):
    [x, y] = map(int, input().split())
    rev = [y, x]
    coordinate_list.append(rev)
coordinate_list = sorted(coordinate_list)
for i in range(num):
    print(coordinate_list[i][1], coordinate_list[i][0])




