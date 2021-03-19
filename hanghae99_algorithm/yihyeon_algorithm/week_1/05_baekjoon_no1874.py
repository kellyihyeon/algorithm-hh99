# 백준 1874번 (스택 수열)

# 범위 1 <= n <= 100,000/   n= 8.

# 리스트 [1, 2, 3, 4, 5, 6, 7, 8] (오름차순)
# 리스트에서 4, 3, 6, 8, 7, 5, 2, 1을 뽑으려면?
# [+ + + + - - + + - + + - - - - -]
# 첫번째 수를 뽑으려면 우선 push == 첫번째 수만큼하고 pop하면 첫번째 수를 뽑을 수 있다.
# pop을 할 때는 -1만큼,
# 테스트용: 1,2,5,3,4 / n= 5    /count=1,2,3,4,5,6
# [1/2/3,4,5/] / [+ - + - + + + -] ->'3'에서 False터짐. -> 'NO'

n = int(input())
stack = []
mark_list = []
count = 1
switch = True

for i in range(n):                  # n = 8, 8번 돌면서 숫자 체크
    number = int(input())           # 4/                                3/ 6, 8, 7, 5, 2, 1
    while count <= number:          # 1<=4/ 2<=4/ 3<=4/ 4<=4/ 5<=4(x)
        stack.append(count)         # stack = [1/2/3/4 ]
        mark_list.append('+')       # mark_list = [+/+/+/+]
        count += 1                  # count = 2/3/4/5                /6
    if stack[-1] == number:         # stack = [1/2/3/4 ] -> 4 == 4/  [1/2/3/ ]
        stack.pop()                 # stack = [1/2/3/ ]              [1/2/ ]
        mark_list.append('-')       # mark_list = [+/+/+/+/-]        [+/+/+/+/-/-]
    else:
        switch = False

if switch == True:
    for mark in mark_list:
        print(mark)
else:
    print('NO')





