import numpy as np
import matplotlib.pyplot as pyplt

x = np.arange(0, 6, 0.1)
y = np.sin(x)
y2 = np.cos(x)

pyplt.plot(x, y, linestyle = "--", label ="sin")
pyplt.plot(x, y2, label ="cos")
pyplt.xlabel("x")
pyplt.ylabel("y")
pyplt.title('sin&cos')
# pyplt.legend()
pyplt.show()
