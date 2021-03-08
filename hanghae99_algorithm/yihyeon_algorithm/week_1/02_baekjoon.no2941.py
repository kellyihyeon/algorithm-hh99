#백준 2941 크로아티아 알파벳

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']
word = input()  #word = ljes=njak

for i in croatia:   #'c=','c-','dz=','d-','lj','nj','s=','z='
    word = word.replace(i, '*')     #word = ljes=njak = *e**ak
print(len(word))