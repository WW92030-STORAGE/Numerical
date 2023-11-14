import math

def func(x):
    return math.sqrt(1 + (1.0 / math.cos(x)) ** 4) # d/dx tan(x) = sec(x) ** 2
    
def simpson(func, a, b, n):
    h = (b - a) / n
    res = func(a) + func(b)
    for i in range(n):
        res = res + 4 * func(a + h * 0.5 * (2 * i + 1))
    for i in range(n - 1):
        res = res + 2 * func(a + h * (i + 1))
    return res * h / 6

print(simpson(func, 0, math.pi / 4, 32)) # 1.2779780695831768
