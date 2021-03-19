def hap(a, b):
    print(a + b)

def gop(a, b):
    print(a * b)

def hap_gop(a, b):
    hap(a, b)
    gop(a, b)

def countdown(n):
    if n == 0:
        print("Blastoff!!!")
    else:
        print(n)
        countdown(n-1)



hap(3, 90)
gop(3, 90)
hap_gop(5, 7)

countdown(10)