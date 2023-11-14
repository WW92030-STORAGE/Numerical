import math

def trapezoid(func, a, b, n):
    h = (b - a) / n
    res = func(a) + func(b)
    for i in range(n - 1):
        res = res + 2 * func(a + h * (i + 1))
    
    return res * h * 0.5
    
def func2(x):
    return x * x

print(trapezoid(func2, 0, 1, 1000))
