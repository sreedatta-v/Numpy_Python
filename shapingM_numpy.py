import numpy as np
from numpy.random._examples.numba.extending import rg

a = np.floor(10 * rg.random((3, 4)))
print(a)
