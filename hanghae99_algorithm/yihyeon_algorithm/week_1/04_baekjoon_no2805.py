# 백준 2805번 (나무 자르기)

tree, take = map(int, input().split())      # 4 7
height = list(map(int, input().split()))    # 20 15 10 17

# 톱날의 높이가 10일 때 가져갈 수 있는 나무의 양을 계산하자.
def tree_sum(mid_height):
    sum = 0
    for i in height:                # i = 20, 15, 10, 17
        if i - mid_height > 0:      #     10, 5,  0,  7  # 15일 때: 5, 0, 0, 2 / 18일 때: 2, 0, 0, 0
            sum = sum + (i - mid_height)     # sum = 22    /sum = 7             / sum = 2
    return sum

def binary_search(take):    # 나무길이 7미터를 집에 가져가길 원한다.
    # 톱날에 설정할 수 있는 높이의 최소값은 0, 최대값은 20이다.
    min_height = 0
    max_height = max(height)
    save_saw_height = 0
    # 0 20
    while(min_height <= max_height):                    # 16 <= 20                  /16 <= 18....
        # 업다운을 하기 위해 톱의 중간 높이를 지정하자.
        mid_height = (min_height + max_height) // 2     # 중간 높이는 10./   15  / 18
        sum = tree_sum(mid_height)                      # sum = 22
        if sum < take:                                  #                      / 2  < 7
            max_height = mid_height - 1                 # 최대 높이:            / 17
        if sum >= take:                                 # 가져갈 수 있는 22 >= 가져가려는 7/   7 >= 7
            save_saw_height = mid_height                # 중간 높이: 10일 때.-> up!해야돼.      15
            min_height = mid_height + 1                 # 최소 높이: 11로 테스트 해보자..../    16
    return save_saw_height                              # 15

print(binary_search(take))

# 팀원들이 알려준 것
#>> ?. sum == take 같을 때 바로 출력하면 되지 않나?
#>> !. 조건이 start지점과 end지점이 교차돼야 while문이 끝나면서 정확한 값을 뽑아내는 것이다.
# 지점이 같을 때 출력해서 끝내도 된다.
#  if ans>b:
#         start = mid+1
#     elif ans==b:
#         end=mid
#         break
#     else:
#         end =mid-1
# 팀원분은 end가 출력값이라 mid를 end에 넣고 끝낸 것.