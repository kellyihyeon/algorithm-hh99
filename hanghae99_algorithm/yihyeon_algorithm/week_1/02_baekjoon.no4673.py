#백준 4673 셀프넘버

natural_num = set(range(1, 10001))
generated_num = set()

for i in range(1, 10001):   # range니까 1부터 10000까지 찍기(순서!!!) i= 850
    for j in str(i):    # str("850") -> j.  j = "8", "5", "0"
        i = i + int(j)
    generated_num.add(i)

self_num = sorted(natural_num - generated_num)  #순서가 뒤죽박죽이니까 정렬
for i in self_num:
    print(i)
