import numpy as np

a = np.arange(1,25).reshape(2,12)
print(a)

a1 = np.hsplit(a,3)
print(a1)
