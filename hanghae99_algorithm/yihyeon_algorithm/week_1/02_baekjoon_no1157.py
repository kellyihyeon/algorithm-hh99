# 입력

words = input().upper()     #pinnokiio
unique_words = list(set(words)) #pinok

cnt_list = []
for x in unique_words:  #x = p, i, n, o, k
    cnt = words.count(x)    #p=1, cnt=1, i=3, cnt=3
    cnt_list.append(cnt)    #cnt_list = [1, 3, 2, 2, 1]

if cnt_list.count(max(cnt_list)) > 1:       #cnt_list.count(3) = 1
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list))   #max_index = 1
    print(unique_words[max_index])