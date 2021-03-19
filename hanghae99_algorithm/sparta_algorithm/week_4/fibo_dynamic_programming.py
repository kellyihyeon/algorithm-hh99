input = 7

memo = {
    1:1,
    2:1
}

def fibo_dynamic_programming(n, fibo_name):

    for i in range(3, n+1):
        if i in fibo_name:
            return fibo_name[i]
        else:
            fibo_name[i] = fibo_name[i-1] + fibo_name[i-2]

    return fibo_name[i]

print(fibo_dynamic_programming(input, memo))