import math

def deriv(x, y):
    return 2 * x
    
def rk4step(deriv, x, y, h):
    s1 = deriv(x, y)
    s2 = deriv(x + 0.5 * h, y + 0.5 * h * s1)
    s3 = deriv(x + 0.5 * h, y + 0.5 * h * s2)
    s4 = deriv(x + h, y + h * s3)
    # print(x, y, s1, s2, s3, s4)
    
    return y + (h / 6) * (s1 + s2 + s2 + s3 + s3 + s4)

def rk4(deriv, x, y, h, steps):
    xp = [x]
    yp = [y]
    for i in range(steps):
        y = rk4step(deriv, x, y, h)
        x = x + h
        xp.append(x)
        yp.append(y)
    
    return [xp, yp]
