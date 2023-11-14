import math
import numpy as np

# PROTOtype GENerator of natural cubic splines through the points [xp, yp] where xp is in sorted order
def protogen(xp, yp):
    if (len(xp) != len(yp)):
        return []
    n = len(xp) # number of data points
    
    A = []
    B = []
    
    a = []
    d = []
    D = []
    
    # SETUP
    
    for i in range(n):
        A.append([])
        B.append(0)
        a.append(0)
        d.append(0)
        D.append(0)
        for j in range(n):
            A[i].append(0)
        
    for i in range(n - 1):
        a[i] = yp[i]
        d[i] = xp[i + 1] - xp[i]
        D[i] = yp[i + 1] - yp[i]
    
    A[0][0] = A[n - 1][n - 1] = 1
    
    for i in range(1, n - 1):
        A[i][i - 1] = d[i - 1]
        A[i][i + 1] = d[i]
        A[i][i] = 2 * (d[i - 1] + d[i])
        
        B[i] = 3 * (D[i + 1] - D[i]) / (d[i + 1] - d[i])
    
    # SOLVE
    
    CX = np.linalg.solve(np.array(A), np.array(B))
    
    print(CX)
    
    DX = []
    BX = []
    
    for i in range(n - 1):
        DX.append(0)
        BX.append(0)
    
    for i in range(n - 1):
        DX[i] = (CX[i + 1] - CX[i]) / (3 * d[i])
        BX[i] = (D[i] / d[i]) - (d[i] / 3) * (2 * CX[i] + CX[i + 1])
    
    return [a, BX, CX, DX]

def eval(x, xval, spline):
    n = len(xval)
    theone = 0
    for i in range(n - 1):
        if (x >= xval[i]):
            theone = i
            break
        
    dx = (x - xval[theone])
    
    res = spline[0][theone]
    res = res + dx * spline[1][theone]
    res = res + dx * dx * spline[2][theone]
    res = res + dx * dx * dx * spline[3][theone]
    return res


xval = [0, 10, 30, 40]
yval = [0, 10, 20, 30]

res = protogen(xval, yval)
    
print(eval(20, xval, res))
