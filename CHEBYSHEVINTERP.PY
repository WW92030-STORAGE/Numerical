import math
import numpy as np

# ENDPOINTS AND NODE COUNT
A = 0
B = math.pi / 2
N = 32

# RADIUS AND CENTER
R = 0.5 * abs(B - A)
C = 0.5 * (A + B)

# CHEBYSHEV NODES
def chebyshev():
    list = []
    for i in range(N):
        list.append(C + R * math.cos((2 * i + 1) * math.pi / (2 * N)) )
    return list

# THE FUNCTION AND THE INTERPOLATION

def func(x):
    return math.cos(x)

def map(inputs):
    outputs = []
    for i in range(len(inputs)):
        outputs.append(func(inputs[i]))
    return outputs

def vandermonde(inputs):
    n = len(inputs)
    mat = []
    for i in range(n):
        lis = []
        for j in range(n):
            lis.append(math.pow(inputs[i], j))
        mat.append(lis)
    
    return mat

def poly(list, x):
    res = 0
    for i in range(len(list)):
        res = x * res + list[len(list) - i - 1]
    return res

# RUNNER PROGRAM

inputs = chebyshev()
outputs = map(inputs)

A = np.array(vandermonde(inputs))
B = np.array(outputs)

# print(inputs, "\n", outputs)

x = np.linalg.solve(A, B) # Interpolation polynomial!

# print(x)

iter = 64

for i in range(iter):
    x0 = math.pi * i / (2 * iter)
    print(x0, abs(math.cos(x0) - poly(x, x0))) # Orders of 10^-15 and 10^-16
    # print(x0, math.cos(x0), poly(x, x0))
