# using dictionary
user = {}
user['age'] = 25
user['address'] = 'seoul'

print(user)

#
live_in_seoul= True
if live_in_seoul:
    print('서울에 살아요')
print()

test_for = [1,4,5,6,2342,3,4,76]

for result in test_for:
    if result%2 == 0:
        print(result)

print()
for result in test_for:
    if result > 30:
        print(result, 'stop!!!')
        break


num = [1,2,3,4,5,6,7,8,9,10]
add = 0
for result in num:
    add = add + result
print(add)
print()

for odd in num:
    if odd % 2 != 0 :
        print(odd)

print()
def get_odd(a):
    if(a%2 != 0):
        return a
    else:
        even = '짝수 입니다.'
        return even


result = get_odd(937234)
print(result)

a = "i am doing well"
print(len(a))

def triangle (width, height):
    rule = width * height / 2
    return rule

print(triangle(4,6))

