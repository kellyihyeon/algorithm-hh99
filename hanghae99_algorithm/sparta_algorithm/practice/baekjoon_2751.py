# 백준 2751번 (수 정렬하기 2)

n = int(input())        # n = 5
list = []

for i in range(n):
    m = int(input())
    list.append(m)

answer = sorted(list)
for j in answer:
    print(j)

# 시간 초과 뜸. 다른 방법은 모르겠다.
# 실수1: for i in range(n): 에서 for문을 n만큼 돌리려면 range함수를 이용해야 하는데,
#       자꾸 range 빼먹고 돌리니까 에러뜨지.



