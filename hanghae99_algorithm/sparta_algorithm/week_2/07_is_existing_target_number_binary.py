finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]

# 낚시 문제. 이진 탐색을 하려면 정렬부터 해야 한다.
def is_exist_target_number_binary(target, numbers):
    # 순차탐색
    for i in numbers:
        if target == i:
            return True
    return False

result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)

