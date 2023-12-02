def newton(func, x0):
    x = x0
    h = 0.00001
    for i in range(64):
        d = (func(x0 + h) - func(x0)) / h
        if (d == 0):
            d = d + 0.0000000001
        x0 = x0 - func(x0) / d
    return x0

def reveulerstep(deriv, x, y, h):
    # Y = y + h * F(x + h, Y) => 0 = y + h * F(x + h, Y) - Y
    def piece(n):
        return y + h * deriv(x + h, n) - n
    
    return newton(piece, y)

def reveuler(deriv, x, y, h, steps):
    dx = [x]
    dy = [y]
    for i in range(steps):
        y = reveulerstep(deriv, x, y, h)
        x = x + h
        dx.append(x)
        dy.append(y)
    return [dx, dy]
