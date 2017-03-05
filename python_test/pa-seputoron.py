import numpy as np
import matplotlib.pyplot as plt



def NAND(in1, in2):
    x = np.array([in1, in2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(x * w) + b
    if tmp <= 0:
        return 0
    else:
        return 1

def AND(in1, in2):
    x = np.array([in1, in2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(x*w)+b
    if tmp <= 0:
        return 0
    else:
        return 1


def OR(in1, in2):
    x = np.array([in1, in2])
    w = np.array([0.5, 0.5])
    b = -0.3
    tmp = np.sum(x*w)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR (in1, in2):
    s1 = NAND(in1, in2)
    s2 = OR(in1,in2)
    temp = AND(s1, s2)
    return temp

print('XOR=')
print(XOR(1,1 ))
print(XOR(0,1 ))
print(XOR(1,0 ))
print(XOR(0,0 ))
print('EOF (ツ)')

x = np.array([0,1])
weight = np.array([0.5, 0.5])
bias = -0.7
weight*x
print(weight*x)
np.sum(weight*x) + bias
print(np.sum(weight*x)+bias)
