# 백준 1316번(그룹 단어 체커)

# 그룹 단어?
# 단어가 주어졌을 때 (ex. happy) 연속해서 같은 알파벳이 나오든지, 한 번만 나오든지(중복 되면 안된다.)

n = int(input())            # n = 3
count = n

for i in range(n):          # i = 0,1,2 즉, 3번 돌아라./ n = 2, i = 0, 1
    word = input()          # newn 가 그룹단어인지? happy = 5글자
    for j in range(len(word)-1):      # i = 0,1,2,3,4
        if word[j] != word[j+1]:    # word = happy
            if word[j] in word[j+1: ]:
                count = count - 1           # count = 2
                break
print(count)