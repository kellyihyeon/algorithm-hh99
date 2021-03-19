# 튜터님 코드

input = 50

memo = {
    1:1,
    2:1
}

def fibo_dynamic_programming(n, fibo_name):
    if n in fibo_name:
        return fibo_name[n]

    nth_fibo = fibo_dynamic_programming(n-1, fibo_name) + fibo_dynamic_programming(n-2, fibo_name)
    fibo_name[n] = nth_fibo

    return nth_fibo

print(fibo_dynamic_programming(input, memo))