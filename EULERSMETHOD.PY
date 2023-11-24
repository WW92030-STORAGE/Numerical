import math

def deriv(x, y):
    return x + y # Example derivative

def euler(deriv, x0, y0, h, steps):
    rety = [y0]
    retx = [x0]
    for i in range(steps):
        tempy = y0
        y0 = y0 + h * deriv(x0, tempy)
        x0 = x0 + h
        
        retx.append(x0)
        rety.append(y0)
    
    return [retx, rety]
