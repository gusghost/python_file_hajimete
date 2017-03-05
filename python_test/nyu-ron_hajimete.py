import numpy as np
import matplotlib.pylib as plt


def step_function(x):
    if x > 0:
        return 1
    else:
        return 0


print(step_function(1))


def step_function2(x):
    y = x > 0
    a = np.int(y)
    # if y:
    #     a = 1
    # else:
    #     a = 0

    return a


print(step_function2(1))
