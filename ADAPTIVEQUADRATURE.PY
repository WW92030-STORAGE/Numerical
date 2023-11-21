def trapezoid(func, a, b): # Area of each panel
    return (b - a) * 0.5 * (func(a) + func(b))

def simpson(func, a, b):
    H = (b - a) * 0.5
    M = (a + b) * 0.5
    return (H / 3.0) * (func(a) + func(b) + 4 * func(M))

def aq_trapezoid(func, a, b, a0, b0, T):
    H0 = b0 - a0
    H = b - a
    M = 0.5 * (a + b)
    h0 = trapezoid(func, a, M)
    h1 = trapezoid(func, M, b)
    hx = trapezoid(func, a, b)
    if abs(h0 + h1 - hx) > 3 * T * H / H0:
        return aq_trapezoid(func, a, M, a0, b0, T) + aq_trapezoid(func, M, b, a0, b0, T)
    return h0 + h1

def aq_simpson(func, a, b, a0, b0, T): # SIMPSON
    H0 = b0 - a0
    H = b - a
    M = 0.5 * (a + b)
    h0 = simpson(func, a, M)
    h1 = simpson(func, M, b)
    hx = simpson(func, a, b)
    if abs(h0 + h1 - hx) > 15 * T * H / H0: # Simpson's rule : 3 --> 15
        return aq_simpson(func, a, M, a0, b0, T) + aq_simpson(func, M, b, a0, b0, T)
    return h0 + h1
    
def integral_trapezoid(func, a, b, T):
    return aq_trapezoid(func, a, b, a, b, T)
    
def integral_simpson(func, a, b, T):
    return aq_simpson(func, a, b, a, b, T)

def func(x):
    return x ** 5 + 2 * x ** 3 - 9 * x
    
B = 20
E = 0.0001

print(integral_trapezoid(func, 0, B, E))
print(integral_simpson(func, 0, B, E))
print(B ** 6 / 6 + 2 * B ** 4 / 4 - 9 * B ** 2 / 2)
