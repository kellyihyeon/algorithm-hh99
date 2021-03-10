# 백준 1021번 (회전하는 큐)

# 문제 이해
# 10 3          큐의 크기 10(n). 뽑아내려는 수의 개수 3(m).
# 2 9 5         뽑아내려는 숫자: 2, 9, 5

# list가 비어있으면 False인 것을 잘 활용하자.

# 큐를 왼쪽으로 돌릴지, 오른쪽으로 돌릴지 함수 짜놓기
def move_left(que, count):          # que = [1,2,3,4,5,6,7,8,9,10] <- 2를 뽑자
    count = count + 1               # 1번 이동
    delete_head = que.pop(0)        # que = [2,3,4,5,6,7,8,9,10]
    que.append(delete_head)         # que = [2,3,4,5,6,7,8,9,10,1]
    return que, count               # que = [2,3,4,5,6,7,8,9,10,1], count = 1

def move_right(que, count):
    count = count + 1               # que = [1,2,3,4,5,6,7,8,9,10] <- 9를 뽑자
    delete_head = [que.pop()]       # delete_head = [10], que = [1,2,3,4,5,6,7,8,9]
    que = delete_head + que         # que = [10,1,2,3,4,5,6,7,8,9]  / 파이썬 콘솔 돌리니까 이렇게 나옴.
    return que, count               # 이걸 count=2번 하면, que = [9,10,1,2,3,4,5,6,7,8]


n, m = map(int, input().split())                        # 10, 3
output_nums_list = list(map(int, input().split()))      # 2, 9, 5

# 큐를 만들어 놓자.
que = list(range(1, n+1))               # que = [1,2,3,4,5,6,7,8,9,10]
count = 0                               # 몇번 옮겼는지 세야 하니까

while output_nums_list:                 # [2, 9, 5] -> 2를 뽑자.   // 리스트를 다 뽑고 나면 output_nums_list=[]가 되는데 ==False!
    if que[0] == output_nums_list[0]:   # que = [2,3,4,5,6,7,8,9,10,1], count = 1
        que.pop(0)                      # 2, que = [3,4,5,6,7,8,9,10,1]
        output_nums_list.pop(0)         # 2, output_nums_list = [9, 5]
    else:                               # que = [1,2,3,4,'5',6,7,8,9,10]
        if que.index(output_nums_list[0]) <= len(que) // 2:     # 3 <= 5    (5보다 왼쪽에 있으니까 왼쪽으로 돌리자)
            while que[0] != output_nums_list[0]:                # 1 != 2 == True
                que, count = move_left(que, count)
        else:                           #que.index(output_nums_list[0]) > len(que) // 2:
            while que[0] != output_nums_list[0]:
                que, count = move_right(que, count)

print(count)


